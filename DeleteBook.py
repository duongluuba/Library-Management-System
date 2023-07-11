# Delete a book from the library (Xóa sách khỏi thư viện)
def delete_book(): 
    bid = input("Enter book id to delete: ")
    with open("books.txt", "r") as file:
        lines = file.readlines()
        
    found = False
    with open("books.txt", "w") as file:
        for line in lines:
            book_data = line.strip().split('\t')
            if book_data[0] != bid:
                file.write(line)
            else:
                found = True

    if found:
        print("Book deleted successfully.")
    else:
        print("Book not found.")
