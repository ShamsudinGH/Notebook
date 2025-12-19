import json
from models import NotePage

FILE = "data/notes.json"

def load_notes() -> dict:
    try:
        with open(FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_notes(notes: dict):
    with open(FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_page(page: NotePage):
    notes = load_notes()
    notes[page.id] = page.dict()
    save_notes(notes)

def update_page(page_id: str, data: dict):
    notes = load_notes()
    notes[page_id].update(data)
    save_notes(notes)

def delete_page(page_id: str):
    notes = load_notes()
    if page_id in notes:
        del notes[page_id]
        save_notes(notes)