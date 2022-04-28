from itertools import count
from unittest import skip
from .. import models, schemas
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from typing import List, Optional
from .. import oauth2, models

router = APIRouter(
    prefix="/arduino",
    tags=['Arduino']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ArduinoData)
def sensor_data(data: schemas.ArduinoData, db: Session = Depends(get_db)):
    new_data = models.Arduino(**data.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data