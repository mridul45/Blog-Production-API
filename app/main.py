from typing import Optional
from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from .database import *
from sqlalchemy.orm import Session
from typing import List
from .routers import post,user,auth,vote
from .config import settings


app = FastAPI()
models.Base.metadata.create_all(bind=engine)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)