class Cbt:
    def __init__(self):
        print("WELCOME!")
        self.name = input('Enter your full name: ')
        self.level = input('Enter your current level: ')
        self.details = [
        ('1. What is the capital city of Nigeria? a. Ibadan b. Lagos c. Abuja d. Kano', 'c'),
        ('2. ______ programming language is a high level programming language? a. Python b. Assembly c. Snake d. C+++', 'a'),
        ('3. What is the additon of 5 and 7? a. 11 b. 12 c. 17 d. 19', 'b'),
        ('4. Is Python an object-orientented programming language? a. True b. False', 'a'),
        ('5. Who invented the Python programming language? a. Python Patrick b. Van Ross c. Guido van Rossum d. Michael Jack', 'c'),
        ('6. What year was the Python programming language invented a. 1978 b. 1990 c. 1987 d. 1991', 'd')
        ]

    def questions(self):
        score = 0
        for ques, ans in self.details:
            print(ques)
            user = input('Answer: ').strip().lower()
            if user == ans:
                print('Correct\n')
                score += 10
            else:
                print('Wrong\n')
        print(f'You scored {score}')

school = Cbt()
school.questions()







    
   
































