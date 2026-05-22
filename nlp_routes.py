from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal

from backend.services.nlp_recommendation import recommend_similar_blogs

router = APIRouter()

@router.get("/similar-blogs/{blog_id}")
def similar_blogs(blog_id: int):

    db: Session = SessionLocal()

    recommendations = recommend_similar_blogs(
        blog_id,
        db
    )

    return recommendations