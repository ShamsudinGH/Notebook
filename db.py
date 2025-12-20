from password import PASSWORD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



DATABASE_URL = f"postgresql+psycopg://postgres:{PASSWORD}@localhost:5432/notebook"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
