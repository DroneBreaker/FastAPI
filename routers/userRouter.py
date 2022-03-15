from fastapi import APIRouter, Depends, HTTPException
from flask import request
from database import get_db
import models, schemas
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Users"]
)


@router.get("/users")
def users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post("/users")
def create_users(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return user


@router.put("/users/{id}")
def update_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return HTTPException(detail='The user has been updated successfully', status_code=200)


@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)

    if not user.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return HTTPException(detail='The user has been deleted successfully', status_code=200)
