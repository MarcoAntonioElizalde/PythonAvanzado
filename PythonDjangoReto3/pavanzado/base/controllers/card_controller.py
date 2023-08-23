import datetime

from ..models import Account
from ..models import Card
from .charge_controller import ChargeController
from .payment_controller import PaymentController
from typing import Union
from django.db.models import Q

class CardController:

    @staticmethod
    def create_card(account: Account, name: str, cvv: str):
        card = Card.objects.create(account_number=account, name=name, cvv=cvv)
        card.save()
        return card

    @staticmethod
    def get_card_by_id(id: int):
        try:
            return Card.objects.get(id=id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def get_cards_list(query:str):
        return Card.objects.filter(Q(name__contains=query) | Q(cvv__contains=query))

    @staticmethod
    def get_card_by_account_id(account_id: int) -> Union[Card, None]:
        try:
            return Card.objects.get(account_id=account_id)
        except Card.DoesNotExist:
            return None

    @staticmethod
    def update_cvv(card_id: int, cvv: str) -> bool:
        card = Card.objects.get(id=card_id)
        card.cvv = cvv
        card.save()
        return card
    @staticmethod
    def make_a_deposit(card: Card, amount: float):
        PaymentController.make_a_payment(card, datetime.datetime.now(), amount)


    @staticmethod
    def make_a_withdrawal(card: Card, amount: float):
        ChargeController.make_a_charge(card, datetime.datetime.now(), amount)

    @staticmethod
    def get_credit_available(card: Card):
        account = Account.objects.get(id=card.account_id)
        balance = account.balance
        if balance > 0:
            return account.limit
        else:
            return account.limit + balance

    @staticmethod
    def get_limit_credit(card: Card):
        account = Account.objects.get(id=card.account_id)
        return account.limit

    @staticmethod
    def get_balance(card: Card):
        account = Account.objects.get(id=card.account_id)
        return account.balance

    @staticmethod
    def delete_card(id: int):
        card = Card.objects.get(id=id)
        print(f'card id {card.id}')
        print(f'card account number {card.account_number}')
        account = Account.objects.get(account_number=card.account_number)
        balance = account.balance
        if balance == 0:
            card.delete()
        else:
            raise RuntimeError('Balance must be zero to delete this card')