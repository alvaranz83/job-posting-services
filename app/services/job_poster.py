from app.integrations import linkedin, indeed, ziprecruiter, infojobs
from app.models import JobPostRequest

async def post_job_to_portals(body: JobPostRequest):
    results = {}
    for portal in body.portals:
        if portal == "linkedin":
            results["linkedin"] = await linkedin.post_job(body)
        elif portal == "indeed":
            results["indeed"] = await indeed.post_job(body)
        elif portal == "ziprecruiter":
            results["ziprecruiter"] = await ziprecruiter.post_job(body)
        elif portal == "infojobs":
            results["infojobs"] = await infojobs.post_job(body)
        else:
            results[portal] = {"error": "Portal not supported"}
    return {"message": "Job posting complete", "results": results}

