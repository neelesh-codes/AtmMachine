import json
import pathlib
from dataclasses import asdict, dataclass

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
class AtmAccount:
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
        self.file_path = pathlib.Path("data") / "account_info.json"
        self.account_fp = open(self.file_path)

    def check_account_existence(self, account_no) -> bool:
        """documentation here (checks the existence of an account)"""
        accounts = json.load(self.account_fp)

        return account_no in accounts

    # FIX: fix the error description in end of the file

    def get_account_data(self, account_no: int) -> AtmAccount:
        """documentation here (get data of an account"""

        if not self.check_account_existence(account_no):
            raise NameError("Account does not exists")

        account_data = json.load(self.account_fp)[account_no]
        account = AtmAccount(**account_data)
        return account

    def add_account(self, account: AtmAccount):
        if self.check_account_existence(account.account_no):
            raise NameError("Account already exists")

        accounts = json.load(self.account_fp)

        account_dict = asdict(account)
        accounts[account.account_no] = account_dict

        json.dump(accounts, self.account_fp)

    def __delete__(self, instance):
        """destructor, closes the file"""
        self.account_fp.close()

    # TODO: after bank proceed to Account.


class Account(_Bank):
    def __init__(self, acc_no: int):
        super().__init__()

        self.__account = self.get_account_data(acc_no)

    @property
    def get_account_name(self):
        return self.__account.account_name


"""
Traceback (most recent call last):
  File "d:\AtmMachine\src\atmmachine\test_account.py", line 10, in <module>
    o_account = Account(1)
  File "d:\AtmMachine\src\atmmachine\account.py", line 72, in __init__
    super().__init__()
    ~~~~~~~~~~~~~~~~^^
  File "d:\AtmMachine\src\atmmachine\account.py", line 34, in __init__
    self.account_fp = open(self.file_path)
                      ~~~~^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'data\\account_info.json'
"""

# file not found maybe system path mistake, 😊😊
# or some blunder done by you bastard in handling the paths
# fix it, I trust you buddy ❤️
# I've not completed my part but still
# Ahoi and Mira you can focus on he UI fast
# Ryuk design the network architecutre in your repo as fast as possible
# Eya and me gonna implement it very soon
# 👋👋
