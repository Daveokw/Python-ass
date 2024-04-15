class Bank:
    def __init__(self):
        self.balance = 0
        self.transact = []
        self.cust_db = {}
        self.home()
    def home(self):
        self.user = input('''Welcome to DAVE bank
        1. Sign up
        2. Sign in

        Option: ''')

        if self.user == '1':
            self.SignUp()
        elif self.user == '2':
            self.SignIn() 
        else:
            self.home()
    
    def SignIn(self):
        self.email = input('Email: ')
        self.password = input('Password: ')
        if self.email in self.cust_db and self.cust_db[self.email] == self.password:
            self.option()
        else:
            print('Email or Password Incorrect!')
            self.home()
    
    def SignUp(self):
        # x = 0
        self.email = input('Email: ')
        self.password = input('Password: ')
        self.cust_db[self.email] = self.password
        print(self.cust_db)
        self.home()

        # d = {}
        # size = int(input('Enter the size: '))
        # for i in range(size):
        #     key = input('Enter the name: ')
        #     value = input('Enter the number: ')
        #     d[key] = value

    def option(self):
        self.choice = input('''
            Which transaction do you want to perform?
            1. Check Balance
            2. Deposit
            3. Withdraw
            4. Transfer
            5. Buy airtime
            6. Pay bills
            7. Transaction history
            Option: ''')
        
        if self.choice == '1':
            self.CheckBalance()
        elif self.choice == '2':
            self.Deposit()
        elif self.choice == '3':
            self.Withdraw()
        elif self.choice == '4':
            self.Transfer()
        elif self.choice == '5':
            self.BuyAirtime()
        elif self.choice == '6':
            self.PayBills()
        elif self.choice == '7':
            self.TransactionHistory()
        else:
            print('Choose a transaction')
    
    def CheckBalance(self):
        print('Your balance is', self.balance)
        self.decision()
    
    def Deduct(self):
        self.balance = self.balance - self.money
        self.deduction = self.amount
        self.transact.append(self.action)
        self.transact.append(self.deduction)
    
    def Deposit(self):
        self.amount = int(input('How much do you want to deposit: '))
        self.balance = self.balance + self.amount
        self.action = 'deposit'
        self.deduction = self.amount
        self.transact.append(self.deduction)
        self.decision()
    
    def Withdraw(self):
        if self.balance > 0:
            self.money = int(input('How much do you want to wothdraw: '))
            self.Deduct()
            self.action = 'withdraw'
            self.transact.append(self.action)
        else:
            print('Insufficient Balance!')
        self.decision()

    def Transfer(self):
        if self.balance > 0:
            bank = input("Enter sender's bank: ")
            account_number = input("Enter sender's account number: ")
            self.send = int(input('How much do you want to transfer?: '))
            self.Deduct()
            self.action = 'transfer'
            self.transact.append(self.action)
        else:
            print('Insufficient Balance!')
        self.decision()

    def BuyAirtime(self):
        if self.balance > 0:
            network = input('Enter network: ')
            phone_number = input('Enter phone number: ')
            self.talktime = int(input('How much airtime do you want to buy: '))
            self.Deduct()
            self.action = 'buy airtime'
            self.transact.append(self.action)
        else:
            print('Insufficient Balance!')
        self.decision()
    
    def PayBills(self):
        if self.balance > 0:
            network = input('Enter network: ')
            phone_number = input('Enter phone number: ')
            self.talktime = int(input('How much airtime do you want to buy: '))
            self.Deduct()
            self.action = 'pay bills'
            self.transact.append(self.action)
        else:
            print('Insufficient Balance!')
        self.decision()
    
    def TransactionHistory(self):
        print(self.transact)
        self.decision()

    def decision(self):
        self.user = input('Press 1 for more options or # to exit')
        if self.user == '1':
            self.option()
        else:
            exit()

bank = Bank()
# bank.home()

