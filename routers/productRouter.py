from fastapi import APIRouter, Depends, HTTPException
from database import get_db
import models, schemas
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Products"]
)


@router.get("/products")
def products(db: Session = Depends(get_db)):
    products = db.query(models.Products).all()
    return products


@router.post("/products")
def create_products(request: schemas.Products, db: Session = Depends(get_db)):
    new_product = models.Products(name=request.name, price=request.price, description=request.description, img=request.img)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


@router.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.User).filter(models.User.id == id)

    if not product.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return product


@router.put("/products/{id}")
def update_product(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Products).filter(models.Products.id == id)

    if not user.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return HTTPException(detail='The product has been updated successfully', status_code=200)


@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Products).filter(models.Products.id == id)

    if not user.first():
        return HTTPException(detail='The id {id} is not available', status_code=404)
    else:
        return HTTPException(detail='The product has been deleted successfully', status_code=200)
