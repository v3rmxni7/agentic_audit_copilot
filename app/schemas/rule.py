from pydantic import BaseModel
from typing import Optional

class ComplianceRule(BaseModel):
    rule_id: str
    description: str
    threshold_amount: Optional[float] = None
    requires_kyc: Optional[bool] = None
    severity: str  # LOW, MEDIUM, HIGH
