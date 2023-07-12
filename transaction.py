import datetime
import csv


class Transaction():
    counter = 0
    Due_Duration = 7

    def __init__(self, user_id, book_id, transaction_date, due_date):
        Transaction.counter += 1
        self.transaction_id = Transaction.counter 
        self.book_id = book_id
        self.user_id = user_id
        self.transaction_date = transaction_date
        self.due_date = due_date
        self.return_date = None
  
    def make_transaction(self):
        transaction_detail = f"{self.transaction_id},{self.user_id},{self.book_id},{self.transaction_date},{self.due_date},{self.return_date}\n"
        with open("transaction.csv", "a") as file:
            file.write(transaction_detail)
        print("----------------------------")
        print("Transaction Successfull!!!")   
        print("----------------------------")


    def update_return_book(user_id):
        transactions = []
        transaction_found = False

        with open("transaction.csv", "r") as file:
            for line in file:
                line_list = line.strip().split(",") 

                if line_list[1] == user_id and line_list[5] == "None":
                    line_list[5] = str(datetime.date.today())
                    line = ','.join(line_list)
                    transaction_found = True

                transactions.append(line)
            file.close()

        if transaction_found:
            f = open("transaction.csv", "w+")

            for transaction in transactions:
                f.write(transaction)
            f.close()
        
        else:
            print("No Transaction Found. Please check email !!!")


    def get_borrowed_book_ids_by_user(user_id):
        book_ids = []
        with open('transaction.csv', 'r') as file:
            for line in file:
                transaction_details = line.strip().split(',')
                if transaction_details[1].lower() == user_id.lower() and transaction_details[5].lower() == "none":
                    book_ids.append(transaction_details[2])
        
        return book_ids
    
    def extend_book_due_date_for_user(book_id, user_id, number_of_days_to_extend):
        transactions = []
        found = False
        with open('transaction.csv', 'r') as file:
            for row in file:
                row_info = row.strip().split(",") 
                if row_info[1].lower() == user_id and row_info[2].lower() == book_id:
                    current_due_date = datetime.datetime.strptime(row_info[4], '%Y-%m-%d')
                    new_due_date = current_due_date + datetime.timedelta(days=number_of_days_to_extend)
                    row_info[4] = new_due_date.strftime("%Y-%m-%d")
                    row =  ','.join(row_info)
                    found = True

                transactions.append(row)

        if found:
            f = open("transaction.csv", "w+")

            for transaction in transactions:
                f.write(transaction)
            f.close()
        
        else:
            print("No Transaction Found. Please check email !!!")
