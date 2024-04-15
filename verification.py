students = [
   ('Dave Temi', 'full'),
   ('Adebisi Precious', 'full'),
   ('Salim Quadri', 'part'),
   ('Tunde Remi', 'part'),
   ('John Ade', 'nil'),
   ('Adeolu James', 'part'),
   ('Olumide Bimpe', 'full')
        ]

staff = [
   ('Moses Simon', '01'),
   ('Adeoye Mercy', '02'),
   ('Oladokun Victory', '03'),
   ('Flair Rick', '04')
]

user = input('''WELCOME TO SQI COLLEGE OF ICT.
      Choose an option below to verify your identity:
      A. Staff
      B. Student
      C. Visitor
    Option: '''
)

if user.strip().capitalize() == 'A':
        staff_id = input('ID: ')
        staff_name = input('First Name: ').strip().capitalize

        fnames = []
        IDs = []

        for name, id in staff:
              fnames.append(name)
              IDs.append(id)
        
        if staff_name in fnames and staff_id in IDs :
            print('Access Granted👍. You can go in')
        else:
            print('Access Denied!')
            
if user.strip().capitalize() == 'C':
   print('You can proceed to the front desk')
   
elif user.strip().capitalize() == 'B':
   print('Welcome to School. Input your name to verify your eligibility: \n')
   student = input('Your Name: ').strip().capitalize()
   # print(student)
   Students =[]
   PaymentStatus=[]

   for name,payment in students:
      Students.append(name)
      PaymentStatus.append(payment)
   # print(Students)
   
   if student in Students:
      print(f'\n Welcome {student}, kindly wait to verify your payment status\n')
   
      _index = Students.index(student)
      _status = PaymentStatus[_index]

      if _status == 'full':
         print(f'{student}, you have made full payment, you can go in')
      elif _status == 'part':
         print(f'{student}, you have made half payment, pay up very soon to preserve your studentship')
      elif _status == 'nil':
         print(f'You are not eligible to go in')
         
   else:
      print('Your name is not registered')
