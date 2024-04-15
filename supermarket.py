# Available food
# Avilable drinks
# Price
# Cond statement: what do you want to order
# check if the food is in the list 
# check if the drink is in the list
# print the price of the ordered food 
# print the price of the ordered drink
# print the total price
# food at no 1 or no 2 like a menu
# any approach
# ask if the customer wants to choose any other items
# print('''
# Thank you Mr Dami, your order are:
# 1.nike sneakers n200000
# 2. rolex n30000
# total n50000 
    # ''')
    # no 1 database
    # print to user 
    # ask order
    # ask if more product keep asking until the customer says no
    

# *add for loop for menu, print one by one
# use for loop for menu

food_menu = [('1. jollof', 600), 
             ('2. fried rice', 700), 
             ('3. indomie', 500)
             ]
drinks_menu = [('4. coke', 350), 
               ('5. bigi', 300), 
               ('6. bottle water', 250)
               ]
amount = 0
order_list = []
price_list =[]

print(food_menu)
user = input('what food do you want to order, jollof, or fried rice or indomie? ').strip().lower()
if user == 'jollof':
    print('jollof')
    amount += 600
elif user == 'fried rice':
    print('fried rice')
    amount += 700
elif user == 'indomie':
    print('indomie')
    amount += 500
else:
    exit()
print(amount)  

order_list.append(user)
price_list.append(amount)


buy_more = (input('Do you want to buy anything else yes, no?')).strip().lower()
while buy_more == 'yes':
    print(food_menu)
    user = input('what food do you want to order, jollof, or fried rice or indomie? ').strip().lower()
    if user == 'jollof':
        print('jollof')
        amount += 600
    elif user == 'fried rice':
        print('fried rice')
        amount += 700
    elif user == 'indomie':
        print('indomie')
        amount += 500
    else:
        exit()
    print(amount)
    
    buy_more = (input('Do you want to buy anything else yes, no?')).strip().lower()
    if buy_more == 'no':
        break

order_list.append(user)
price_list.append(amount)


print(drinks_menu)
user = input('what drink do you want to order, coke or bigi or bottle water? ').strip().lower()
if user == 'coke':
    print('coke')
    amount += 350
elif user == 'bigi':
    print('bigi')
    amount += 300
elif user == 'bottle water':
    print('bottle water')
    amount += 250
else:
    exit()

order_list.append(user)
price_list.append(amount)


buy_more = (input('Do you want to buy anything else yes, no?')).strip().lower()
while buy_more == 'yes':
    print(drinks_menu)
    user = input('what drink do you want to order, coke or bigi or bottle water? ').strip().lower()
    if user == 'coke':
        print('coke')
        amount += 350
    elif user == 'bigi':
        print('bigi')
        amount += 300
    elif user == 'bottle water':
        print('bottle water')
        amount += 250
    else:
        exit()
    print(amount)

    buy_more = (input('Do you want to buy anything else yes, no?')).strip().lower()
    if buy_more == 'no':
        break

order_list.append(user)
price_list.append(amount)

print(order_list) 
print(price_list) 


print(f'''
    Thank you Mr Dami, your order are:
    {order_list}--{price_list}
    Total: {amount}
    ''')


