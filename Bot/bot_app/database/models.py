from sqlalchemy import Boolean
from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase

from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from ..local_settings import SQL_ALCHEMY_URL
from typing import List
from sqlalchemy import String

engine = create_async_engine(SQL_ALCHEMY_URL, echo=True)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

# class User(Base) with the telegram_id(int, primary_key), username(char 30), fullname(char 50)
class User(Base):
    __tablename__ = "users"
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String(50))
    def __repr__(self):
        return f"User(telegram_id={self.telegram_id}, username={self.username}, fullname={self.fullname})"
    def __str__(self):
        return f"User(telegram_id={self.telegram_id}, username={self.username}, fullname={self.fullname})"
    def __eq__(self, other):
        return self.telegram_id == other.telegram_id
    def __hash__(self):
        return hash(self.telegram_id)
    def __ne__(self, other):
        pass

# class Stud(telegram_id(fk), studnum(pk), studname - char, studgroup - int, studyear - int)
class Stud(Base):
    __tablename__ = "stud"
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    studnum: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    studname: Mapped[str] = mapped_column(String(30))
    studgroup: Mapped[int] = mapped_column(BigInteger)
    studyear: Mapped[int] = mapped_column(BigInteger)
    def __repr__(self):
        return f"Stud(telegram_id={self.telegram_id}, studnum={self.studnum}, studname={self.studname}, studgroup={self.studgroup}, studyear={self.studyear})"
    def __str__(self):
        return f"Stud(telegram_id={self.telegram_id}, studnum={self.studnum}, studname={self.studname}, studgroup={self.studgroup}, studyear={self.studyear})"
    def __eq__(self, other):
        pass

# class Request(telegram_id(fk), studnum(fk), studname, organisation, data_send - data)
class Request(Base):
    __tablename__ = "requests"
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    studnum: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    studname: Mapped[str] = mapped_column(String(30))
    organisation: Mapped[str] = mapped_column(String(30))
    data_send: Mapped[str] = mapped_column(String(30), primary_key=True)
    status: Mapped[bool] = mapped_column(Boolean)
    def __repr__(self):
        return f"Request(telegram_id={self.telegram_id}, studnum={self.studnum}, studname={self.studname}, organisation={self.organisation}, data_send={self.data_send})"
    def __str__(self):
        return f"Request(telegram_id={self.telegram_id}, studnum={self.studnum}, studname={self.studname}, organisation={self.organisation}, data_send={self.data_send})"
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass


# class Graph of the course(int), studgroup, week_type(str), day of week(str), time_start(str), time_end(str), place, teacher, type
class Graph(Base):
    __tablename__ = "graphs"
    course: Mapped[int] = mapped_column(BigInteger, )
    studgroup: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    week_type: Mapped[str] = mapped_column(String(30), primary_key=True)
    day_of_week: Mapped[str] = mapped_column(String(30), primary_key=True)
    time_start: Mapped[str] = mapped_column(String(30), primary_key=True)
    time_end: Mapped[str] = mapped_column(String(30))
    place: Mapped[str] = mapped_column(String(30))
    teacher: Mapped[str] = mapped_column(String(30), primary_key=True)
    type: Mapped[str] = mapped_column(String(30))
    def __repr__(self):
        pass



async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
