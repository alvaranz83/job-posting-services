# job-posting-services
📢 Job Posting Service
A microservice that integrates with external job portals (LinkedIn, ZipRecruiter, InfoJobs, Indeed) to post jobs and sync applicants into CipherScale’s recruiting system.
⚙️ Features
Post Jobs → Publish role descriptions to multiple job portals.
Sync Applicants → Pull applicants from job portals and inject them into the hiring pipeline.
GPT Integration → Natural-language prompts like
“Post a Senior Backend Engineer role to LinkedIn and Indeed.”
Pluggable Integrations → Each portal lives in its own module (integrations/).
Railway Ready → Deployable in one click with FastAPI + Postgres.


#🏗️ Architecture
#job-posting-service/
#│── app/
#│   ├── main.py                # FastAPI entrypoint
#│   ├── config.py              # Env vars & settings
#│   ├── models.py              # Pydantic models
#│   ├── database.py            # DB connection (Postgres on Railway)
#│   ├── routers/               # Route definitions
#│   │   ├── jobs.py            # /jobs/post endpoints
#│   │   ├── candidates.py      # /candidates/sync endpoints
#│   │   └── health.py          # /health endpoint
#│   ├── integrations/          # External job portal APIs
#│   │   ├── linkedin.py
#│   │   ├── indeed.py
#│   │   ├── ziprecruiter.py
#│   │   └── infojobs.py
#│   ├── services/              # Core business logic
#│   │   ├── job_poster.py
#│   │   └── candidate_sync.py
#│   └── utils/                 # Helpers
#│       ├── gpt_agent.py
#│       └── logger.py
#│
#├── tests/                     # Unit tests
#├── requirements.txt
#├── Dockerfile
#├── railway.toml
#└── README.md
#####

🚀 Deployment on Railway
Push this repo to GitHub/GitLab.
In Railway, create a New Project → Deploy from GitHub repo.
Add environment variables in Railway Settings:
LINKEDIN_API_KEY=xxxx
INDEED_API_KEY=xxxx
ZIPRECRUITER_API_KEY=xxxx
INFOJOBS_API_KEY=xxxx
OPENAI_API_KEY=xxxx
DATABASE_URL=postgresql://user:pass@host:5432/db
Railway auto-detects FastAPI via Dockerfile and deploys it.
Expose the service → get a Railway-provided URL.
🛠️ Development Setup
# Clone repo
git clone https://github.com/your-org/job-posting-service.git
cd job-posting-service

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run locally
uvicorn app.main:app --reload
API docs available at → http://localhost:8000/docs
📌 Example Usage
Post a Job
POST /jobs/post
Content-Type: application/json

{
  "roleName": "Senior Backend Engineer",
  "department": "Software Engineering",
  "description": "We are hiring a Senior Backend Engineer to join our growing team...",
  "portals": ["linkedin", "indeed"]
}
Sync Applicants
POST /candidates/sync
Content-Type: application/json

{
  "portal": "linkedin",
  "positionId": "12345"
}
🧪 Running Tests
pytest tests/
📄 License
🔒 Private repository — internal use only.
