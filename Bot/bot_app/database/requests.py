from .models import User, Stud, Request, async_session
from sqlalchemy import select


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