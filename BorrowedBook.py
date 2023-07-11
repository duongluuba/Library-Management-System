# lend a book from library ( mượn một cuốn sách từ thư viện )
def borrow_book():
    bid = input("Enter book id to borrow: ")
    with open("books.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("books.txt", "w") as file:
        for line in lines:
            book_data = line.strip().split('\t')
            if book_data[0] == bid: # nếu có sách trong thư viện 
                if book_data[3] == '0': # mượn sách 
                    file.write(f"{book_data[0]}\t{book_data[1]}\t{book_data[2]}\t1\n")
                    found = True
                    print("Book borrowed successfully.") #
                else: # sách đă được mượn
                    print("Book is already borrowed.")
            else: 
                file.write(line)

    if not found:# không có sách trong thư viện 
        print("Book not found.")