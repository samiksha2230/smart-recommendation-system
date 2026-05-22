from fastapi import APIRouter
from sqlalchemy.orm import Session

from backend.database import SessionLocal
from backend.models.like import Like
from backend.models.save import Save

router = APIRouter()

@router.post("/like-blog")
def like_blog(username: str, blog_id: int):

    db: Session = SessionLocal()

    like = Like(
        username=username,
        blog_id=blog_id
    )

    db.add(like)
    db.commit()

    return {
        "message": "Blog liked successfully"
    }

@router.post("/save-blog")
def save_blog(username: str, blog_id: int):

    db: Session = SessionLocal()

    saved = Save(
        username=username,
        blog_id=blog_id
    )

    db.add(saved)
    db.commit()

    return {
        "message": "Blog saved successfully"
    }

@router.get("/liked-blogs")
def liked_blogs():

    db: Session = SessionLocal()

    return db.query(Like).all()

@router.get("/saved-blogs")
def saved_blogs():

    db: Session = SessionLocal()

    return db.query(Save).all()