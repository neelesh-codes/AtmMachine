from account import AtmAccount, Account

my_account = AtmAccount(10, "Neelesh", 12994, 1122)

print(my_account)

print(my_account.account_name)
print(my_account.balance)

o_account = Account(1)

print(o_account.get_account_name)