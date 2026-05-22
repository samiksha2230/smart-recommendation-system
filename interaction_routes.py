from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.interaction import Interaction

router = APIRouter()

@router.post("/track-interaction")
def track_interaction(
    username: str,
    blog_id: int,
    category: str,
    time_spent: int
):

    db: Session = SessionLocal()

    interaction = Interaction(
        username=username,
        blog_id=blog_id,
        category=category,
        time_spent=time_spent
    )

    db.add(interaction)
    db.commit()

    return {
        "message": "Interaction tracked successfully"
    }

@router.get("/interactions")
def get_interactions():

    db: Session = SessionLocal()

    interactions = db.query(Interaction).all()

    return interactions
@router.get("/interactions")
def get_interactions():

    db: Session = SessionLocal()

    return db.query(Interaction).all()