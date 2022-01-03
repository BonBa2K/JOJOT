from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from ..repository import devicedata

router = APIRouter(
    prefix = "/devicedata",
    tags = ['Devicedatas']
)
get_db = database.get_db

@router.get("/", response_model = List[schemas.ShowDevicedata])
def all(db: Session = Depends(get_db)):
    return devicedata.get_all(db)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Devicedata, db: Session = Depends(get_db)):
    return devicedata.create(request, db)

@router.delete("/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy( device_id, db: Session = Depends(get_db)):
    return devicedata.destory(device_id, db)