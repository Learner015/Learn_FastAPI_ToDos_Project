from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base as db

# postgresql://devteam:D3vteaM#21@172.16.1.8:5432/Todoapp
SQLALCHEMY_DATABASE_URL = 'postgresql://devteam:D3vteaM#21@172.16.1.8:5432/TodoApp__Database'
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocals =sessionmaker(autocommit = False, autoflush= False,bind = engine)
Base = db()







# import psycopg2

# conn = psycopg2.connect(
#     dbname="ToDoApp",
#     user="devteam",
#     password="D3vteaM#21",
#     host="172.16.1.8",
#     port="5432"
# )

# print('connected')