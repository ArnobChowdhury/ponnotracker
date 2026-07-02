import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.database import get_db
from app.models import Placeholder

app = FastAPI(title="Gudam")

# Configure CORS
# In development, should be limited to only specific frontend domain.
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
        "message": "Welcome to Gudam API",
        "database_configured": bool(os.getenv("DATABASE_URL")),
        "redis_configured": bool(os.getenv("REDIS_URL"))
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

class PlaceholderCreate(BaseModel):
    name: str

@app.post("/placeholders/")
async def create_placeholder(data: PlaceholderCreate, db: AsyncSession = Depends(get_db)):
    placeholder = Placeholder(name=data.name)
    db.add(placeholder)
    await db.commit()
    await db.refresh(placeholder)
    return {"id": placeholder.id, "name": placeholder.name}

@app.get("/placeholders/")
async def list_placeholders(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Placeholder))
    placeholders = result.scalars().all()
    return [{"id": p.id, "name": p.name} for p in placeholders]
