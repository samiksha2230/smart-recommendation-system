from sqlalchemy import Column, Integer, String
from backend.database import Base

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)

    blog_id = Column(Integer)