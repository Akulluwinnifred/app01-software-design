from typing import Protocol

# Login Strategies:

class LoginStrategy(Protocol):
    def login(self, credentials: dict) -> bool: ...

class UsernameAndPasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> bool:
        # {username: "usnm", password: "pswd"}
        print("Username And Password Login Strategy")
        print("Username: " + credentials["username"])
        print("Password: " + credentials["password"])
        print(" ")

class EmailAndPasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> bool:
        # {email: "email@example.com", password: "pswd"}
        print("Email And Password Login Strategy")
        print("Email: " + credentials['email'])
        print("Password: " + credentials["password"])
        print(" ")

class PhoneNumberAndPasswordStrategy(LoginStrategy):
    def login(self, credentials: dict) -> bool:
        # {phone_number: "email@example.com", password: "pswd"}
        print("PhoneNumber And Password Login Strategy")
        print("PhoneNumber: " + credentials['phone_number'])
        print("Password: " + credentials["password"])
        print(" ")


# Login Context Class
class IAMlogger:
    __instance = None
    __login_strategy: LoginStrategy
    __credentials = None

    def __init__(self, login_strategy: LoginStrategy, credentials: dict):
        if IAMlogger.__instance is None:
            IAMlogger.__instance = self
            IAMlogger.__login_strategy = login_strategy
            IAMlogger.__credentials = credentials

    @staticmethod
    def login(login_strategy: LoginStrategy, credentials: dict):
        if IAMlogger.__instance is None:
            IAMlogger(login_strategy, credentials)
            IAMlogger.__login_strategy.login(credentials)
        return IAMlogger.__instance


    @staticmethod
    def logout():
        IAMlogger.__instance = None
        if IAMlogger.__instance is None:
            return "Logged out successfully"
        

    @staticmethod
    def get_instance():
        return IAMlogger.__instance

    @staticmethod
    def get_user_details():
        if IAMlogger.__instance is not None:
            return IAMlogger.__credentials
        else:
            return "No active user logged in"


    @staticmethod
    def set_login_strategy(login_strategy: LoginStrategy):
        IAMlogger.__login_strategy = login_strategy

# Login instances
login_strategy = UsernameAndPasswordStrategy()
user1 = IAMlogger.login(login_strategy, {'username':'vanessa', 'password':'@vanessa123'})
IAMlogger.logout()


login_strategy = EmailAndPasswordStrategy()
user2 = IAMlogger.login(login_strategy, {'email':'jovita@refactory.com', 'password':'@jovita123'})
IAMlogger.logout()

login_strategy = PhoneNumberAndPasswordStrategy()
user3 = IAMlogger.login(login_strategy, {'phone_number':'+256701234567', 'password':'@akram123'})
IAMlogger.logout()


login_strategy = UsernameAndPasswordStrategy()
user4 = IAMlogger.login(login_strategy, {'username':'benjamin', 'password':'@benjamin123'})
IAMlogger.logout()

login_strategy = EmailAndPasswordStrategy()
IAMlogger.set_login_strategy(login_strategy)
IAMlogger.login(login_strategy, {'email':'benjamin@example.com', 'password':'@benjamin123'})
