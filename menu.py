from books import Book
from users import User
from transaction import Transaction
import datetime
import csv

print("----Welcome to Takeo Library Management System----")

user_choice = input("Please select from the following menu:\n"
                         "To borrow a book--Enter 1 \n"
                         "To return a book--Enter 2 \n"
                         "To extend a loan--Enter 3 \n"
                         "To add a user--Enter 4 \n"
                         "To update a user--Enter 5 \n"
                         "To add a book--Enter 6 \n"
                         "Enter 7 to 'exit' \n"
                         " Enter Choice: ")

while user_choice != 7:

    if user_choice == 1:

        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        phone_no = input("Enter Your Phone_No: ")
        address = input("Enter Your Address: ")
        print()
        print("-----Enter Book_Id To Choose Book-----")
        print()

        # display available books from books.csv show id and some description
        Book.show_books()

        book_id = input("Enter Book Id: ")
        print()
        print("Making Transaction................")

        user = User(name=name, email=email, phone_no=phone_no, address = address)
        user.add_to_csv()
        
        transaction_date = datetime.date.today()
        due_date = transaction_date + datetime.timedelta(days=Transaction.Due_Duration)
        transaction = Transaction(user.id, book_id,transaction_date,due_date)
        transaction.make_transaction()

       
        
    elif user_choice == 2:
        email = input("Enter Your Email: ")
        Book.return_book(email)

    elif user_choice == 3:
        print('*** You can extend your book here ***\n')
        user_email = input("Please enter your Email: ")
        user = User.find_user_by_email(user_email)
        
        if user:
            book_ids = Transaction.get_borrowed_book_ids_by_user(user[0])
            found_books = Book.get_books_from_ids(book_ids)
           
            if len(found_books) > 0:
                print('These are the borrowed books found in our database for you:\n')
                print('---------------------------------------------------------------------')
                print('Book_ID | Book_Name | Title | Author | Quantity | Edition | Pub_Year')
                print('---------------------------------------------------------------------\n')
                for book in found_books:
                    print('     |    '.join(book))

                is_extend = True
                while is_extend:
                    extend_book = input("Please enter a book title for book you want to extend: ")
                    for book in found_books:
                        if book[2].lower() == extend_book.lower():
                            try:
                                extension_days = int(input("Please enter the number of days you want to extend the loan: "))
                                Transaction.extend_book_due_date_for_user(book[0], user[0], extension_days)
                                print('-----------------------------------')
                                print("Return date updated successfully!")
                                is_extend = False  # Exit the while loop

                            except ValueError as e:
                                print(e)
                                print("Invalid input. Please enter a valid number of days.")
                            break

                if is_extend:
                    print("No book found with the given title. Please try again.")
            
            else:
                print("You have not borrowed any books yet")



    elif user_choice == 4:
        name = input("Enter name: ")
        email = input("Enter email: ")
        phone_no = input("Enter phone no: ")
        address = input("Enter your address: ")
        user_data = f"{name}-{email}-{phone_no}-{address}\n"
        with open("users.csv", "a") as file:
            file.write(user_data)
        print("User added successfully!")


    elif user_choice == 5:
        email = input("Enter email to update: ")
        updated_data = []
        with open("users.csv", "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if len(user_info) >= 3 and user_info[2] == email:
                    name = input("Enter New name: ")
                    phone_no = input("Enter nee phone_no: ")
                    address = input("Enter new address: ")
                    user = User(name, email, phone_no, address)
                    updated_data.append(user)
                    print("User information updated successfully!")
                else:
                    updated_data.append(user_info)

        with open("users.csv", "w") as file:
            for data in updated_data:
                if isinstance(data, User):
                    user_data = f"{data.id},{data.name},{data.email},{data.phone_no},{data.address}\n"
                    file.write(user_data)
                else:
                    file.write(",".join(data) + "\n")

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
