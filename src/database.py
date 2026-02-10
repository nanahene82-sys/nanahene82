# Database Models and Operations

class DatabaseModel:
    def __init__(self, data):
        self.data = data

    def save(self):
        # Code to save the model to the database
        pass

    def delete(self):
        # Code to delete the model from the database
        pass

class User(DatabaseModel):
    def __init__(self, username, email):
        super().__init__({'username': username, 'email': email})

class Post(DatabaseModel):
    def __init__(self, title, content):
        super().__init__({'title': title, 'content': content})
