from fastapi import FastAPI

app = FastAPI()

# Sample book data
BOOKS = [
    {
        'title': 'Title One',
        'author': 'Author One',
        'category': 'Science'
    },
    {
        'title': 'Title Two',
        'author': 'Author Two',
        'category': 'Science'        
    },
    {
        'title': 'Title Three',
        'author': 'Author Three',
        'category': 'History'        
    },
    {
        'title': 'Title Four',
        'author': 'Author Four',
        'category': 'Math'
    },
    {
        'title': 'Title Five',
        'author': 'Author Five',
        'category': 'Math'        
    },
    {
        'title': 'Title Six',
        'author': 'Author Two',
        'category': 'Math'        
    }
]


# Endpoint to get all books
@app.get('/books')
async def read_all_books():
    """
    Returns the list of all books.
    """
    return BOOKS


# Endpoint to get a favorite book
@app.get("/books/mybook")
async def read_my_book():
    """
    Returns a predefined favorite book.
    """
    return {'book_title': 'My favorite book!'}


# Endpoint to get a book by its title
@app.get('/books/title/{book_title}')
async def read_book_by_title(book_title: str):
    """
    Returns a book that matches the given title.
    
    Args:
        book_title: The title of the book to search for.
    
    Returns:
        The book that matches the title, or None if no match is found.
    """
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return None


# Endpoint to get books by optional category or author query parameters
@app.get('/books/')
async def read_books(category: str, author: str):
    """
    Returns books filtered by category or author.
    
    Args:
        category: The category to filter books by (optional).
        author: The author to filter books by (optional).
    
    Returns:
        A list of books that match the given category or author.
    """
    books_to_return = []
    for book in BOOKS:
        if category and book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
        elif author and book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


# Endpoint to get books by their category
@app.get('/books/category/{category}')
async def read_books_by_category(category: str):
    """
    Returns books that match the given category.
    
    Args:
        category: The category to filter books by.
    
    Returns:
        A list of books that match the given category.
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


# Endpoint to get books by their author
@app.get('/books/author/{author}')
async def read_books_by_author(author: str):
    """
    Returns books that match the given author.
    
    Args:
        author: The author to filter books by.
    
    Returns:
        A list of books that match the given author.
    """
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return