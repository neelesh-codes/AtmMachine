import json
from dataclasses import dataclass, asdict

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


class _Bank:
    """documentation here"""

    def __init__(self) -> None:
        # json file of accounts
        self.__account_fp = open("data\\account_info.json")

    def check_account_existence(self, account_no) -> bool:
        """documentation here (checks the existence of an account)"""
        accounts = json.load(self.__account_fp)

        return account_no in accounts

    def get_account_data(self, account_no: int) -> _AccountCore:
        """documentation here (get data of an account"""

        if not self.check_account_existence(account_no):
            raise NameError("Account does not exists")

        account_data = json.load(self.__account_fp)[account_no]
        account = _AccountCore(**account_data)
        return account

    def add_account(self, account: _AccountCore):
        if self.check_account_existence(account.account_no):
            raise NameError("Account already exists")

        accounts = json.load(self.__account_fp)

        account_dict = asdict(account)
        accounts[account.account_no] = account_dict

        json.dump(accounts, self.__account_fp)
        


    def __delete__(self, instance):
        """destructor, closes the file"""
        self.__account_fp.close()

    # TODO: after bank proceed to Account.


# extra -->
# Unused part intended to cover in future
# don't look over here 😊😊.
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
