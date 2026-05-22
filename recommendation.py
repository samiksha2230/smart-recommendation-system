from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.models.interaction import Interaction
from backend.models.blog import Blog


def _fallback_recommendations(db: Session):
    return db.query(Blog).order_by(Blog.id.desc()).all()


def _normalize_category(category: str | None):
    if not category:
        return None

    normalized = category.strip().lower()
    return normalized or None


def get_user_recommendations(username: str, db: Session):

    interactions = db.query(Interaction).filter(
        Interaction.username == username
    ).all()

    if not interactions:
        return _fallback_recommendations(db)

    category_count = {}

    for interaction in interactions:

        category = _normalize_category(interaction.category)

        if category is None:
            continue

        if category not in category_count:
            category_count[category] = 0

        category_count[category] += interaction.time_spent or 0

    if not category_count:
        return _fallback_recommendations(db)

    favorite_category = max(
        category_count,
        key=category_count.get
    )

    recommended_blogs = db.query(Blog).filter(
        func.lower(func.trim(Blog.category)) == favorite_category
    ).all()

    if recommended_blogs:
        return recommended_blogs

    return _fallback_recommendations(db)
