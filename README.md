# Quetta (Q)
A Python bot using Google's Gmail API to respond to messages.

### Getting Started

Hello, Q uses OS env variables so when you go through the setup process you will need to modify your bash_profile file to export two variables. OWNER_EMAIL is your email and QUETTA_EMAIL is the Gmail you want Q to listen to. 

### Installation
1. Create a Python virtualenv for Q.
2. Clone the Repo
3. Run "quetta_setup.py" ***Make sure you are in your virtualenv*** (creates the SQLite DB and installs requirements into the virtualenv)
4. You will be prompted by quetta_setup.py to enable the Google API on the Google Quickstart page, follow the instructions in the terminal.
5. Ensure that the Gmail you have configured Q to listen to is clean, if you run "run_quetta.py" Q will respond to every message. (I havent configured a bypass for    this yet)
6. Run "run_quetta.py" - - python3 run_quetta.py std - - std is a place holder for the feature notification arg.


### References

#### Gmail API
https://developers.google.com/gmail/api/quickstart/python

#### API Usage Limits
https://developers.google.com/gmail/api/v1/reference/quota

#### API Scopes 
https://developers.google.com/gmail/api/auth/scopes
