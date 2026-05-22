from sqlalchemy import Column, Integer, String
from backend.database import Base

class Save(Base):
    __tablename__ = "saved_blogs"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)

    blog_id = Column(Integer)
