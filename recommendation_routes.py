from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.services.recommendation import get_user_recommendations

router = APIRouter()

@router.get("/recommend/{username}")
def recommend(username: str):

    db: Session = SessionLocal()

    recommendations = get_user_recommendations(username, db)

    return recommendations