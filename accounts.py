#Should turn Account into an Abstract class
#remember to do type hinting and docstrings!!

class Account:
    def __init__(self, name, balance = 0):
        self.__account_name = name
        self.set_balance(balance)



    def deposit(self, amount):
        '''
        
        :param:
        :return:
        '''
        if amount <= 0:
            # print(f'did NOT deposit {amount} for {self.get_name()}, current balance = {self.get_balance()}')
            return False
        
        self.__account_balance += amount
        # print(f'did deposit {amount} for {self.get_name()}, current balance = {self.get_balance()}')
        return True


    def withdraw(self, amount):
        '''
        
        :param:
        :return:
        '''
        if amount <= 0 or amount > self.__account_balance:
            # print(f'did NOT withdraw {amount} from {self.get_name()}, current balance = {self.get_balance()}')
            return False
        
        self.__account_balance -= amount
        # print(f'withdrew {amount} from {self.get_name()}, current balance = {self.get_balance()}')
        return True


    #defining getters
    def get_balance(self):
        return self.__account_balance
    

    def get_name(self):
        return self.__account_name
    
    #defining setters
    def set_balance(self, value):
        if value < 0:
            self.__account_balance = 0
        else:
            self.__account_balance = value
    

    def set_name(self, value):
        if isinstance(value, str):
            self.__account_name = value
            return True
        
        return False


    def __str__(self):
        return f'Account name = {self.__account_name}, Account balance = {self.__account_balance:.2f}'





class SavingAccount(Account):
    __MINIMUM = 100
    __RATE = 0.02

    def __init__(self,name):
        super().__init__(name, SavingAccount.__MINIMUM)
        self.__deposit_count = 0


    def __str__(self):
        #example using getter functions
        # return f'SAVING ACCOUNT: Account name = {self.get_name()}, Account balance = {self.get_balance():.2f}'

        #example using super()
        return f'SAVING ACCOUNT: {super().__str__()}'



    def withdraw(self, amount):
        '''
        Method withdraws from SavingAccount
        SavingAccount has minimum balance of $100

        :param amount: how much to withdraw (looking for int)
        :return: True if withdraw successful,, False if withdraw unsuccessful
        '''
        #b/c SavingAccount has to have at least $100
        if self.get_balance() - amount < SavingAccount.__MINIMUM:
            return False
        super().withdraw(amount) #remaining checks are in super().withdraw()



    def deposit(self, amount):
        '''
        Method makes deposit into SavingAccount
        every 5 deposits, interest method is applied

        :param amount: how much to deposit (looking for int)
        :return: True if deposit successful,, False if deposit unsuccessful
        '''
        if amount <= 0:
            # print(f'did NOT deposit {amount} for {self.get_name()}, current balance = {self.get_balance()}')
            return False
        
        self.__deposit_count += 1
        self.set_balance(self.get_balance() + amount)
        # print(f'did deposit {amount} for {self.get_name()}, current balance = {self.get_balance()}')


        if self.__deposit_count % 5 == 0:
            self.apply_interest()

        return True



    def apply_interest(self):
        '''
        
        
        :return:
        '''
        self.set_balance(self.get_balance() * (1 + SavingAccount.__RATE))

    def set_balance(self, value):
        '''
        
        :param:
        :return:
        '''
        if value < SavingAccount.__MINIMUM:
            value = SavingAccount.__MINIMUM
        super().set_balance(value)
        



class CheckingAccount(Account):
    __MINIMUM = 0
    __RATE = 0.00

    def __init__(self,name):
        # super().__init__(name)
        pass


    