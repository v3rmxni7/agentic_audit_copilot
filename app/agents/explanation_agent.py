from typing import Dict
from app.services.llm import call_llm


SYSTEM_PROMPT = """
You are a senior financial auditor.

Explain the compliance violation clearly and concisely.
Do NOT mention AI or models.
Use professional audit language.
"""


class ExplanationAgent:
    def explain(self, scored_violation: Dict) -> Dict:
        prompt = f"""
{SYSTEM_PROMPT}

Violation details:
- Transaction ID: {scored_violation["transaction_id"]}
- Rule ID: {scored_violation["rule_id"]}
- Risk Level: {scored_violation["risk_level"]}
- Reason: {scored_violation["reason"]}

Return a single-paragraph explanation.
"""

        explanation = call_llm(prompt)

        scored_violation["explanation"] = explanation.strip()
        return scored_violation
