from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, status
from fastapi import APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta

from db.session import get_db
from db.repository.login import get_user
from core.hashing import Hasher
from core.config import settings
from core.security import create_access_token


router = APIRouter()


def authenticate_user(username:str, password:str, db:Session):
    user = get_user(username=username, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user

@router.post("/token")
def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends(),
                            db:Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password")
    access_token_expire = timedelta(minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":user.email}, expires_delta=access_token_expire)
    return {"access_token":access_token, "token_type": "bearer"}
