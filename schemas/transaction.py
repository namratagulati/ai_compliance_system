from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    transaction_id: str

    sender: str
    receiver: str

    amount: float
    country: str

    
    device_id: str | None = None
    ip_address: str | None = None
    bank_account: str | None = None
