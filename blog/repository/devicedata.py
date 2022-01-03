from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    datas = db.query(models.Devicedata).all()
    return datas

def create(request: schemas.Devicedata, db: Session):
    new_data = models.Devicedata(device_id = request.device_id, account = request.account, device_name = request.device_name,
        language = request.language, system_volume = request.system_volume, media_volume = request.media_volume, user_account = request.user_account )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def destory( device_id: str, db: Session):
    devicedata = db.query(models.Devicedata).filter(models.Devicedata.device_id == device_id)
    if not devicedata.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with device_id {device_id} not found")
    devicedata.delete(synchronize_session=False)
    db.commit()
    return 'done'