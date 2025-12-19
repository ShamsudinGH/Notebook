from pydantic import BaseModel
from uuid import uuid4


class NotePage(BaseModel):
    id: str
    title: str
    content: str = ""

def create_page(title: str) -> NotePage:
    return NotePage(id=str(uuid4()), title=title)