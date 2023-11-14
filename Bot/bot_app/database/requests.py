from .models import User, Stud, Request, Graph, async_session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError


# get or create user by telegram_id
async def get_user(telegram_id: int, username: str, full_name: str) -> User:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.telegram_id == telegram_id))
        user = result.scalars().first()
        if not user:
            user = User(telegram_id=telegram_id, username=username, fullname=full_name)
            session.add(user)
            await session.commit()
        return user
        

# add data to request table
async def add_request(user: int, studnum: int, studname: str, organisation: str) -> Request:
    import datetime
    async with async_session() as session:
        now = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}"
        result = await session.execute(
            select(Request).where(
                Request.studnum == studnum 
                and 
                Request.data_send == now
            )
        ) 
        if result.scalar() is None:
            request = Request(
                telegram_id=user, 
                studnum=studnum, 
                studname=studname, 
                organisation=organisation, 
                data_send=now, 
                status=False
            )
            session.add(request)
            await session.commit()
            return False
        else:
            return True
        
# create new user in stud by user_ id, studnum, studname, studgroup, studyear
async def create_stud(user: int, studnum: int, studname: str, studgroup: int, studyear: int) -> Stud:
    async with async_session() as session:
        result = await session.execute(select(Stud).where(Stud.telegram_id == user))
        if result.scalar() is None:
            stud = Stud(
                telegram_id=user, 
                studnum=studnum, 
                studname=studname, 
                studgroup=studgroup,
                studyear=studyear
            )
            session.add(stud)
            await session.commit()
            return False
        else:
            return True
        

async def add_user(user: int, username: str, fullname: str) -> User:
    async with async_session() as session:
        result = await session.execute(select(User).where(User.telegram_id == user))
        if result.scalar() is None:
            user = User(telegram_id=user, username=username, fullname=fullname)
            session.add(user)
            await session.commit()
            return False
        else:
            return True


# get info about graph by studgroup, day, week_type
async def get_graph_info(studgroup: str, day: str, week_type: str) -> list:
    async with async_session() as session:
        result = await session.execute(select(Graph).where(Graph.studgroup == studgroup and Graph.day_of_week == day and Graph.week_type == week_type))
        return result.scalars().all()


# add info to Graph from json file
async def refresh_graph_table(file_paths: str) -> Graph:
    # delete all rows from Graph

    async with async_session() as session:
        await session.execute(Graph.__table__.delete())
        await session.commit()
    count = 0
    error_rows = []
    for file_path in file_paths:  
        import json
        with open(file_path, 'r') as file:
            data = json.load(file)
            for group, lessons in data.items():
                for lesson in lessons:
                    day = lesson[0]
                    hour = lesson[1]
                    week_type = lesson[2]
                    name = lesson[3]
                    tutor = lesson[4]
                    async with async_session() as session:
                        try:
                        # get or create graph
                            graph = Graph(
                                studgroup=group, 
                                week_type=week_type, 
                                day_of_week=day,
                                time=hour,
                                name=name,
                                tutor=tutor
                            )
                            session.add(graph)
                            await session.commit()
                        except IntegrityError:
                            error_rows.append([group, week_type, day, hour, name, tutor])
                    count += 1
        import os   
        os.remove(file_path)
    print(
        f"Added {count} rows to Graph table\n Declined row: {error_rows}"
        )

