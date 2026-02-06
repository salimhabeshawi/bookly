from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime, date

class Book(BaseModel):
    uuid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: date
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime

class BookCreateModel(BaseModel):
    title: Optional[str] = Field(None, description="title of the book")
    author: str
    publisher: Optional[str] = None
    published_date: date
    page_count: Optional[int] = None
    language: str
    
class BookUpdateModel(BaseModel):
    title: Optional[str] = Field(None, description="title of the book")
    author: str
    publisher: Optional[str] = None
    page_count: Optional[int] = None
