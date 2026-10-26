from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="API de test - Projet Sécurité",
    description="API minimaliste pour tester l'architecture de sécurité",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "API en ligne",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello depuis l'API de test !",
        "status": "success"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
