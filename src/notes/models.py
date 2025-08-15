from core.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship


class ShortNotes(Base):
    __tablename__ = 'short_notes'

    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)
    text: str = Column(Text, nullable=False)

    category = relationship('Categories', back_populates='short_notes')
    category_id: int = Column(Integer, ForeignKey('categories.id'), nullable=True)

    def __str__(self):
        return self.title


class Categories(Base):
    __tablename__ = 'categories'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String, nullable=False)

    short_notes = relationship('ShortNotes', back_populates='category', cascade='all, delete-orphan')

    def __str__(self):
        return self.title
