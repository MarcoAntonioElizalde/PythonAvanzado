from db.migrations import create_db
from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
from schemas.account import Account
from schemas.user import User
from schemas.card import Card
import datetime


def run_crud_user():
    print("Running CRUD for user:")
    print("Creating user Marco Elizalde, age 33 years old")
    user = UserController.create_user(age=33, name='Marco Elizalde')

    try:
        print("Showing all the users:")
        for i in User.select():
            print(f"({i.id}, {i.name}, {i.age})")
    except:
        print("No user found")

    print("Reading user from DB")
    user = UserController.get_user_by_name(name='Marco Elizalde')
    print(f"Showing user information Id: {user.id}, Name: {user.name}, Age: {user.age}")
    print("Updating age to 25")
    user = UserController.update_age(user, age=25)
    print(f"Showing user information after update Id: {user.id}, Name: {user.name}, Age: {user.age}")
    print("Deleting user")
    UserController.delete_user(user)

    try:
        print("Showing all the users:")
        for i in User.select():
            print(f"({i.id}, {i.name}, {i.age})")
    except:
        print("No users found")

    print("CRUD completed from User schema")

def run_crud_account():
    print("Running CRUD for account:")
    print("Creating account balance = 15000 and limite = 50000")
    user = UserController.create_user(age=33, name='Marco Elizalde')
    account = AccountController.create_account(user=user, balance=15000, open_date=datetime.datetime.now(), limit=50000)

    try:
        print("Showing all the accounts:")
        for i in Account.select():
            print(f"({i.id}, {i.user_id}, {i.balance}, {i.open_date}, {i.limit})")
    except:
        print("No accounts found")

    print("Reading account from DB")
    account = AccountController.get_account_by_user(user)
    print(f"Showing account information Id: {account.id}, User id: {account.user_id}, Balance: {account.balance}, Open date: {account.open_date}, Limit: {account.limit}")
    print("Updating balance= 50000+12000, limit = 20000")
    AccountController.update_balance(account, amount=12000)
    AccountController.update_limit(account, limit=12000)
    print(f"Showing account information after update Id: {account.id}, User id: {account.user_id}, Balance: {account.balance}, Open date: {account.open_date}, Limit: {account.limit}")
    print("Deleting account and user associated")
    #AccountController.delete_account(account)
    UserController.delete_user(user)

    try:
        print("Showing all the accounts:")
        for i in Account.select():
            print(f"({i.id}, {i.user_id}, {i.balance}, {i.open_date}, {i.limit})")
    except:
        print("No accounts found")

    print("CRUD completed from Account schema")


def run_crud_card():
    print("Running CRUD for card:")
    print("Creating card name = Like U and cvv = 666")
    user = UserController.create_user(age=33, name='Marco Elizalde')
    account = AccountController.create_account(user=user, balance=15000, open_date=datetime.datetime.now(), limit=50000)
    card = CardController.create_card(account=account, name="Like U", cvv="666")

    try:
        print("Showing all the cards:")
        for i in Card.select():
            print(f"({i.id}, {i.account_id}, {i.name}, {i.cvv})")
    except:
        print("No cards found")

    print("Reading card from DB")
    card = CardController.get_card_by_account(account)
    print(f"Showing card information Id: {card.id}, account id: {card.account_id}, name: {card.name}, cvv: {card.cvv}")
    print("Updating cvv = 555")
    CardController.update_cvv(card, cvv=555)
    print(f"Showing card information after update Id: {card.id}, account id: {card.account_id}, name: {card.name}, cvv: {card.cvv}")
    print("Deleting card, account and user associated")
    #CardController.delete_card(card)
    #AccountController.delete_account(account)
    UserController.delete_user(user)

    try:
        print("Showing all the cards:")
        for i in Card.select():
            print(f"({i.id}, {i.account_id}, {i.name}, {i.cvv})")
    except:
        print("No cards found")

    print("CRUD completed from Card schema")


def run_card_balance():
    user = UserController.create_user(age=33, name='Marco Elizalde')
    account = AccountController.create_account(user=user, balance=15000, open_date=datetime.datetime.now(), limit=50000)
    card = CardController.create_card(account=account, name="Like U", cvv="666")

    print("Showing initial data for card")
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a deposit of 2000")
    CardController.make_a_deposit(card, amount=2000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a withdrawal of 13000")
    CardController.make_a_withdrawal(card, amount=13000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a withdrawal of 5000")
    CardController.make_a_withdrawal(card, amount=5000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a withdrawal of 49000")
    CardController.make_a_withdrawal(card, amount=49000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a withdrawal of 1000 to show not enough credit")
    CardController.make_a_withdrawal(card, amount=49000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a deposit of 3000 to have a credit again")
    CardController.make_a_deposit(card, amount=3000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")
    print("Doing a withdrawal of 1000, valid because we did a deposit before")
    CardController.make_a_withdrawal(card, amount=1000)
    print(f"Balance: {CardController.get_balance(card)}, Limit: {CardController.get_limit_credit(card)}, Credit "
          f"available: {CardController.get_credit_available(card)}")

    print("Completed card balance operations")
    UserController.delete_user(user)

if __name__ == '__main__':
    create_db('db/db_oltp.db')
    print("")
    print("")
    run_crud_user()
    print("")
    print("")
    run_crud_account()
    print("")
    print("")
    run_crud_card()
    print("")
    print("")
    run_card_balance()





