from sqlalchemy import Column, Integer, String
from backend.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)

    blog_id = Column(Integer)

    category = Column(String)

    time_spent = Column(Integer)