from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix = "/user",
    tags = ['Users']
)
get_db = database.get_db

@router.post('/', response_model = schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get("/{id}", status_code=200, response_model = schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return user.show(id, db)

"""
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy_user( id, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id {id} not found")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'
"""