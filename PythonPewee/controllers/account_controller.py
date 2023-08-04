from Tools.scripts.var_access_benchmark import A

from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from typing import Union

import datetime

# CRUD
class AccountController:

    @staticmethod
    def create_account(user: User, balance: float, open_date: datetime.datetime,
                       limit: float) -> Account:
        account = Account(user_id=user.id, balance=balance, open_date=open_date, limit=limit)
        account.save()
        return account

    # read
    @staticmethod
    def get_account_by_id(id: int) -> Account:
        return Account.get(id=id)

    @staticmethod
    def get_account_by_user(user: User) -> Union[Account, None]:
        try:
            return Account.get(user_id=user.id)
        except Account.DoesNotExist:
            return None

    @staticmethod
    def get_account_by_card(card=Card) -> Account:
        return Card.get(id=card.account_id)

    @staticmethod
    def update_balance(account: Account, amount: float) -> bool:
        balance = account.balance + amount
        limit = account.limit
        if balance <= limit:
            account.balance += amount
            account.save()
            return True
        else:
            print('Not enough credit')
            return False


    @staticmethod
    def update_limit(account: Account, limit: int):
        if limit > 0:
            account.limit += limit
            account.save()
        else:
            print("Limit must be positive")

    @staticmethod
    def delete_account(account: Account):
        try:
            card = Card.get(account_id=account.id)
        except:
            card = None

        if card is None:
            account.delete_instance()
        else:
            account.delete_instance()
            card.delete_instance()


