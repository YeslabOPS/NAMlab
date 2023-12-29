import random


class Login:
    def __init__(self, system_name):
        print(system_name)
        self.database = {}
        self.level = 3
        self.sign_up()
        #self.login

    def _get_account(self):
        self.username = input('请输入用户名：')
        self.password = input('请输入密码：')

    def sign_up(self):
        self._get_account()
        user_id = str(random.randint(1,100))
        self.database[user_id] = {'username': self.username,
                                       'password': self.password,
                                       'level': self.level}
        print(f'User {self.username} has already been record, User ID is {user_id}')

    def find_id(self, query_id):
        if query_id in self.database:
            print(f'{query_id}: {self.database[query_id]['username']}')
    
    def login(self):
        self._get_account()
        for user_id in self.database:
            if self.database[user_id]['username'] == self.username:
                if self.database[user_id]['password'] == self.password:
                    print(f'登录成功！用户级别为{self.database[user_id]['level']}')


system1 = Login('思科门户')
system1.login()

system2 = Login('华为门户')
system2.login()

