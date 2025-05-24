class BankAccount:
    def __init__(account, first_name, last_name, account_id, account_type, pin, balance):
        account.first_name = first_name
        account.last_name = last_name
        account.account_id = account_id
        account.account_type = account_type
        account.pin = pin
        account.balance = balance
    def deposit(account, money):
        account.balance += money
        return account.balance
    def withdraw(account, money):
        if account.balance >= money:
            account.balance -= money
            return account.balance
        else:
            account.balance = 0
            return account.balance
    def display_balance(account):
        print((f"Your curent balance: {account.balance}"))

user = BankAccount("Dinh", "Manh", 10112005, "Golden", 101105, 150000.0)

user.deposit(96)
user.withdraw(25)
user.display_balance()