import view_atm
import model_atm


def run():
    model_atm.load()
    account_num = view_atm.get_account_num()
    mainmenu(account_num)

def mainmenu(account_num):
    while True:
        view_atm.show_menu(account_num)
        selection = view_atm.get_input()
        
        if selection == '3':
            model_atm.save()
            return
        elif selection == '1':
            newtransaction = view_atm.get_input()
            model_atm.add_transaction(account_num, transaction)
        elif selection == '2':
            debit = model_atm.get_debit(account_num)
            view_atm.show_debit(debit)


if __name__ == "__main__":
    run()
    
    