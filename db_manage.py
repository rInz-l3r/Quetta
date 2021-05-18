import sqlite3

class DbManage:
    def __init__(self):
        self.connect = sqlite3.connect('quetta.db')
        self.cursor = self.connect.cursor()

    def check_user(self, email):
        self.cursor.execute("SELECT * FROM users WHERE email=(:email)", {'email':email})
        if self.cursor.fetchone():
            return True
    
    def add_user(self, email, message_id):
        self.cursor.execute("INSERT INTO users VALUES (:email, :last_message)", {'email':email, 'last_message':message_id})
        self.connect.commit()
        return True


    def new_message_id(self, email, message_id):
        self.cursor.execute("SELECT * FROM users WHERE email=(:email) AND last_message=(:last_message)", {'email':email, 'last_message':message_id})
        if self.cursor.fetchone() is None:
            # update last message message id for user.
            with self.connect:
                self.cursor.execute("""UPDATE users SET last_message = :last_message WHERE email = :email""", {'email':email, 'last_message':message_id})
            return True

    def get_users(self):
        user_list = []
        self.cursor.execute("SELECT * FROM users WHERE email!=''")
        for entry in self.cursor.fetchall():
            user_list.append(entry[0])
        return user_list

    def close_connection(self):
        self.connect.close()