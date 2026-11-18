import json
from dataclasses import dataclass

"""
HACK: Data structure of json file
account_no:{
    name: "str",
    account_pin: int,
    balance: int
}
"""


# main structure defination of accounts
@dataclass
class _AccountCore:
    """documentation here (basic data structure for all accounts)"""
    # fundamental block of all upcoming classes.

    account_no: int
    account_name: str
    account_pin: int
    balance: int


class Bank:
    """documentation here"""

    def __init__(self) -> None:
        # json file of accounts
        self.__account_fp = open("data\\account_info.json")

    def add_account(self, account_data: _AccountCore):
        """documentation here (adds another account to data file.)"""
        account_file_data = json.load(self.__account_fp)
        acc_no = account_data.account_no
        account_file_data[acc_no] = acc_no
        account_file_data[acc_no]["name"] = account_data.account_name
        account_file_data[acc_no]["account_pin"] = account_data.account_pin
        account_file_data[acc_no]["balance"] = account_data.balance

        # TODO: complete Bank

    def __delete__(self, instance):
        """destructor, closes the file"""
        self.__account_fp.close()

    # TODO: after bank proceed to Account.

class Account:
    # TODO: make the class more abstract by shifiting data managing to <_Bank> and <_AccountCore>
    # This class is useless till now, progress will be after bank.

    def __init__(
        self, acc_name: str, acc_no: int, acc_pin: int, create_acc: bool = False
    ):
        self.__account_name = acc_name
        self.__account_no = acc_no
        self.__account_pin = acc_pin
        self.__account = None
        self.__balance = None
        super().__init__()

        # account data file (data\account_info.json) -->
        with open("data\\account_info.json", "w") as fp:
            accounts = json.load(fp)

            if self.__account_no in accounts:
                raise NameError("Account no already found!")

            if create_acc:
                accounts[self.__account_no] = {
                    "name": self.__account_name,
                    "account pin": self.__account_pin,
                }

                # updating account data file for adding new account.
                json.dump(accounts, fp)
            else:
                self.__account = accounts[self.__account_no]  # taken data from account
                self.__balance = self.__account["balance"]

    @property
    def get_account_name(self):
        """getter for self.__account_name"""
        return self.__account_name

    @property
    def get_account_no(self):
        """getter form self.__account_no"""
        return self.__account_no

    @property
    def get_balance(self):
        """getter for self.__balance"""
        return self.__balance

    @get_balance.setter
    def set_balanace(self, new_balance):
        self.__balance = new_balance  # change the current balance

        # TODO: finish later

