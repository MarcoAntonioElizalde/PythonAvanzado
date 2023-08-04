from schemas.user import User
from schemas.account import Account
from controllers.account_controller import  AccountController

class UserController:

    @staticmethod
    def create_user(age: int, name:str) -> User:
        user = User(age=age, name=name)
        user.save()
        return user

    @staticmethod
    def get_user_by_id():
        return User.get(id=id)

    @staticmethod
    def get_user_by_name(name: str):
        return User.get(name=name)

    @staticmethod
    def update_name(user: User, name: str) -> User:
        user.name = name
        user.save()
        return user

    @staticmethod
    def update_age(user: User, age: int) -> User:
        user.age = age
        user.save()
        return user

    @staticmethod
    def delete_user(user: User):
        try:
            account = Account.get(user_id=user.id)
        except:
            account = None
        if account is None:
            user.delete_instance()
        else:
            AccountController.delete_account(account)
            user.delete_instance()
