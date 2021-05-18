import os
from datetime import datetime

from db_manage import DbManage
from send_messages import SendMessages


class ProcessMessages:
        def __init__ (self, google_service):
            self.database = DbManage()
            self.owner_email = os.environ.get('OWNER_EMAIL')
            self.email_address = os.environ.get('QUETTA_EMAIL')
            self.send_message = SendMessages(google_service)

        def process(self, message_list):
            for message in message_list:
                if self.check_user(message['from']):
                    if self.new_message(message['from'], message['id']):
                        user = message['from']
                        print(f'new message from: {user}')
                        if message['from'] == self.owner_email:
                            self.management(message['message'])
                        self.standard_message(message['from'])
                    return True
                else:
                    print("this user does not exist   ---adding user")
                    if self.add_user(message['from'], message['id']):
                        print("user added")
                        return True
        
        def new_message(self, email_from, message_id):
            print("checking for new messages")
            if self.database.new_message_id(email_from, message_id):
                return True

        def check_user(self, email_from):
            if self.database.check_user(email_from):
                return True

        # need to add whitelisting functionality
        def add_user(self, email_from, message_id):
            if self.database.add_user(email_from, message_id):
                print("sending introduction message")
                self.send_message.new_user_resp(email_from)
            return True

        def standard_message(self, email_from):
            self.send_message.standard_resp(email_from)
        
        def shutdown(self):
            self.send_message.shutdown_confirmation(self.owner_email)
            print("closing db connection")
            self.database.close_connection()
        
        def update(self, status):
            self.send_message.update_confirmation(self.owner_email, status)
            print("closing db connection")
            self.database.close_connection()
            os.system("python3 update.py")
            exit()

        def management(self, body):
            if "shutdown" in body:
                self.shutdown()
                exit()
            if "update" in body:
                self.update("manual")
                os.system("python3 update.py")
                exit()
            else:
                pass

        def feature_notification(self):
            with open('feature_notification.txt', 'r') as f:
                message = f.read()
            for user in self.database.get_users():
                self.send_message.feature_notification(user, message)
