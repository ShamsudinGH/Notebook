from db import engine
from models_db import Note

Note.metadata.create_all(engine)
