from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.api.audit import router as audit_router

app = FastAPI(
    title="Agentic Audit Copilot",
    description="Enterprise Agentic AI for Audit & Compliance",
    version="1.0.0",
)

# -------------------------
# API ROUTES
# -------------------------
app.include_router(audit_router, prefix="/api")


# -------------------------
# STATIC UI
# -------------------------
app.mount(
    "/static",
    StaticFiles(directory="app/ui"),
    name="static"
)


@app.get("/", include_in_schema=False)
def serve_ui():
    """
    Serve the main UI page
    """
    return FileResponse("app/ui/index.html")


# -------------------------
# HEALTH CHECK
# -------------------------
@app.get("/health", include_in_schema=False)
def health_check():
    return {"status": "ok"}
