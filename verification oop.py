import time

class Verification:
    def __init__(self):
        self.Students_db = [
            ('Dave Temi', 'full'),
            ('Adebisi Precious', 'full'),
            ('Salim Quadri', 'part'),
            ('Tunde Remi', 'part'),
            ('John Ade', 'nil'),
            ('Adeolu James', 'part'),
            ('Olumide Bimpe', 'full')
        ]
        self.mstaff = [
            ('Moses Simon', '01'),
            ('Adeoye Mercy', '02'),
            ('Oladokun Victory', '03'),
            ('Flair Rick', '04')
        ]

    def user(self):
        option = input('''WELCOME TO SQI COLLEGE OF ICT.
      Choose an option below to verify your identity:
      A. Staff
      B. Student
      C. Visitor
    Option: ''').strip().capitalize()
        
        if option == 'A':
            self.staff()
        elif option == 'B':
            self.student()
        elif option == 'C':
            self.visitor()
        else:
            print("Invalid option")

    def staff(self):
        staff_id = input('ID: ')
        staff_name = input('First Name: ').strip().title()

        fnames = []
        IDs = []

        for name, id in self.mstaff:
            fnames.append(name)
            IDs.append(id)

        print('Loading ...')
        time.sleep(3)
        if staff_name in fnames and staff_id in IDs:
            print('Access Granted👍. You can go in')
        else:
            print('Access Denied!')

    def student(self):
        print('Welcome to school. Input your name to verify your eligibility: \n')
        student_name = input('Your Name: ').strip().title()

        Students_dbName = []
        PaymentStatus = []

        for name, payment in self.Students_db:
            Students_dbName.append(name)
            PaymentStatus.append(payment)

        if student_name in Students_dbName:
            print(f'\n Welcome {student_name}, kindly wait to verify your payment status\n')
            print('Loading ...')
            time.sleep(3)
            _index = Students_dbName.index(student_name)
            _status = PaymentStatus[_index]

            if _status == 'full':
                print(f'{student_name}, you have made full payment, you can go in')
            elif _status == 'part':
                print(f'{student_name}, you have made half payment, pay up very soon to preserve your studentship')
            elif _status == 'nil':
                print(f'You are not eligible to go in')
        else:
            print('Your name is not registered')

    def visitor(self):
        print('You are welcome. Please proceed to the front desk')

sqi = Verification()
sqi.user()
