from typing import List
import json
import re

from app.schemas.rule import ComplianceRule
from app.services.llm import call_llm


SYSTEM_PROMPT = """
You are a senior banking compliance expert.

Your task is to extract enforceable compliance rules from policy text.

RULES:
- Return ONLY valid JSON
- Do NOT include explanations
- Do NOT include markdown
- Output must be a JSON array

Each rule must follow this schema:
{
  "rule_id": "string",
  "description": "string",
  "threshold_amount": number or null,
  "requires_kyc": true/false/null,
  "severity": "LOW" | "MEDIUM" | "HIGH"
}
"""


def _extract_json_array(text: str) -> str:
    """
    Safely extract a JSON array from LLM output.
    This is critical for open-source models.
    """
    match = re.search(r"\[\s*{.*?}\s*\]", text, re.DOTALL)
    if not match:
        raise ValueError(
            f"PolicyAgent: Failed to extract JSON array from LLM output:\n{text}"
        )
    return match.group()


def extract_rules(policy_chunks: List[str]) -> List[ComplianceRule]:
    """
    Convert policy document text into structured ComplianceRule objects.
    """

    # Limit context for reliability (POC-safe)
    context = "\n".join(policy_chunks[:3])

    prompt = f"""
{SYSTEM_PROMPT}

POLICY TEXT:
{context}
"""

    response = call_llm(prompt)

    json_str = _extract_json_array(response)
    rules_data = json.loads(json_str)

    rules: List[ComplianceRule] = []
    for rule in rules_data:
        rules.append(ComplianceRule(**rule))

    return rules
