from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/")
def homepage(request:Request):
    dir(request)
    return templates.TemplateResponse("jobs/homepage.html", {"request":request})