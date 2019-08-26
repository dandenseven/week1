import json
import os


PATH = os.path.dirname(__file__)
TERMINAL = "terminal.json"
TERMINALPATH = os.path.join(PATH, TERMINAL)

terminal = {}

def load():
    global terminal
    with open (TERMINALPATH, 'r') as file_object:
        terminal = json.load(file_object)

def save():
    with open(TERMINALPATH, 'w') as json_file:
        json.dump(terminal, json_file, indent=3)

def get_balance(account_num, balance):
    terminal[account_num] = {"withdrawal"}
    print(terminal[balance])
    
        
def get_debit(transaction, balance):
    charges = terminal[transaction]["charges"]
    return sum(charges)/len(balance)

def get_withdrawals(account_num, withdrawal):
    terminal[withdrawal] = {"withdrawals" :[]}