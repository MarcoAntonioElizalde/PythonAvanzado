from db.migrations import create_db
from schemas.user import User
from controllers.user_controller import UserController

def test_create_user():
    user = User(name="Marco", age=12)
    assert user.id is None
    assert user.name == "Marco"
    assert user.age == 12

