from pydantic import BaseModel
from typing import List, Optional

class JobPostRequest(BaseModel):
    roleName: str
    department: str
    description: str
    portals: List[str]
    userEmail: Optional[str] = None
    dryRun: bool = False

class ApplicantSyncRequest(BaseModel):
    portal: str
    positionId: Optional[str] = None
    roleQuery: Optional[str] = None
    userEmail: Optional[str] = None
    dryRun: bool = False

