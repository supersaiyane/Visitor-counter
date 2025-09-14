from sqlalchemy import Column, Integer, String
from app.database import Base

class VisitorCount(Base):
    __tablename__ = "visitor_counts"

    repo = Column(String, primary_key=True, index=True)
    count = Column(Integer, default=0)