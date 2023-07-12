import csv
import time
from users import User
from transaction import Transaction

class Book():
    counter = 0

    def __init__(self, book_name, title, author, quantity, pub_year, edition):
        Book.counter += 1
        self.book_id = Book.counter 
        self.book_name = book_name
        self.title = title
        self.author = author
        self.quantity = quantity
        self.pub_year = pub_year
        self.edition = edition

 
    def add_book(self):
        book_data = f"{self.book_id},{self.book_name},{self.title},{self.author},{self.quantity},{self.edition},{self.pub_year}\n"
        found = self.search_book_by_title(self.title)

        if not found:
            with open("book_data.csv", "a") as file:
                file.write(book_data)
                print("---------------")
                print("Book added successfully!")
                print("---------------")

        else: 
            print("Book already exists!!!")


    def search_book_by_title(self, title):
        found = False
        with open("book_data.csv", "r") as file:
            for line in file:
                book_info = line.strip().split(",") #['book', 2012]
                print(book_info)

                if book_info[2] == title:
                    found = True
                    return found
                
            if not found:
                return found
            

    def return_book(email):
        user = User.find_user_by_email(email)

        if user:
            Transaction.update_return_book(user[0])
            print("Book returned successfully")
        else:
            print("Incorrect email !!!!")

    
    def show_books():
        with open("book_data.csv", "r") as file:
            reader = csv.reader(file)
            print("----------------------------------------------------------------------------")
            print("                            Available Books                                 ")
            print("----------------------------------------------------------------------------")        
            for row in reader:
                if len(row) >= 7:
                    print(f"{row[0]}--{row[1]}--{row[2]}--{row[3]}--{row[4]}--{row[5]}--{row[6]}")

    
    def get_books_from_ids(book_ids):
        found_books = []
        with open('book_data.csv', 'r') as file:
            for line in file:
                book = line.strip().split(',')
                if book[0].lower() in book_ids:
                    found_books.append(book)
        
        return found_books