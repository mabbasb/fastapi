from .. import models, schemas
from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter(prefix="/arduino",
    tags=['Arduino'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ArduinoData)
def sensor_data(data: schemas.ArduinoData, db: Session = Depends(get_db)):
    new_data = models.Arduino(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data