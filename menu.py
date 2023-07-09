from books import Book
from users import User
import csv
from transaction import Transaction
import datetime

print("----Welcome to Takeo Library Management System----")

user_choice = int(input("Please select from the following menu:\n"
                         "To borrow a book--Enter 1 \n"
                         "To return a book--Enter 2 \n"
                         "To extend a loan--Enter 3 \n"
                         "To add a user--Enter 4 \n"
                         "To update a user--Enter 5 \n"
                         "To add a book--Enter 6 \n"
                         " Enter Choice: "))

while user_choice != 3:

    if user_choice == 1:

        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        phone_no = input("Enter Your Phone_No: ")
        address = input("Enter Your Address: ")
        print()
        print("-----Enter Book_Id To Choose Book-----")
        print()

        # display available books from books.csv show id and some description
        with open("book_data.csv", "r") as file:
            reader = csv.reader(file)
            print("------------------------")
            print("Available Books:")
            print("------------------------")
            
            for row in reader:
                if len(row) >= 7:
                    print(f"{row[0]}--{row[1]}--{row[2]}--{row[3]}--{row[4]}--{row[5]}--{row[6]}")

        book_id = input("Enter Book Id: ")
        print()
        print("Making Transaction................")

        user = User(name=name, email=email, phone_no=phone_no, address = address)
        user.add_user_to_csv()
        
        transaction_date = datetime.date.today()
        due_date = transaction_date + datetime.timedelta(days=Transaction.Due_Duration)
        transaction = Transaction(user.id, book_id,transaction_date,due_date)
        transaction.make_transaction()

       
        
    elif user_choice == 2:
        email = input("Enter Your Email: ")
        Book.return_book(email)

    elif user_choice == 3:
        pass

    elif user_choice == 4:
        pass

    elif user_choice == 5:
        pass

    elif user_choice == 6:

        book_name = input("Enter Book Name: ")
        title = input("Enter Title: ")
        author = input("Enter author: ")
        quantity = input("Enter quantity: ")
        pub_year = input("Enter Publication Year: ")
        edition = input("Enter Edition: ")

        new_book = Book(book_name=book_name, title=title, author=author, quantity=quantity, pub_year=pub_year, edition=edition)
        new_book.add_book()
    else: 
        print("Invalid Input!!!!")
    
    print("----Welcome to Takeo Library Management System----")
    user_choice = int(input("Please select from the following menu:\n"
                         "To borrow a book--Enter 1 \n"
                         "To return a book--Enter 2 \n"
                         "To extend a loan--Enter 3 \n"
                         "To add a user--Enter 4 \n"
                         "To update a user--Enter 5 \n"
                         "To add a book--Enter 6 \n"
                         " Enter Choice: "))

print("Exiting Program......")
