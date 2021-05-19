from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


# If modifying these scopes, delete the file token.pickle.


class GmailApi:
    def __init__(self):
        self.scopes = ['https://mail.google.com/']
        self.creds = None
        self.path = f"{os.path.abspath('.')}/src/credentials/"

    def service(self):
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(f'{self.path}token.pickle'):
            with open(f'{self.path}token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'{self.path}credentials.json', self.scopes)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(f'{self.path}token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        return build('gmail', 'v1', credentials=self.creds)

    def get_messages(self):
        message_list = []
        results = self.service().users().messages().list(userId='me', labelIds=['INBOX']).execute()
        messages = results.get('messages', [])
        for message in messages:
            msg = self.service().users().messages().get(userId='me', id=message['id']).execute()
            for element in msg['payload']['headers']:
                if element['name'] == 'From':
                    message_list.append({"from": element['value'].split('<')[1].replace('>',''),
                                    "message": msg['snippet'],
                                    "id": message['id']})
        return message_list

    def send_message(self, message):
        message = (self.service().users().messages().send(userId='me', body=message).execute())
        if message is not None:
            return True

