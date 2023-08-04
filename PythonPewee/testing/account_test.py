import datetime
from schemas.user import User
from schemas.account import Account


def test_create_account():
    openDate = datetime.datetime.now()
    user = User(name="Marco", age=12)
    account = Account(user.id, balance=15000, open_date=openDate, limit=50000)
    assert account.id is None
    assert account.balance == 15000
    assert account.open_date == openDate
    assert account.limit == 50000