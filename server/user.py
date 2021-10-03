class user:

    def __init__(self, userId, username, password):
        self.userId = userId
        self.username = username
        self.password = password
        self.authenticated = False

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.userId