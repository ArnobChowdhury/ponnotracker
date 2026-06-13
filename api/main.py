import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Ponno Tracker API")

# Configure CORS
# In development, we allow all origins. In production, you should limit this
# to your specific frontend domain.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Ponno Tracker API",
        "database_configured": bool(os.getenv("DATABASE_URL")),
        "redis_configured": bool(os.getenv("REDIS_URL"))
    }

@app.get("/health")
def health_check():
    """
    This endpoint is used by the Docker healthcheck defined in 
    docker-compose.prod.yml to ensure the service is running.
    """
    return {"status": "healthy"}