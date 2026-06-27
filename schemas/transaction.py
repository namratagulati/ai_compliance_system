from pydantic import BaseModel

class Transaction(BaseModel):
    transaction_id: str

    sender: str
    receiver: str

    amount: float
    country: str

    device_id: str
    ip_address: str
    bank_account: str