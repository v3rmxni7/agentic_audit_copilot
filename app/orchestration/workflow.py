from app.agents.policy_agent import extract_rules
from app.agents.transaction_agent import TransactionAnalysisAgent
from app.agents.rule_agent import RuleEvaluationAgent
from app.agents.risk_agent import RiskScoringAgent
from app.agents.explanation_agent import ExplanationAgent
from app.agents.report_agent import AuditReportGenerator
from app.ingestion.transaction_loader import load_transactions


def run_audit(policy_text: list, transaction_csv_path: str):
    # 1. Extract rules from policy
    rules = extract_rules(policy_text)

    # 2. Load & analyze transactions
    txns = load_transactions(transaction_csv_path)
    txn_agent = TransactionAnalysisAgent()
    processed_txns = txn_agent.analyze(txns)

    # 3. Evaluate rules
    rule_agent = RuleEvaluationAgent()
    violations = rule_agent.evaluate(processed_txns, rules)

    # 4. Risk scoring + explanation
    risk_agent = RiskScoringAgent()
    explain_agent = ExplanationAgent()

    explained = []
    for v in violations:
        scored = risk_agent.score(v)
        explained.append(explain_agent.explain(scored))

    # 5. Generate report
    report_agent = AuditReportGenerator()
    report = report_agent.generate(
        explained_violations=explained,
        total_transactions=len(processed_txns),
    )

    return report
