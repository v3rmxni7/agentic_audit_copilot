from fastapi import APIRouter, UploadFile, File, Form
import tempfile
from app.orchestration.workflow import run_audit

router = APIRouter()

@router.post("/run-audit")
async def run_audit_endpoint(
    policy_text: str = Form(...),
    transactions_file: UploadFile = File(...)
):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        content = await transactions_file.read()
        tmp.write(content)
        csv_path = tmp.name

    policy_lines = [l.strip() for l in policy_text.split("\n") if l.strip()]

    report = run_audit(
        policy_text=policy_lines,
        transaction_csv_path=csv_path
    )

    return report
