import json


class Account:
    def __init__(
        self, acc_name: str, acc_no: int, acc_pin: int, create_acc: bool = False
    ):
        self.__account_name = acc_name
        self.__account_no = acc_no
        self.__account_pin = acc_pin
        self.__account = None

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
                self.__account = accounts[self.__account_no]

    @property
    def get_account_name(self):
        return self.__account_name

    @property
    def get_account_no(self):
        return self.__account_no
