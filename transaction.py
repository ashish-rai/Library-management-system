import datetime

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
        print("-----------------------------")


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

                transactions.append(line + "\n")
            file.close()

        if transaction_found:
            f = open("transaction.csv", "w+")

            for transaction in transactions:
                f.write(transaction)
            f.close()
        
        else:
            print("No Transaction Found. Please check email !!!")
