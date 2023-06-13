from typing import List
from .. import models,schemas,auth2
from sqlalchemy.orm import Session
from fastapi import FastAPI,Response,status,HTTPException,Depends,APIRouter
from ..database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.get('/',response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db)):

    # cursor.execute(""" SELECT * FROM posts """)
    # posts = cursor.fetchall()
    # print(posts)

    posts = db.query(models.Post).all()
    return posts


@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(request: schemas.PostCreate,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):
    
    # cursor.execute(""" INSERT INTO posts (title,content,published) VALUES (%s,%s,%s) RETURNING * """,(request.title,request.content,request.published))
    # conn.commit()
    # new_post = cursor.fetchone()
    # print(current_user.email)

    new_post = models.Post(**request.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post



@router.get('/posts/{id}',response_model=schemas.Post)
def get_post(id: int,response: Response,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):

    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """,(str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": "Post not found"}  ---> One solution

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    return post


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):

    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """,(str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post = db.query(models.Post).filter(models.Post.id == id)
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The index is not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db: Session = Depends(get_db),current_user:int = Depends(auth2.get_current_user)):

    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The index is not found")
    
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()