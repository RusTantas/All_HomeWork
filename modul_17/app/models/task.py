from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.models import *
from app.models.user import User


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates="tasks")
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
