from fastapi import (
    FastAPI,Path,status,
    HTTPException,Body
)
#initialize project
app = FastAPI()
#dummy data
books = [   
    {"title":"book-1","content":"content-1","isbn":"234234-23423-42323"},
    {"title":"book-2","content":"content-2","isbn":"234234-23423-4233"},
    {"title":"book-3","content":"content-3","isbn":"23234-232323-4223"},
    {"title":"book-4","content":"content-4","isbn":"23234-234423-4233"}
]

@app.get("/")
async def root():
    return {"message":"It's worked!"}

@app.get("/books/",status_code=status.HTTP_200_OK)
async def get_books():
    return books 

@app.get("/books/{id}/",status_code=status.HTTP_200_OK)
async def show_books(id: int=Path(...,title="id")):
    return books[id-1]

@app.put("/books/{id}/",status_code=status.HTTP_202_ACCEPTED)
async def update_books(id: int=Path(...,gt=0),body=Body()):
    try:
        book = books[id-1]
    except IndexError:
        raise HTTPException(status_code=404,detail="Can't find...")
    book["title"] = body.get("title") or book.get("title")
    book["content"] = body.get("content") or book.get("content")
    book["isbn"] = body.get("isbn") or book.get("isbn")
    books[id-1] = book 
    return books 
    
@app.delete("/books/{id}/",status_code=status.HTTP_204_NO_CONTENT)
async def delete_books(id: int=Path(...,gt=0)):
    try: 
        book = books[id-1]
    except IndexError:
        raise HTTPException(status_code=404,detail="Can't find...")
    else:
        books.remove(book)
