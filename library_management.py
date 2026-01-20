# Custom exception for wrong book ID
class InvalidBookID(Exception):
    pass

# Custom exception when book is already issued
class BookAlreadyIssued(Exception):
    pass


# This class stores details of one book
class Book:
    def __init__(self, book_id, book_name, author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        self.available = True   # book is available at start


# This class manages all library work
class Library:
    def __init__(self):
        self.books = []   # list to store all books

    # This function adds a new book
    def add_book(self):
        try:
            book_id = int(input("Enter book id: "))
            book_name = input("Enter book name: ")
            author_name = input("Enter author name: ")

            new_book = Book(book_id, book_name, author_name)
            self.books.append(new_book)
            print("Book added successfully")

        except:
            print("Wrong input")

    # This function shows all books
    def show_books(self):
        if len(self.books) == 0:
            print("No books in library")
        else:
            for book in self.books:
                if book.available:
                    status = "Available"
                else:
                    status = "Issued"

                print(book.book_id, book.book_name, book.author_name, status)

    # This function issues a book
    def issue_book(self):
        try:
            book_id = int(input("Enter book id to issue: "))

            for book in self.books:
                if book.book_id == book_id:
                    if book.available == False:
                        raise BookAlreadyIssued
                    book.available = False
                    print("Book issued")
                    return

            raise InvalidBookID

        except BookAlreadyIssued:
            print("Book is already issued")
        except InvalidBookID:
            print("Book id not found")
        except:
            print("Wrong input")

    # This function returns a book
    def return_book(self):
        try:
            book_id = int(input("Enter book id to return: "))

            for book in self.books:
                if book.book_id == book_id:
                    book.available = True
                    print("Book returned")
                    return

            raise InvalidBookID

        except InvalidBookID:
            print("Book id not found")
        except:
            print("Wrong input")


# Main menu
library = Library()

while True:
    print()
    print("1 Add Book")
    print("2 Show All Books")
    print("3 Issue Book")
    print("4 Return Book")
    print("5 Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.show_books()
        elif choice == 3:
            library.issue_book()
        elif choice == 4:
            library.return_book()
        elif choice == 5:
            print("Program closed")
            break
        else:
            print("Wrong choice")

    except:
        print("Please enter number only")
