from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class TransactionCreate(BaseModel):
    amount:float = Field(gt=0)
    description: str = Field(min_length=1, max_length=200)
    type: TransactionType

class TransactionResponse(BaseModel):
    id:int
    amount:float
    description:str
    type: TransactionType
    created_at: datetime
