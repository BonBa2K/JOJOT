from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Userdata).all()
    return datas

def create(request: schemas.Userdata, db: Session):
    new_data = models.Userdata(status = request.status, account = request.account, user_name = request.user_name, region = request.region,
        time_zone = request.time_zone, music_account = request.music_account, device_count = request.device_count)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def destory(id: int, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.id == id)
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with id {id} not found")
    userdata.delete(synchronize_session=False)
    db.commit()
    return 'done'

def updateAccount(request: schemas.UpdateAccount, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.account == str(request.old_account))
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with account {request.old_account} not found")

    userdata.update({'account':request.new_account})
    db.commit()
    return 'verificated'

def updateRegionTimezone(request: schemas.UpdateRegionTimezone, db: Session):
    userdata = db.query(models.Userdata).filter(models.Userdata.account == str(request.account))
    if not userdata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Userdata with account {request.account} not found")

    userdata.update(request.dict())
    db.commit()
    return 'updated'
"""
def show(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail=f"ID {id} is not available")
    return blog
"""