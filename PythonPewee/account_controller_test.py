from controllers.user_controller import UserController
from controllers.account_controller import AccountController
from controllers.card_controller import CardController
import datetime


def test_card_balance():
    user = UserController.create_user(age=33, name='Marco Elizalde')
    account = AccountController.create_account(user=user, balance=15000, open_date=datetime.datetime.now(), limit=50000)
    card = CardController.create_card(account=account, name="Like U", cvv="666")

    assert CardController.get_balance(card) == 15000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 50000

    CardController.make_a_deposit(card, amount=2000)
    assert CardController.get_balance(card) == 17000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 50000

    CardController.make_a_withdrawal(card, amount=13000)
    assert CardController.get_balance(card) == 4000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 50000

    CardController.make_a_withdrawal(card, amount=5000)
    assert CardController.get_balance(card) == -1000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 49000

    CardController.make_a_withdrawal(card, amount=49000)
    assert CardController.get_balance(card) == -50000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 0

    CardController.make_a_withdrawal(card, amount=49000)
    assert CardController.get_balance(card) == -50000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 0

    CardController.make_a_deposit(card, amount=3000)
    assert CardController.get_balance(card) == -47000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 3000

    CardController.make_a_withdrawal(card, amount=1000)
    assert CardController.get_balance(card) == -48000
    assert CardController.get_limit_credit(card) == 50000
    assert CardController.get_credit_available(card) == 2000

    UserController.delete_user(user)
