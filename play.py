books = [
    {
        "id": 1,
        "name": "Book1"
    },
    
    {
        "id": 2,
        "name": "Book2"
    },

    {
        "id": 3,
        "name": "Book3"
    },
]

book_id = int(input("book id: "))

if book_id in list(book["id"] for book in books):
    print("book found: ", end='')
    for book in books:
        if book["id"] == book_id:
            print(book["name"])

else:
    print("book not found")