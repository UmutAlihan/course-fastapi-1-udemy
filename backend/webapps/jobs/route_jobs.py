from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.jobs import list_jobs
from sqlalchemy.orm import Session
from db.session import get_db
from db.repository.jobs import retreive_job
from fastapi import Depends


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