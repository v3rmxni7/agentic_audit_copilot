from pydantic import BaseModel
from typing import List

class AuditFinding(BaseModel):
    transaction_id: str
    rule_id: str
    risk_level: str
    explanation: str

class AuditReport(BaseModel):
    total_transactions: int
    total_flagged: int
    findings: List[AuditFinding]
    summary: str
