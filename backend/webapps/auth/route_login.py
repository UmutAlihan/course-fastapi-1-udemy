from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.post("/login")
def login(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})




