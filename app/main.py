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
from .routers import post,user,auth



app = FastAPI()
models.Base.metadata.create_all(bind=engine)


while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='7015477816ms',
            cursor_factory=RealDictCursor
        )

        cursor = conn.cursor()
        print("Database successfully connected")
        break

    except Exception as error:
        print("Connection failed")
        time.sleep(2)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)