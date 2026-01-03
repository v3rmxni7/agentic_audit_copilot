from typing import List, Dict
from app.schemas.transaction import Transaction
from app.schemas.rule import ComplianceRule


class RuleEvaluationAgent:
    """
    Evaluates transactions against compliance rules.
    """

    def evaluate(
        self,
        transactions: List[Transaction],
        rules: List[ComplianceRule],
    ) -> List[Dict]:
        violations = []

        for txn in transactions:
            for rule in rules:
                violated, reason = self._check_rule(txn, rule)
                if violated:
                    violations.append(
                        {
                            "transaction_id": txn.transaction_id,
                            "rule_id": rule.rule_id,
                            "severity": rule.severity,
                            "reason": reason,
                        }
                    )

        return violations

    def _check_rule(self, txn, rule):
    # Amount-based rule
        if rule.threshold_amount is not None:
            if txn.amount > rule.threshold_amount:
                if rule.requires_kyc is True and not txn.has_kyc:
                    return True, (
                        f"Transaction amount {txn.amount} exceeds "
                        f"{rule.threshold_amount} without KYC verification."
                    )

        return False, None

