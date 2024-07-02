import json
import os

os.system('clear')

class CRUD:
    def __init__(self):
        self.data = self.load_json_file()

    def load_json_file(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
            
        return data

    def create_account(self,data):
        id = len(data['accounts']) +1
        print('\nID:',id)
        username = input('Enter new username: ')
        password = input('Enter new pass: ')
        email = input('Enter new email: ')
        first_name = input('Enter new first name: ')
        last_name = input('Enter new last name: ')
        age = int(input('Enter new age: '))
        new_account = {
                "id": id,
                "user": {
                "username": username,
                "password": password,
                "email": email,
                "details": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "age": age
                }}}
        data['accounts'].append(new_account)
    
    def read_account(self,data):
        for account in data['accounts']:
            user = account['user']
            print(f"\nID: {account['id']}")
            print(f"Username: {user['username']}")
            print(f"Pass: {user['password']}")
            print(f"Email: {user['email']}")
            details = user['details']
            print(f"Full name and age: {details['first_name']} {details['last_name']} {details['age']}")

    def update_account(self,data):
        select_by_id = int(input('\nSelect by ID: '))
        for account in data['accounts']:
            if account['id'] == select_by_id:
                account['user']['username'] = input("Enter new username: ")
                account['user']['password'] = input("Enter new password: ") 
                account['user']['email'] = input("Enter new email: ")
                account['user']['details']['first_name'] = input("Enter new first name: ")
                account['user']['details']['last_name'] = input("Enter new last name: ")
                account['user']['details']['age'] = int(input("Enter new age: "))
                print("Account updated successfully.")
        return

    def delete_account(self,data):
        delete_by_id = int(input('\ndelete by ID: '))
        for account in data['accounts']:
            if account['id'] == delete_by_id:
                data['accounts'].remove(account) 

    def small_menu(self):
        while True:
            print('MAIN MENU\n')
            print('1: Create Account')
            print('2: Show Account')
            print('3: Update Account')
            print('4: Delete Account')
            print('5: Exit')
            menu_choice = int(input('\nEnter your choice: '))
        
            if menu_choice == 1:
                self.create_account(self.data)
                os.system('clear')
            elif menu_choice == 2:
                
                self.read_account(self.data)
                input()
                os.system('clear')
            elif menu_choice == 3:
                self.update_account(self.data)
                os.system('clear')
            elif menu_choice == 4:
                self.delete_account(self.data)
                os.system('clear')
            elif menu_choice == 5:
                exit()
            else:
                menu_choice = input('Enter a valid number')
            
crud = CRUD()
crud.small_menu()