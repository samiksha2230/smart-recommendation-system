from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.user import User

router = APIRouter()


# -------------------------
# Request Models
# -------------------------

class SignupRequest(BaseModel):
    username: str
    email: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# -------------------------
# Signup API
# -------------------------

@router.post("/signup")
def signup(data: SignupRequest):

    db: Session = SessionLocal()

    existing_user = db.query(User).filter(
        User.username == data.username
    ).first()

    if existing_user:
        return {
            "message": "Username already exists"
        }

    new_user = User(
        username=data.username,
        email=data.email,
        password=data.password
    )

    db.add(new_user)
    db.commit()

    return {
        "message": "User created successfully"
    }


# -------------------------
# Login API
# -------------------------

@router.post("/login")
def login(data: LoginRequest):

    db: Session = SessionLocal()

    user = db.query(User).filter(
        User.username == data.username,
        User.password == data.password
    ).first()

    if user:

        return {
            "message": "Login successful",
            "username": user.username
        }

    return {
        "message": "Invalid username or password"
    }