class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data):
        return User(
            id=str(data.get('_id')),
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
        )