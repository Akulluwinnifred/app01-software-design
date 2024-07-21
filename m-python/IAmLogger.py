# using the static method (lazy implementation)
# class IAmLogger:
#     __instance = None
#     username = ''
#     password = ''

#     @staticmethod
#     def get_instance():
#         if IAmLogger.__instance == None:
#             IAmLogger()
#         return IAmLogger.__instance

#     def __init__(self,username,password):
#         if IAmLogger.__instance != None:
#             raise Exception("user already logged in")
#         else:
#             IAmLogger.__instance = self

# print(IAmLogger('madiba', 'pwdmadiba'))
# print(IAmLogger.get_instance() )

class IAmLogger:
    __instance = None #static instance
    __user = None
    
    def __init__(self,username,password):
        if IAmLogger.__instance is None: 
            IAmLogger.__user = {
                'username':username,
                'password':password
                }
            IAmLogger.__instance = self
    
    @staticmethod
    def login(username,password):
        if IAmLogger.__instance is None:
            raise Exception('User not logged in')
        else:
            if IAmLogger.__user['username'] == username and IAmLogger.__user['password'] == password:
                print('Logged in successfully')
            else:
                print('Invalid credentials')
    
    @staticmethod
    def logout():
        IAmLogger.__instance = None
        print('Logged out successfully')
    
    # def __new__(cls):
    #     if cls.__instance is None:
    #         cls.__instance = super(IAmLogger,cls).__new__(cls)
    #     return cls.__instance
    
print(IAmLogger())