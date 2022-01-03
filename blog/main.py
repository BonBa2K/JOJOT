from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, userdata, devicedata, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
#app.include_router(blog.router)
app.include_router(userdata.router)
app.include_router(devicedata.router)
#app.include_router(user.router)