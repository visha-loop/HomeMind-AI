from fastapi import FastAPI

app = FastAPI(title="HomeMind-AI")

@app.get("/")
def root():
    return {
        "status": "running",
        "project": "HomeMind-AI"
    }
