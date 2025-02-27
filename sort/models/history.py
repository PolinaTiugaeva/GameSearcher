"""History of user's reactions"""
from sqlmodel import SQLModel, Field


class History(SQLModel, table=True):
    """ORM class for history table"""
    id: int = Field(default=None, primary_key=True)
    username: str
    game_title: str
    reaction: int