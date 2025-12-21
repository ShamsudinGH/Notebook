import json
from models import NotePage  # твоя модель страницы

FILE = "data/notes.json"

# Загрузка всех страниц
def load_notes() -> dict:
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Сохранение всех страниц
def save_notes(notes: dict):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2, ensure_ascii=False)

# Добавление новой страницы
def add_page(page: NotePage):
    notes = load_notes()
    notes[page.id] = page.dict()
    save_notes(notes)
    return notes[page.id]  # возвращаем созданную страницу

# Обновление страницы (возвращает актуальную страницу)
def update_page(page_id: str, data: dict):
    notes = load_notes()
    if page_id not in notes:
        return None

    notes[page_id].update(data)
    save_notes(notes)
    return notes[page_id]  # возвращаем обновлённую страницу

# Удаление страницы
def delete_page(page_id: str):
    notes = load_notes()
    if page_id in notes:
        del notes[page_id]
        save_notes(notes)
