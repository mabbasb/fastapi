from .. import models, schemas
from fastapi import status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from typing import List, Optional

router = APIRouter(prefix="/waterstatus",
    tags=['WasteWaterMonitoring'])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.WaterStatus)
def sensor_data(data: schemas.WaterStatus, db: Session = Depends(get_db)):
    new_data = models.Water_Status(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.get("/getposts", response_model=List[schemas.WaterStatusOut])
def retrieve_data(db: Session = Depends(get_db)):
    data = db.query(models.Water_Status).all()

    return data