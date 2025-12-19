from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from storage import load_notes, add_page, update_page, delete_page
from models import create_page

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/pages")
def get_pages():
    return load_notes()

@app.post("/pages")
def create(title: str):
    page = create_page(title)
    add_page(page)
    return page

@app.put("/pages/{page_id}")
def rename_or_edit(page_id: str, title: str | None = None, content: str | None = None):
    data = {}
    if title is not None:
        data["title"] = title
    if content is not None:
        data["content"] = content

    update_page(page_id, data)
    return {"status": "updated"}

@app.delete("/pages/{page_id}")
def delete(page_id: str):
    delete_page(page_id)
    return {"status": "deleted"}