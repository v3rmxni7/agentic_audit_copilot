from typing import Dict


class RiskScoringAgent:
    """
    Assigns numeric and categorical risk based on rule severity.
    Deterministic by design (auditor-friendly).
    """

    SEVERITY_MAP = {
        "LOW": 0.3,
        "MEDIUM": 0.6,
        "HIGH": 0.9,
    }

    def score(self, violation: Dict) -> Dict:
        severity = violation["severity"]
        risk_score = self.SEVERITY_MAP.get(severity, 0.5)

        return {
            "transaction_id": violation["transaction_id"],
            "rule_id": violation["rule_id"],
            "risk_score": risk_score,
            "risk_level": severity,
            "reason": violation["reason"],
        }
