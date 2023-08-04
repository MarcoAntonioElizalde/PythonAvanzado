import datetime
from schemas.card import Card
from schemas.user import User
from schemas.account import Account

def test_create_card():
    openDate = datetime.datetime.now()
    user = User(name="Marco", age=12)
    account = Account(user.id, balance=15000, open_date=openDate, limit=50000)
    card = Card(account_id=account.id, name="Like U", cvv="666")
    assert account.id is None
    assert card.name == "Like U"
    assert card.cvv == "666"
