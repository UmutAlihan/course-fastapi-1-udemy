from fastapi import Depends
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi import responses, status
from fastapi.security.utils import get_authorization_scheme_param
from typing import Optional

from db.repository.jobs import list_jobs, create_new_job  
from db.session import get_db
from db.repository.jobs import retreive_job, search_job
from db.models.users import User
from apis.version1.route_login import get_current_user_from_token
from schemas.jobs import JobCreate
from webapps.jobs.forms import JobCreateForm



templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
def homepage(request:Request, db:Session = Depends(get_db), msg:str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/homepage.html", {"request":request, "jobs": jobs, "msg": msg})

@router.get("/detail/{id}")
def job_detail(id:int, request:Request, db:Session = Depends(get_db)):
    job = retreive_job(id=id, db=db)
    return templates.TemplateResponse("jobs/detail.html", 
                                     {"request":request, "job":job})

@router.get("/post-a-job/")  
def create_job(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("jobs/create_job.html", {"request": request})

@router.post("/post-a-job/")
async def create_job(request: Request, db: Session = Depends(get_db)):
    # this is cleaner once you implement an UI 
    #async def create_job(request: Request, db: Session = Depends(get_db),
    #       current_user:User = Depends(get_current_user_from_token)):

    # If you don't want to publish a job post instantly and review it before publishing,
    # You can make use of the is_active field on the Job Model. When someone non-admin creates a job post it can be False by default. 
    # And won't show up because in the list view we are querying from database
    form = JobCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            job = JobCreate(**form.__dict__)
            job = create_new_job(job=job, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/detail/{job.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("jobs/create_job.html", form.__dict__)
    return templates.TemplateResponse("jobs/create_job.html", form.__dict__)

@router.get("/delete-job/")
def show_jobs_to_delete(request: Request, db: Session = Depends(get_db)):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse("jobs/show_jobs_to_delete.html", {
        "request": request,
        "jobs": jobs
    })

@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    jobs = search_job(query, db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs}
    )  
