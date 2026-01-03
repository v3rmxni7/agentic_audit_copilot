from typing import List
from app.schemas.transaction import Transaction


class TransactionAnalysisAgent:
    """
    Prepares transactions for compliance rule evaluation.
    """

    def analyze(self, transactions: List[Transaction]) -> List[Transaction]:
        # For POC, analysis is identity.
        # In future: pattern detection, aggregation, anomaly signals.
        return transactions
