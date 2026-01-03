from typing import List
from app.schemas.report import AuditFinding, AuditReport


class AuditReportGenerator:
    """
    Generates final audit report from explained violations.
    """

    def generate(
        self,
        explained_violations: List[dict],
        total_transactions: int,
    ) -> AuditReport:

        findings = []
        for v in explained_violations:
            findings.append(
                AuditFinding(
                    transaction_id=v["transaction_id"],
                    rule_id=v["rule_id"],
                    risk_level=v["risk_level"],
                    explanation=v["explanation"],
                )
            )

        summary = (
            f"{len(findings)} compliance violations detected "
            f"out of {total_transactions} transactions."
        )

        return AuditReport(
            total_transactions=total_transactions,
            total_flagged=len(findings),
            findings=findings,
            summary=summary,
        )
