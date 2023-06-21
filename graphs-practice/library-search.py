def search(books, key):
    output = []
    for book in books:
        if book.lower().startswith(key.lower()):
            output.append(book)
    if output is None:
        return -1
    else:
        return output






books = ["hello","happylife","Algorithm","DSA","Python","happynewyear"]
key = "h"
output = search(books,key)
print(output)