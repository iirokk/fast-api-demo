from sqlalchemy import Column, Integer, String
from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
