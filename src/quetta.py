import os
import sqlite3
from gmailApi import GmailApi
from dbManage import DbManage
import asyncio

class Quetta(GmailApi, DbManage):
    def __init__(self):
        self.db_path = f"{os.path.abspath('.')}/src/db/quetta.db"
        GmailApi.__init__(self)
        DbManage.__init__(self, self.db_path)
        self.checkDBExists()

    # check DB exists, if not create, handled in constructor
    def checkDBExists(self):
        
        def createDB():
            print(self.db_path)
            print(self.db_path)
            print("creating quetta database.")
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE users (
                email text,
                last_message text
                )""")
            conn.commit()
            conn.close()
                    
        if os.path.exists(self.db_path):
            pass
        else:
            createDB()
    
    
    async def checkMessages(self):
        await asyncio.sleep(5)
        while self.get_messages() == []:
            print("No messages.")
            await asyncio.sleep(5)
        return self.get_messages()
      
    async def start(self):
       result = await self.checkMessages()

    async def restart(self):
        

asyncio.run(Quetta().start())



    
