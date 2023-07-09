# from books import Book  

# def selection_validate():

#     valid_selections = ('1', '2', '3', '4', '5', '6')

#     message = input("Welcome to the main menu. Press enter to continue: ")

#     loop = 'yes'

#     while True and loop == 'yes':

#         selection = input("\nPlease select from the following menu (Type exit to exit program) \n"

#                           "To request a new loan enter 1 \n"

#                           "To return a book enter 2 \n"

#                           "To extend a loan enter 3 \n"

#                           "To add a user enter 4 \n"

#                           "To update a user enter 5 \n"

#                           "To add a book enter 6 \n"

#                           "\nEnter choice: ")

#         if selection == 'exit':
#             break

#         else:

#             if selection in valid_selections:
#                 loop = 'no'

#             else:
#                 print('\nValue: {} did not match any menu choice'.format(selection))

#                 loop = 'yes'

#     return selection

# def selection_calls():
    
#     selection = selection_validate()

#     if selection == '1':
#         pass

#     elif selection == '2':
#         pass

#     elif selection == '3':
#         pass

#     elif selection == '4':
#         pass

#     elif selection == '5':
#         pass

#     elif selection == '6':

#         book_name = input("Enter Book Name: ")

#         title = input("Enter Title: ")

#         author = input("Enter author: ")

#         quantity = input("Enter quantity: ")

#         pub_year = input("Enter Publication Year: ")

#         edition = input("Enter Edition: ")

#         book_id = input("Enter Book Id: ")




#         new_book = Book(book_id=book_id, book_name=book_name, title=title, author=author, quantity=quantity, pub_year=pub_year, edition=edition)

#         new_book.add_book()




# if __name__ == '__main__':

#     selection_calls()

import uuid


unique_id = uuid.uuid4()
print(unique_id)