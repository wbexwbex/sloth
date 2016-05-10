from sqlalchemy import Column,Integer,String,ForeignKey,Sequence,DateTime,TIMESTAMP
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlalchemy.orm import relationship
from collections import namedtuple

Base = declarative_base()

class MAccount(Base):
    __tablename__ = 'account'
    uin = Column(String(50), primary_key=True)
    passwd = Column(String(48))
    group = Column(String(50))
    registration_ip = Column(String(16))
    registration_date = Column(TIMESTAMP, nullable=False)


from collections import namedtuple
MAccountTuple = namedtuple('MAccountTuple', ('uin', 'passwd', 'group', 'registration_ip', 'registration_date'))