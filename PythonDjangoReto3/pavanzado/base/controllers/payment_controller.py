import datetime
from ..models import Card
from ..models import Payment
from .account_controller import AccountController
from django.db.models import Q


class PaymentController:

    @staticmethod
    def get_payment_list(query:str):
        return Payment.objects.filter(Q(id__contains=query) | Q(date_time__contains=query))


    @staticmethod
    def get_object(payment_id):
        try:
            return Payment.objects.get(id=payment_id)
        except Payment.DoesNotExist:
            raise RuntimeError('Payment does not exist')

    @staticmethod
    def create_payment(card:Card, date_time: datetime.datetime, amount:float):
        try:
            return Payment.objects.create(card_id=card, date_time=date_time, amount=amount)
        except Payment.DoesNotExist:
            raise RuntimeError(f'Charge with id {id} does not exist')

    @staticmethod
    def make_a_payment(card: Card, date_time: datetime.datetime, amount: float):
        account = AccountController.get_account_by_number(account_number=card.account_number)

        if amount > 0:
            card_id = card.id
            payment = PaymentController.create_payment(card=card, date_time=date_time, amount=amount)
            AccountController.update_balance(account=account, amount=amount)
            payment.save()
            return payment
        else:
            raise RuntimeError("Invalid amount")

    @staticmethod
    def get_payment_id(id: int):
        try:
            return Payment.objects.get(id=id)
        except Payment.DoesNotExist:
            raise RuntimeError(f'Charge with id {id} does not exist')

    @staticmethod
    def get_payments_by_card(card_id: int):
        try:
            payments = Payment.objects.filter(card_id=card_id)
            return payments
        except Card.DoesNotExist:
            raise RuntimeError(f'No charges were found in card id {card_id}')

    @staticmethod
    def delete_payment(id: id):
        payment = PaymentController.get_payment_id(id=id)
        payment.delete()


