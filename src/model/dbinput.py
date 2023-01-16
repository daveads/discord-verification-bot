import sqlite3
from datetime import datetime

con = sqlite3.connect("verification.db")
cur = con.cursor()

class verify_data():
  def __init__(self, username, user_id, age_verified, age_verified_g, selfie_verified, selfie_verified_g,  age_verification_date,  selfie_verification_date):
    self.username = username
    self.user_id = user_id
    self.age_verified = age_verified
    self.age_verified_g = age_verified_g
    self.selfie_verified = selfie_verified
    self.selfie_verified_g = selfie_verified_g
    self.age_verification_date = age_verification_date
    self.selfie_verification_date = selfie_verification_date
    #datetime.utcnow().strftime("%d-%m-%Y")

    try:
      cur.execute("INSERT INTO verifi VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (
      self.username,
      self.user_id,
      self.age_verified,
      self.age_verified_g,
      self.selfie_verified,
      self.selfie_verified_g,
      self.age_verification_date,
      self.selfie_verification_date
    ))
      con.commit()
      con.close()

    except sqlite3.Error as error:
      print(f"unable to create add {self.username} into the database >> ", error)