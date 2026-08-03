from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class EntryCreate(BaseModel):
    type: str
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    description: str = Field(..., min_length=1, max_length=500)
    category: Optional[str] = Field("General", max_length=100)
    date: date
    notes: Optional[str] = Field("", max_length=1000)

class EntryUpdate(BaseModel):
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    description: str = Field(..., min_length=1, max_length=500)
    category: Optional[str] = Field("General", max_length=100)
    date: date
    notes: Optional[str] = Field("", max_length=1000)

