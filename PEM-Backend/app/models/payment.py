from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PaymentCreate(BaseModel):
    amount: float = Field(..., gt=0, description="Must be greater than 0")
    date: date
    notes: Optional[str] = Field("", max_length=1000)
