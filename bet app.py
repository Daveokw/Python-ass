myset = {'mango', 'apple', 'pineapple', 'grape'}
print(myset)
balance = 500
stake = float(input('Stake: '))

while balance > 0 and balance > stake: 
   guess = input('Guess the chosen fruit: ').strip().lower()
   chosen_fruit = myset.pop()
   myset.add(chosen_fruit)
   # print(chosen_fruit)
   if guess == chosen_fruit:
      balance += 2 * stake
      print('You guessed right.\nYour current balance is ', balance)
   else:
      balance -= stake
      print('Wrong\nYour current balance is ', balance)
   user = input('Press 1 to replay or # to exit: ')
   if user == '#':
      break
else: 
   print('Insufficient fund. Go and deposit')
print('Your cashout price is ', balance)
