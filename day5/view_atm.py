print("Welcome to The Rebulic Terminal Teller!:")

def get_account_num():
        return input("Storm Trooper Name: ")


def show_menu(account_num):
    print("create an account")
    print("Log in: {}".format(account_num))
    print("Options")
    print("quit")
    print()
    print("your balance is: {}".format())

def account_creation(first_name, last_name):
    print("first_name: {}".format(first_name))
    print("last_name: {}".format(last_name))
def get_input(pin):
    print("PIN: {}".format(pin))
    print("confirm pin: ", end="")
    return input()
    print("Account created, your account number is {}.".format(account_num))

def menu_options(balance):
    print("Choose more options:")
    print("Check Balance: {}".format(balance))
    print("Withdraw Funds:", end="")
    return input()
    print("Deposit Funds:", end="")
    return input()

def show_debit(debit):
    print()
    print("Storm Trooper's debit info {}.".format(debit))
    

if __name__ == "__main__":
    show_menu("Storm Trooper")