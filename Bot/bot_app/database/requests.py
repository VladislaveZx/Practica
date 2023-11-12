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
        # get the date format day-month-year
        now = f"{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}"
        # get the request where studnum = studnum and data_send = now
        result = await session.execute(
            select(Request).where(
                Request.studnum == studnum 
                and 
                Request.data_send == now
            )
        )
        request = result.scalars().first()
        if not request:
            result = Request(
                telegram_id=user, 
                studnum=studnum, 
                studname=studname,
                organisation=organisation,
                data_send=str(now),
                status=False
                )
            session.add(request)
            await session.commit()
            return False
        return request