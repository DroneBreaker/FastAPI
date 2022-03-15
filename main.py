from fastapi import FastAPI
import models
from database import engine
from routers import productRouter, userRouter

vogue = FastAPI()

models.Base.metadata.create_all(engine)

vogue.include_router(userRouter.router)
vogue.include_router(productRouter.router)