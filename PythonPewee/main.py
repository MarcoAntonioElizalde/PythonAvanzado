
from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from schemas.account import Account
from schemas.user import User
from schemas.card import Card
import datetime


if __name__ == '__main__':
    create_db('db/db_oltp.db')
    user = UserController.create_user(age=60, name='Juan Lopez')
    account = AccountController.create_account(user=user, balance=0, open_date=datetime.datetime.now(), limit=50000)
    card = CardController.create_card(account=account, name="Platinum",cvv="666")

    #AccountController.update_limit(account, 3000)
    AccountController.update_balance(account, 3000)

    for i in Account.select():
        print(i.id, i.user_id, i.balance, i.open_date, i.limit)

    for i in User.select():
        print(i.id, i.name, i.age)

    for i in Card.select():
        print(i.id, i.account_id, i.name, i.cvv)
