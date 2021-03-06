from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base, Job, User
from apis.base import api_router
from webapps.base import api_router as webapp_router
from fastapi.staticfiles import StaticFiles


def create_tables():
    print("creating tables")
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    create_tables()
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static(app)
    return app


app = start_application()
