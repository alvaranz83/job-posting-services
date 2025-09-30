from fastapi import APIRouter, Request
from app.models import JobPostRequest
from app.services.job_poster import post_job_to_portals

router = APIRouter()

@router.post("/post")
async def post_job(request: Request, body: JobPostRequest):
    return await post_job_to_portals(body)

