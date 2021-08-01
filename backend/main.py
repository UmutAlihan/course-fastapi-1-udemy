from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base, Job, User
from apis.version1.route_users import api_router


def include_router(app):
    app.include_router(api_router)

def start_application():
    create_tables()
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

def create_tables():
    print("creating tables")
    Base.metadata.create_all(bind=engine)

app = start_application()

@app.get("/")
def hello_api():
    return {"detail": "Hello"}
    