import sqlite3
from datetime import datetime
from os.path import exists

con = sqlite3.connect("verification.db")
cur = con.cursor()

def main():
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS verifi (
            id INTEGER PRIMARY KEY ,
            username VARCHAR(255),
            user_id VARCHAR(25),
            
            age_verified int,
            age_verified_g  VARCHAR(25),
            
            selfie_verified int,
            selfie_verified_g VARCHAR(25),

            age_verification_date VARCHAR(12),
            selfie_verification_date VARCHAR(12)
            )''')
      #print("Table created")

    except sqlite3.Error as error:
        print("unable to create database table", error)


    test = cur.execute("SELECT * FROM verifi WHERE ROWID IN ( SELECT max( ROWID ) FROM verifi );")
    test0 = ()
    for i in test:
        test0 = i


    if len(test0) == 0:
        try:
            cur.execute("INSERT INTO verifi VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?);", (
                                                                  "creator0000",
                                                                  "00000000022331",

                                                                   1,
                                                                   "3456789532345678",

                                                                   1,
                                                                   "3456896323456768",

                                                                  "2024-12-12",
                                                                  "2023-10-03"))
            print(">>>   Default Values Inputed")
            con.commit()

        except sqlite3.Error as error:
            print(">>>   Unable To Input Default Data >> ", error)

    else:
        print(">>>   Default Data Already Exist")


if __name__ == '__main__':
  main()