from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from db import Base
import uuid

class Note(Base):
    __tablename__ = "notes"

    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    title: Mapped[str] = mapped_column(String(255))
    content: Mapped[str] = mapped_column(Text, default="")
