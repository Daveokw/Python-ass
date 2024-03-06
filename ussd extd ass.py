def display_menu():
    print('''
          Welcome to my USSD App
          1. Data Plan
          2. Check Balance
          3. Buy Airtime 
          0. Exit''')
def data_plan():
    print('''
            Data Plan
            1. Daily
            2. Weekly
            3. Monthly
            4. 2-3 Months  
            ''')
    user = input('Choice: ')
    if user == '1':
        print('Daily Plans')
    elif user == '2':
        print('Weekly Plans')
    elif user == '3':
        print('Monthly Plans')
    elif user == '4':
        print('2-3 Months')
def check_balance():
    print('Your balance is #500')

def buy_airtime():
    user = input('Enter amount to buy: ')
    print(f'Airtime of {user} has been successfully recharged!')

while True:
    display_menu()
    option = input('Enter option: ')
    if option == '1':
        data_plan()
    elif option == '2':
        check_balance()
    elif option == '3':
        buy_airtime()
    elif option == '0':
        print('Exiting...')
        break
    else:
        print('Invalid option. Please try again')
    
