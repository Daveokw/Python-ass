import mysql.connector as sql 
from datetime import datetime

# Create the Customer_Database and transaction_history databases
try:
    mycon = sql.connect(host='localhost', user='root', password='')
    mycursor = mycon.cursor()
    mycon.autocommit = True

    mycursor.execute('CREATE DATABASE IF NOT EXISTS Customer_Database')
    print("Database 'Customer_Database' created successfully.")
except sql.Error as err:
    print(f"Error: {err}")

try:
    mycon = sql.connect(host='localhost', user='root', password='')
    mycursor = mycon.cursor()
    mycon.autocommit = True

    mycursor.execute('CREATE DATABASE IF NOT EXISTS transaction_history')
    print("Database 'transaction_history' created successfully.")
except sql.Error as err:
    print(f"Error: {err}")


class BankApp:
    def __init__(self):
        self.balance = 0
        self.transact = []
        self.cust_db = {}
        self.Customer_Database()
        self.home()

    def home(self):
        self.user = input('''Welcome to DAVE bank
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
        if self.email in self.cust_db and self.cust_db[self.email] == self.password:
            self.option()
        else:
            print('Email or Password Incorrect!')
            self.home()
    
    def SignUp(self):
        self.email = input('Email: ')
        self.password = input('Password: ')
        self.account_no = int(input('Account number: '))
        self.cust_db[self.email] = self.password
        print(self.cust_db)
        self.InsertCustomerData()
        self.home()

    def Customer_Database(self):
        try:
            mycon = sql.connect(host = 'localhost', user = 'root', password = '', database = 'Customer_Database')
            mycursor = mycon.cursor()
            mycon.autocommit = True

            mycursor.execute('USE Customer_Database')
            mycursor.execute('CREATE TABLE IF NOT EXISTS Customer_Table (id INT(4) PRIMARY KEY AUTO_INCREMENT, email VARCHAR(50), password VARCHAR(255), account_no FLOAT(10))')
            print("Customer_Table created successfully.")
        except sql.Error as err: 
            print(f"Error: {err}")   

    def InsertCustomerData(self): 
        try: 
            mycon = sql.connect(host='localhost', user='root', password='', database='Customer_Database') 
            mycursor = mycon.cursor() 
            mycon.autocommit = True 
            query = 'INSERT INTO Customer_Table (email, password, account_no) VALUES (%s, %s, %s)' 
            values = (self.email, self.password, self.account_no) 
            mycursor.execute(query, values) 
            print("Customer data inserted successfully.") 
        except sql.Error as err: 
            print(f"Error: {err}")

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
    
    def Deduct(self, amount): 
        self.balance -= amount

    def Deposit(self):
        self.amount = int(input('How much do you want to deposit: '))
        self.balance += self.amount
        #self.u = print(self.amount, 'has been deposited')
        self.action = 'deposit of funds:'
        self.transaction = self.amount
        self.AddTransactionHistory()
        print(f'{self.amount} has been deposited.')
        self.decision()

    def Withdraw(self):
        if self.balance > 0:
            self.money = int(input('How much do you want to withdraw: '))
            self.Deduct(self.money)
            #self.u = print(self.money, 'has been withdrawn')
            self.action = 'withrawal of funds:'
            self.transaction = self.money
            self.AddTransactionHistory()
            print(f'{self.money} has been withdrawn.')

        else:
            print('Insufficient Balance!')
        self.decision()

    def Transfer(self):
        if self.balance > 0:
            bank = input("Enter sender's bank: ")
            account_number = input("Enter sender's account number: ")
            self.send = int(input('How much do you want to transfer: '))
            self.Deduct(self.send)
            self.action = f'transfer of funds to {bank}'
            self.transaction = self.send
            self.AddTransactionHistory()
            print(f'{self.send} has been transferred to {bank}.')
        else:
            print('Insufficient Balance!')
        self.decision()

    def BuyAirtime(self):
        if self.balance > 0:
            network = input('Enter network:')
            phone_number = input('Enter phone number: ')
            self.talktime = int(input('How much airtime do you want to buy: '))
            self.Deduct(self.talktime)
            self.action = f'purchase of airtime for {phone_number}'
            self.transaction = self.talktime
            self.AddTransactionHistory()
            print(f'{self.talktime} has been recharged.')
        else:
            print('Insufficient Balance!')
        self.decision()

    def PayBills(self):
        if self.balance > 0:
            bill_type = input('Enter bill type: ')
            self.bill_amount = int(input('How bill amount: '))
            self.Deduct(self.bill_amount)
            self.action = f'payment of bills for {bill_type}'
            self.transaction = self.bill_amount
            self.AddTransactionHistory()
            print(f'{self.bill_amount} has been paid for {bill_type} bill.')
        else:
            print('Insufficient Balance!')
        self.decision()

    def AddTransactionHistory(self):
        try:
            mycon = sql.connect(host = 'localhost', user = 'root', password = '', database = 'transaction_history') #create database
            mycursor = mycon.cursor()
            mycon.autocommit = True

            #mycursor.execute('CREATE DATABASE IF NOT EXISTS transaction_history')
            mycursor.execute('USE transaction_history')
            mycursor.execute('CREATE TABLE IF NOT EXISTS transaction_table ( id INT(4) PRIMARY KEY AUTO_INCREMENT, transaction VARCHAR(25), amount FLOAT(10), date DATETIME DEFAULT CURRENT_TIMESTAMP)')
            # mycursor.execute('SHOW DATABASES')
            # print(mycursor)
            # for db in mycursor:
            #     print (db)

            # mycursor.execute(
                #     'CREATE TABLE transaction_table(id INT(4) PRIMARY KEY AUTO_INCREMENT, transaction VARCHAR(25),  amount FLOAT(10), date DATETIME DEFAULT CURRENT_TIMESTAMP)'
                # )
            current_date = datetime.now()
            query = 'INSERT INTO transaction_table(transaction, amount, date) VALUES (%s, %s, %s)'
            values = (self.action, self.transaction, current_date)

            mycursor.execute(query, values)
            print(mycursor)
        except sql.Error as err: print(f"Error: {err}")

    def TransactionHistory(self):
        try:
            mycon = sql.connect(host = 'localhost', user = 'root', password = '', database = 'transaction_history') #create database
            mycursor = mycon.cursor()
            mycon.autocommit = True
            mycursor.execute('SELECT * FROM transaction_table')
            details = mycursor.fetchall()
            for x in details:
                print (x) 
            self.decision()
        except sql.Error as err: print(f"Error: {err}")


    def decision(self):
        self.user = input('Press 1 for more options or # to exit ')
        if self.user == '1':
            self.option()
        else:
            exit

bankapp = BankApp()






