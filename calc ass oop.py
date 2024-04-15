class Calculator:
    def __init__(self):
        self.calc_name = 'Casio'
        # self.home()
        
    def home(self):
        print('Welcome to', self.calc_name)
        try:
            self.val1 = float(input('First value: '))
            self.val2 = float(input('Second value: '))
        except Exception as e:
            print(e)
            self.decide()
        user = input('''
            Choose your operation:
              1. Addition
              2. Subtraction
              3. Multiply
              4. Divide         
              #. Exit
            Option: ''')
        if user == '1':
            self.addition()
        elif user == '2':
            self.subtraction()
        elif user == '3':
            self.multiplication()
        elif user == '4':
            self.division()
        elif user == '#':
            exit()
        else:
            print('Invalid function. Try again')
            self.home()

    def addition(self):
        print(f'Answer =  {self.val1 + self.val2}')
        self.decide()
    def subtraction(self):
        print(f'Answer = ', self.val1 - self.val2)
        self.decide()
    def multiplication(self):
        print(f'Answer =  {self.val1 * self.val2}')
        self.decide()
    def division(self):
        try:
            print(f'Answer = ', self.val1 / self.val2)
        except Exception as e:
            print(e)
            self.decide()
    def decide(self):
        user = input('Press 1 to go to home or # to exit')
        if user == '1':
            self.home()
        else:
            exit()

mycalc = Calculator() # casio is the object, calculator is the class
# print(mycalc.calc_name)
mycalc.home()
  