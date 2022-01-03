from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import userdata

router = APIRouter(
    prefix = "/userdata",
    tags = ['Userdatas']
)
get_db = database.get_db

@router.get("/", response_model = List[schemas.ShowUserdata])
def all(db: Session = Depends(get_db)):
    return userdata.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Userdata, db: Session = Depends(get_db)):
    return userdata.create(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy( id, db: Session = Depends(get_db)):
    return userdata.destory(id, db)

@router.put("/account/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateAccount( request: schemas.UpdateAccount, db: Session = Depends(get_db)):
    return userdata.updateAccount(request, db)

@router.put("/regiontimezone/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateRegionTimezone( request: schemas.UpdateRegionTimezone, db: Session = Depends(get_db)):
    return userdata.updateRegionTimezone(request, db)
"""
@router.get("/{id}", status_code=200, response_model = schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
"""