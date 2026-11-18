from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "Kindred", "author": "Octavia E. Butler"},
]


@app.get("/books")
def list_books():
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    pass
