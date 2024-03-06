class Ussd:
    def __init__(self):
        self.ussd_name = 'My USSD App'

    def home(self):
        print(f'''Welcome to {self.ussd_name}
          1. Data Plan
          2. Check Balance
          3. Buy Airtime 
          0. Exit''')
        user = input('Choice: ')
        if user == '1':
            self.data_plan()
        elif user == '2':
            self.check_balance()
        elif user == '3':
            self.buy_airtime()
        elif user == '0':
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please try again')

    def data_plan(self):
        print('''
            Data Plan
            1. Daily
            2. Weekly
            3. Monthly
            4. Others (2-3 Months)  
            ''')
        user = input('Choice: ')
        if user == '1':
            print('Daily Plans')
            self.daily()
        elif user == '2':
            print('Weekly Plans')
            self.weekly()
        elif user == '3':
            print('Monthly Plans')
            self.monthly()
        elif user == '4':
            print('Others (2-3 Months)')
            self.others()

    def daily(self):
        print('''
            1. 100mb for #50 for 1 day
            2. 200mb for #100 for 1 day
            3. 500mb for #300 for 1 day''')
        user = input('Choice: ')
        if user == '1':
            print('You have been credited with 100mb!')
            self.decide()
        elif user == '2':
            print('You have been credited with 200mb!')
            self.decide()
        elif user == '3':
            print('You have been credited with 500mb!')
            self.decide()
    def weekly(self):
        print('''
            1. 1gb for #100 for 7 days
            2. 2gb for #200 for 7 days
            3. 5gb for #500 for 7 days''')
        user = input('Choice: ')
        if user == '1':
            print('You have been credited with 1gb!')
            self.decide()
        elif user == '2':
            print('You have been credited with 2gb!')
            self.decide()
        elif user == '3':
            print('You have been credited with 5gb!')
            self.decide()
    def monthly(self):
        print('''
            1. 10gb for #1000 for 30days
            2. 20gb for #2000 for 30 days
            3. 50gb for #5000 for 30 days''')
        user = input('Choice: ')
        if user == '1':
            print('You have been credited with 10gb!')
            self.decide()
        elif user == '2':
            print('You have been credited with 20gb!')
            self.decide()
        elif user == '3':
            print('You have been credited with 50gb!')
            self.decide()
    def others(self):
        print('''
            1. 100gb for #10000 for 2 months
            2. 200gb for #20000 for 5 months
            3. 500gb for #50000 for 12 months''')
        user = input('Choice: ')
        if user == '1':
            print('You have been credited with 100gb!')
            self.decide()
        elif user == '2':
            print('You have been credited with 200gb!')
            self.decide()
        elif user == '3':
            print('You have been credited with 500gb!')
            self.decide()
    def decide(self):
        user = input('Press 0 to go to home or # to exit')
        if user == '0':
            self.home()
        else:
            exit()

    def check_balance(self):
        print('Your balance is #500')
        self.decide()
    def buy_airtime(self):
        user = input('Enter amount to buy: ')
        print(f'Airtime of {user} has been successfully recharged!')
        self.decide()

myussd = Ussd()
myussd.home()


