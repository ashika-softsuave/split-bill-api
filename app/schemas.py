from pydantic import BaseModel
from typing import List

class BillCreate(BaseModel):
    title: str
    total_amount: int
    participants: List[str]
    paid_by: str
