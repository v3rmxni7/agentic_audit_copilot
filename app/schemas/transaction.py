from pydantic import BaseModel
from typing import Optional


class Transaction(BaseModel):
    transaction_id: str
    amount: float
    has_kyc: bool

    # Optional metadata (not required for audit logic)
    account_id: Optional[str] = None
    currency: Optional[str] = None
    timestamp: Optional[str] = None
