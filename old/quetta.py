import time
from datetime import datetime

from google_service import GoogleService

from process_messages import ProcessMessages

class Server:
    def __init__(self):
        self.gs = GoogleService()
        self.process_messages = ProcessMessages(self.gs)
        self.message_list = []
        self.update = True
        self.update_time = "21:30"
        
    # server entry point
    def runtime(self, notification):
        if notification == 'notify':
            self.process_messages.feature_notification()
        if self.update_check() is False:
            if self.new_messages():
                self.process_messages.process(self.message_list)
                time.sleep(30)
                self.runtime('')
            else:
                print("no messages in the inbox")
                time.sleep(30)
                self.runtime('')
        


    # check for new messages
    def new_messages(self):
        print(datetime.now().strftime("%H:%M"), "checking messages")
        message_list = self.gs.get_messages()
        # check to see if message list isnt empty
        if message_list != []:
            self.message_list = message_list
            return True

    def update_check(self):
        if self.update == True and datetime.now().strftime("%H:%M") == self.update_time:
            self.process_messages.update("automatic")
        else:
            return False

       
        
            


 
 
        

            

