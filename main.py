def display_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
