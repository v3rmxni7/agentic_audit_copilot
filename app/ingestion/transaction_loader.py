import pandas as pd
from app.schemas.transaction import Transaction


def load_transactions(csv_path: str):
    """
    Load transactions from a CSV file and normalize schema.

    Expected logical fields:
    - transaction_id
    - amount
    - has_kyc / kyc_verified
    """

    # Read CSV (handles Excel BOM safely)
    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    # Normalize column names
    df.columns = [
        col.strip()
           .lower()
           .replace('"', '')
           .replace("'", "")
        for col in df.columns
    ]

    # Column aliases supported
    column_aliases = {
        "transaction_id": ["transaction_id", "txn_id", "id", "transactionid"],
        "amount": ["amount", "amt", "transaction_amount"],
        "has_kyc": ["has_kyc", "kyc", "kyc_verified"],
    }

    def resolve_column(possible_names):
        for name in possible_names:
            if name in df.columns:
                return name
        return None

    tx_id_col = resolve_column(column_aliases["transaction_id"])
    amt_col = resolve_column(column_aliases["amount"])
    kyc_col = resolve_column(column_aliases["has_kyc"])

    missing = []
    if not tx_id_col:
        missing.append("transaction_id")
    if not amt_col:
        missing.append("amount")
    if not kyc_col:
        missing.append("has_kyc / kyc_verified")

    if missing:
        raise ValueError(
            f"CSV missing required columns: {missing}. "
            f"Found columns: {list(df.columns)}"
        )

    transactions = []
    for _, row in df.iterrows():
        transactions.append(
            Transaction(
                transaction_id=str(row[tx_id_col]),
                amount=float(row[amt_col]),
                has_kyc=str(row[kyc_col]).strip().lower() in ["true", "1", "yes"]
            )
        )

    return transactions
