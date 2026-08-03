from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class UdharCreate(BaseModel):
    type: str
    person_name: str = Field(..., min_length=1, max_length=200)
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    description: Optional[str] = Field("", max_length=500)
    date: date
    due_date: Optional[date] = None
    notes: Optional[str] = Field("", max_length=1000)

class UdharUpdate(BaseModel):
    person_name: str = Field(..., min_length=1, max_length=200)
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    description: Optional[str] = Field("", max_length=500)
    date: date
    due_date: Optional[date] = None
    notes: Optional[str] = Field("", max_length=1000)
