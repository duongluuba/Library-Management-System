class Book:
    def __init__(self, bid, title, author, status):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status

def add_book():
    bid = str(input("Enter book id: "))
    title = str(input("Enter book title: "))
    author = str(input("Enter book author: "))
    status = '0'  # 0 for available

    new_book = Book(bid, title, author, status)

    with open("books.txt", "a") as file:
        file.write(f"{new_book.bid}\t{new_book.title}\t{new_book.author}\t{new_book.status}\n")

    print("Book added successfully.")
