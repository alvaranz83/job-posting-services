from fastapi import FastAPI
from app.routers import jobs, candidates, health

app = FastAPI(title="Job Posting Service")

# Routers
app.include_router(jobs.router, prefix="/jobs", tags=["Jobs"])
app.include_router(candidates.router, prefix="/candidates", tags=["Candidates"])
app.include_router(health.router, prefix="/health", tags=["Health"])

