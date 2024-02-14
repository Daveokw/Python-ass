
user = input('USSD Code: ')

if user == '*312#':
    print('''
    1. Data Plan
    2. Check Balance
    3. Airtime
    '''
    )

    user = input('Choice: ')

    if user == '1':
        print('''
              Data Plan
            1. Daily
            2. Weekly
            3. Monthly
            4. 2-3 Months  
            ''')
        user = input('Choice: ')
        if user == '1':
            print('Daily')
        elif user == '2':
            print('Weekly')
        elif user == '3':
            print('Monthly')
        elif user == '4':
            print('2-3 Months')

    elif user == '2':
        print('Check Balance')

    elif user =='3':
        print('''
              Airtime
            1. #100 for #100
            2. #300 for #300
            3. #500 for #500
            '''
        )
        user = input('Choice: ')
        if user == '1':
            print('#100 for #100')
        elif user == '2':
            print('#300 for #300')
        elif user == '3':
            print('#500 for #500')
    else:
        print('Invalid command')

else:
    print('Invalid ussd code! ')

