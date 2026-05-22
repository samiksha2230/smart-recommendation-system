from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models.blog import Blog

router = APIRouter()

@router.post("/create-blog")
def create_blog(title: str, content: str, category: str):

    db: Session = SessionLocal()

    new_blog = Blog(
        title=title,
        content=content,
        category=category
    )

    db.add(new_blog)
    db.commit()

    return {
        "message": "Blog created successfully"
    }

@router.get("/blogs")
def get_blogs():

    db: Session = SessionLocal()

    blogs = db.query(Blog).all()

    return blogs
@router.get("/search/{query}")
def search_blogs(query: str):

    db: Session = SessionLocal()

    blogs = db.query(Blog).filter(
        Blog.title.contains(query)
    ).all()

    return blogs