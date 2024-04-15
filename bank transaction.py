class BankApp:
    def __init__(self):
        self.balance = 0
        self.transact = []
        self.cust_db = {}
        self.home()

    def home(self):
        self.user = input('''Welcome to UBA
            1. Sign Up
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

        if self.email == self.password:
            self.option()
        else:
            print('Email or Password Incorrect!')
            self.home()

    def SignUp(self):
        x = 0
        self.email = input(f'Email: ')
        self.password = input(f'Password: ')
        self.cust_db[self.email] = self.password
        print(self.cust_db)

    def Customer_Database(self):
        import mysql.connector as sql
        mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'Customer_Database') #create database
        mycursor = mycon.cursor()
        mycon.autocommit = True

        mycursor.execute('CREATE DATABASE Customer_Database')

        mycursor.execute('CREATE TABLE Customer_Table (id INT(4) PRIMARY KEY AUTO_INCREMENT, email VARCHAR(25), password VARCHAR(25), account no FLOAT(10))')

        query = 'INSERT INTO Customer_table(email, password, account no) VALUES (%s, %s, %s)'
        values = (self.email, self.password, self.account_no)

        mycursor.execute(query, values)
        print(mycursor)
        
    def option(self):
        self.choice = input('''
            Which transaction do you want to perform?
            1. Check balance
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
        # self.deduction = self.amount
        # self.transact.append(self.action)
        # self.transact.append(self.deduction)

    def Deposit(self):
        self.amount = int(input('How much do you want to deposit: '))
        self.balance = self.balance + self.amount
        self.action = 'deposit'
        self.transaction = self.amount
        self.AddTransactionHistory()
        self.decision()

    def Withdraw(self):
        if self.balance > 0:
            self.money = int(input('How much do you want to withraw: '))
            self.Deduct()
            self.action = 'withdraw'
            self.transaction = self.money
            self.AddTransactionHistory()
        else:
            print('Insufficient Balance!')
        self.decision()

    def Transfer(self):
        if self.balance > 0:
            bank = input("Enter sender's bank: ")
            account_number = input("Enter sender's account number: ")
            self.send = int(input('How much do you want to transfer: '))
            self.Deduct()
            self.transaction = self.send
            self.AddTransactionHistory()
        else:
            print('Insufficient Balance!')
        self.decision()

    def BuyAirtime(self):
        if self.balance > 0:
            network = input('Enter network:')
            phone_number = input('Enter phone number: ')
            self.talktime = int(input('How much airtime do you want to buy: '))
            self.Deduct()
            self.action = 'buy airtime'
            self.transaction = self.talktime
            self.AddTransactionHistory()
        else:
            print('Insufficient Balance!')
        self.decision()

    def PayBills(self):
        if self.balance > 0:
            network = input('Enter network:')
            phone_number = input('Enter phone number: ')
            self.talktime = int(input('How much airtime do you want to buy: '))
            self.Deduct()
            self.action = 'pay bills'
            self.transaction = self.nepabill
            self.AddTransactionHistory()
        else:
            print('Insufficient Balance!')
        self.decision()

    def AddTransactionHistory(self):
        import mysql.connector as sql
        mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'transaction_history') #create database
        mycursor = mycon.cursor()
        mycon.autocommit = True

        # mycursor.execute('CREATE DATABASE transaction_history')
        mycursor.execute('SHOW DATABASES')
        print(mycursor)
        for db in mycursor:
            print (db)

        # mycursor.execute(
            #     'CREATE TABLE transaction_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, transaction VARCHAR(25),  amount FLOAT(10), date DATETIME DEFAULT CURRENT_TIMESTAMP)'
            # )

        query = 'INSERT INTO transaction_table(transaction, amount, date) VALUES (%s, %s, %s)'
        values = (self.action, self.transaction)

        mycursor.execute(query, values)
        print(mycursor)

    def TransactionHistory(self):
        import mysql.connector as sql
        mycon = sql.connect(host = '127.0.0.1', user = 'root', password = '', database = 'transaction_history') #create database
        mycursor = mycon.cursor()
        mycon.autocommit = True
        mycursor.execute('SELECT * FROM transaction_history') 
        for x in mycursor:
            print (x)      
        details = mycursor.fetchall()
        print(details)

    def decision(self):
        self.user = input('Press 1 for more options or # to exit')
        if self.user == '1':
            self.option()
        else:
            exit

bankapp = BankApp()






