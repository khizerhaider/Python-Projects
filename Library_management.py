import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def __str__(self):
        return f"Member {self.name} (ID: {self.member_id})"

    def borrow_book(self, book, borrow_period_days=14):
        if book.is_borrowed:
            return f"The book '{book.title}' is already borrowed."
        else:
            self.borrowed_books.append(book)
            book.is_borrowed = True
            book.due_date = datetime.now() + timedelta(days=borrow_period_days)
            return f"The book '{book.title}' has been borrowed by {self.name}. Due date: {book.due_date.strftime('%Y-%m-%d')}"

    def return_book(self, book, fine_per_day=1):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False
            now = datetime.now()
            fine = 0
            if now > book.due_date:
                late_days = (now - book.due_date).days
                fine = late_days * fine_per_day
            book.due_date = None
            return f"The book '{book.title}' has been returned by {self.name}. Fine: ${fine}"
        else:
            return f"The book '{book.title}' was not borrowed by {self.name}."

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.add_default_books()

    def add_book(self, book):
        self.books.append(book)
        return f"The book '{book.title}' has been added to the library."

    def add_member(self, member):
        self.members.append(member)
        return f"Member {member.name} has been added to the library."

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        return [str(book) for book in self.books]

    def list_available_books(self):
        return [str(book) for book in self.books if not book.is_borrowed]

    def list_borrowed_books(self):
        return [str(book) for book in self.books if book.is_borrowed]

    def list_members(self):
        return [str(member) for member in self.members]

    def add_default_books(self):
        default_books = [
            ("1984", "George Orwell", "1111"),
            ("Pride and Prejudice", "Jane Austen", "2222"),
            ("To Kill a Mockingbird", "Harper Lee", "3333"),
            ("The Great Gatsby", "F. Scott Fitzgerald", "4444"),
            ("Moby Dick", "Herman Melville", "5555"),
            ("War and Peace", "Leo Tolstoy", "6666"),
            ("The Catcher in the Rye", "J.D. Salinger", "7777"),
            ("The Hobbit", "J.R.R. Tolkien", "8888"),
            ("Brave New World", "Aldous Huxley", "9999"),
            ("The Odyssey", "Homer", "1010"),
        ]
        for title, author, isbn in default_books:
            self.add_book(Book(title, author, isbn))

library = Library()

def add_book():
    title = entry_title.get()
    author = entry_author.get()
    isbn = entry_isbn.get()
    book = Book(title, author, isbn)
    messagebox.showinfo("Add Book", library.add_book(book))

def add_member():
    name = entry_name.get()
    member_id = entry_member_id.get()
    member = Member(name, member_id)
    messagebox.showinfo("Add Member", library.add_member(member))

def borrow_book():
    member_id = entry_member_id.get()
    isbn = entry_isbn.get()
    member = next((m for m in library.members if m.member_id == member_id), None)
    book = library.find_book_by_isbn(isbn)
    if member and book:
        messagebox.showinfo("Borrow Book", member.borrow_book(book))
    else:
        messagebox.showerror("Error", "Member or Book not found")

def return_book():
    member_id = entry_member_id.get()
    isbn = entry_isbn.get()
    member = next((m for m in library.members if m.member_id == member_id), None)
    book = library.find_book_by_isbn(isbn)
    if member and book:
        messagebox.showinfo("Return Book", member.return_book(book))
    else:
        messagebox.showerror("Error", "Member or Book not found")

def list_books():
    books = library.list_books()
    messagebox.showinfo("All Books", "\n".join(books))

def list_available_books():
    books = library.list_available_books()
    messagebox.showinfo("Available Books", "\n".join(books))

def list_borrowed_books():
    books = library.list_borrowed_books()
    messagebox.showinfo("Borrowed Books", "\n".join(books))

app = tk.Tk()
app.title("Library Management System")

tk.Label(app, text="Title").grid(row=0)
tk.Label(app, text="Author").grid(row=1)
tk.Label(app, text="ISBN").grid(row=2)
entry_title = tk.Entry(app)
entry_author = tk.Entry(app)
entry_isbn = tk.Entry(app)
entry_title.grid(row=0, column=1)
entry_author.grid(row=1, column=1)
entry_isbn.grid(row=2, column=1)

tk.Button(app, text="Add Book", command=add_book).grid(row=3, column=0)
tk.Button(app, text="List All Books", command=list_books).grid(row=3, column=1)
tk.Button(app, text="List Available Books", command=list_available_books).grid(row=3, column=2)
tk.Button(app, text="List Borrowed Books", command=list_borrowed_books).grid(row=3, column=3)

tk.Label(app, text="Name").grid(row=4)
tk.Label(app, text="Member ID").grid(row=5)
entry_name = tk.Entry(app)
entry_member_id = tk.Entry(app)
entry_name.grid(row=4, column=1)
entry_member_id.grid(row=5, column=1)

tk.Button(app, text="Add Member", command=add_member).grid(row=6, column=0)

tk.Label(app, text="Member ID").grid(row=7)
tk.Label(app, text="ISBN").grid(row=8)
entry_member_id = tk.Entry(app)
entry_isbn = tk.Entry(app)
entry_member_id.grid(row=7, column=1)
entry_isbn.grid(row=8, column=1)

tk.Button(app, text="Borrow Book", command=borrow_book).grid(row=9, column=0)
tk.Button(app, text="Return Book", command=return_book).grid(row=9, column=1)

app.mainloop()
