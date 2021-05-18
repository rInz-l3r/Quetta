import os
import json
import base64
from email.mime.text import MIMEText

class SendMessages:
    def __init__(self, google_service):
        self.email_address = os.environ.get('QUETTA_EMAIL')
        self.responses = self.load_responses()
        self.gs = google_service

    # load responses.json
    def load_responses(self):
        with open('responses.json', 'r') as j:
            responses = json.load(j)
        return responses

    # create message format for Gmail API
    def create_message(self, email_to, email_subject, email_body):
        message = MIMEText(email_body)
        message['to'] = email_to
        message['from'] = self.email_address
        message['subject'] = email_subject
        encoding = base64.urlsafe_b64encode(message.as_bytes())
        message_string = encoding.decode()
        return {'raw': message_string}

    # send message through Gmail API
    def send_message(self, message):
        if self.gs.send_message(message):
            return True

   # Send Standard Response
    def standard_resp(self, email_to):
        print("sending standard resp.")
        email_subject = self.responses['deprecated']['subject']
        email_body = self.responses['deprecated']['body']
        if self.send_message(self.create_message(email_to, email_subject, email_body)):
            print(f'standard resp sent to: {email_to}')

    # Send New User Response
    def new_user_resp(self, email_to):
        print("sending NU resp.")
        email_subject = self.responses['introduction']['subject']
        email_body = self.responses['introduction']['body']
        if self.send_message(self.create_message(email_to, email_subject, email_body)):
            print(f'intro resp sent to: {email_to}')
    
    # Send Shutdown Conf Resp
    def shutdown_confirmation(self, email_to):
        print("sending shutdown confirmation resp.")
        email_subject = self.responses['shutdown']['subject']
        email_body = self.responses['shutdown']['body']
        if self.send_message(self.create_message(email_to, email_subject, email_body)):
            print(f'shutdown conf resp sent to: {email_to}')
    
    # Send Update Conf Resp
    def update_confirmation(self, email_to, status):
        print("sending update confirmation resp.")
        if status == "manual":
            email_subject = self.responses['manual_update']['subject']
            email_body = self.responses['manual_update']['body']
        if status == "automatic":
            email_subject = self.responses['automatic_update']['subject']
            email_body = self.responses['automatic_update']['body']
        if self.send_message(self.create_message(email_to, email_subject, email_body)):
            print(f'update conf resp sent to: {email_to}')

    def feature_notification(self, email_to, message):
        email_subject = self.responses['feature_notification']['subject']
        email_body = message
        if self.send_message(self.create_message(email_to, email_subject, email_body)):
            print(f'feature notification sent to: {email_to}')
        