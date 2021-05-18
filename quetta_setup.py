import sqlite3
import os
import time

print("creating quetta database.")
conn = sqlite3.connect('quetta.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE users (
    email text,
    last_message text
    )""")
conn.commit()
conn.close()
time.sleep(5)

print("installing requirements")
time.sleep(5)
os.system("pip install -r requirements.txt")
print("\n\nNow you need to enable the gmail API, do so on the following page and copy the credentials.json file into the Quetta directory. ")
time.sleep(5)
print("https://developers.google.com/gmail/api/quickstart/python")
print("\n\nAfter enabling the API, ensure your Gmail is clear of any messages as Quetta will respond to all on the first run. Run Quetta when you are ready. (Python3 run_quetta.py)")