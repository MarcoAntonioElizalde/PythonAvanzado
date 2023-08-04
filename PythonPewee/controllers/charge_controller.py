import datetime
from schemas.account import Account
from schemas.user import User
from schemas.card import Card
from schemas.charge import Charge
from controllers.account_controller import AccountController
from typing import Union, List


class ChargeController:

    @staticmethod
    def make_a_charge(card: Card, date_time: datetime.datetime, amount: float):
        account = Account.get(id=card.account_id)

        if amount > 0:
            card_id = card.id
            charge = Charge(card_id=card_id, date_time = date_time, amount=amount)
            AccountController.update_balance(account=account, amount=-amount)
            charge.save()
        else:
            print("Invalid amount")

    @staticmethod
    def get_charge_id(id: int) -> Union[Charge, None]:
        try:
            return Charge.get(id=id)
        except Charge.DoesNotExist:
            print(f'Charge with id {id} does not exist')
            return None

    @staticmethod
    def get_charges_by_card(card: Card) -> Union[List, None]:
        try:
            return list(Charge.filter(card_id=card.id))
        except Card.DoesNotExist:
            print(f'No charges were found in card id {card.id}')
            return None

    @staticmethod
    def delete_charge(charge: Charge):
        charge.delete_instance()


