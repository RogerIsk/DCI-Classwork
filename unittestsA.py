# a simple login system
class UserLoginSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password): # using register(username, password) you can register
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = password

    def login(self, username, password): # using login(username, password) you can login
        if username not in self.users:
            raise ValueError("User does not exist")
        if self.users[username] != password:
            raise ValueError("Incorrect password")
        return True
    
    