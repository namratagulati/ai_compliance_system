from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    transaction_id: str

    sender: str
    receiver: str

    amount: float
    country: str

    device_id: Optional[str] = None
    ip_address: Optional[str] = None
    bank_account: str
