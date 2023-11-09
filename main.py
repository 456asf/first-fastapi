from fastapi import (
    FastAPI,Path,status
)

app = FastAPI()

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
def get_books():
    return books 