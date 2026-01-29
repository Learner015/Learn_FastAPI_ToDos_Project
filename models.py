# actual record is here
from database import Base
from sqlalchemy import Column, Integer,String, Boolean,ForeignKey

class users_a(Base):
    __tablename__ = 'users_a'
    id = Column(Integer,primary_key = True,index = True)
    email = Column(String, unique= True)
    username = Column(String, unique= True)
    f_name = Column(String)
    l_name = Column(String)
    hashed_pass = Column(String)
    is_active = Column(Boolean,default=True)
    role= Column(String)
    # phone_number= Column(String)

class todos1(Base):
    __tablename__ = 'todos1'
    id = Column(Integer,primary_key= True,index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean,default=False)
    owner_id= Column(Integer,ForeignKey("users_a.id"))