import datetime
from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from schemas.payment import Payment
from controllers.account_controller import AccountController
from typing import Union, List


class PaymentController:

    @staticmethod
    def make_a_payment(card: Card, date_time: datetime.datetime, amount: float):
        account = Account.get(id=card.account_id)

        if amount > 0:
            card_id = card.id
            payment = Payment(card_id=card_id, date_time = date_time, amount=amount)
            AccountController.update_balance(account=account, amount=amount)
            payment.save()
        else:
            print("Invalid amount")

    @staticmethod
    def get_payment_id(id: int) -> Union[Payment, None]:
        try:
            return Payment.get(id=id)
        except Payment.DoesNotExist:
            print(f'Charge with id {id} does not exist')
            return None

    @staticmethod
    def get_charges_by_card(card: Card) -> Union[List, None]:
        try:
            return list(Payment.filter(card_id=card.id))
        except Card.DoesNotExist:
            print(f'No charges were found in card id {card.id}')
            return None

    @staticmethod
    def delete_charge(charge: Payment):
        charge.delete_instance()


