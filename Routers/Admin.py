from fastapi import APIRouter as Router,Depends,HTTPException,Path
# import models
from database import SessionLocals
from typing import Annotated
from sqlalchemy.orm import Session
from models import todos1
from starlette import status
# from pydantic import BaseModel,Field
from .Auth import get_current_user
# from .Todo import *


router = Router(
    prefix= '/admin',
    tags =['admin']
)

async def get_db():
    db=SessionLocals()
    try: 
        yield db
    finally: 
        db.close()


db_dependency = Annotated[Session,Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]





@router.get("/todo", status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    # if user is None or user.get('user_role') != 'admin':
    #     raise HTTPException(status_code=401, detail='Authentication Failed')
    # return db.query(Todos).all()
    return {'username':user.get('username'),
    'user_id': user.get('id'),
    'user_role': user.get('user_role')
    
    }










