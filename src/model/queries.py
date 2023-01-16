import sqlite3

class verifiedque():

    def __init__(self):

        self.con = sqlite3.connect("verification.db")
        self.cur = self.con.cursor()


    def get_user(self, id):
        try:
            self.cur.execute(f"SELECT * FROM verifi WHERE user_id='{id}'")
            user_in_db= self.cur.fetchone();
            return user_in_db

        except sqlite3.Error as error:
            print("error error queries >>", error)


    def update(self, table, value, username_id):
        try:
            self.cur.execute(f"UPDATE verifi SET {table} ='{value}' WHERE username_id='{username_id}'")

        except sqlite3.Error as error:
            print(f"unable to update user {table} >>", error)
