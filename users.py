import uuid

class User:
    def __init__(self, name, email, phone_no, address):
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.phone_no = phone_no 
        self.address = address
    
    def add_to_csv(self):
        if not User.find_user_by_email(self.email):
            user_data = f"{self.id},{self.name},{self.email},{self.phone_no},{self.address}\n"
            with open("users.csv", "a") as file:
                file.write(user_data)

            print("----------------------------")
            print("User added successfully!")   
            print("-----------------------------")
        
        else: 
            print("User Exists. Continue")

    
    def find_user_by_email(email):
        user = None

        with open("users.csv", "r") as file:
            for line in file:
                user_info = line.strip().split(",") #['book', 2012]

                if user_info[2] == email:
                    user = user_info
                    return user
        return user
    

    def find_user_by_id(self,id):
        found = False
        with open("users.csv", "r") as file:
            for line in file:
                user_info = line.strip().split(",")
                if user_info[0] == id:
                    found = True
                    return found
            if not found:
                return found
