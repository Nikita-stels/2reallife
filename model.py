from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(63), nullable=False)
    personal_account = Column(Float)
    prize_fund_account = Column(Float)
    prize_fund = relationship('PrizeFund', back_populates='users')


class PrizFund(base):
    __tablename__ = 'prize_fund'
    id = Column(Integer, primary_key=True)
    name = Column(String(63), nullable=False)
    users = relationship('User', back_populates='prize_fund')
    jackpot = Column(Float)


db = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')
session_factory = sessionmaker(bind=db)
Session = scoped_session(session_factory)
#
if __name__ == '__main__':
    base.metadata.create_all(db)
