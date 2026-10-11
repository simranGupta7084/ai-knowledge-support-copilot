from fastapi import FastAPI

app = FastAPI(title="AI Knowledge & Support Copilot")

@app.get("/health")
def health():
    return {"status": "ok"}
