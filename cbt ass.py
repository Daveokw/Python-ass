count = 0
user = input('Name: ')
user = input('Exam Number: ')
user = input('Press Enter to start test: ')

print('''1. What is the capital city of Nigeria?
        a. Ibadan
        b. Lagos
        c. Abuja
        d. Kano
        ''')
user =input('Answer: ')
if user == 'c':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('''2. ______ programming language is a high level programming language?
        a. Python
        b. Assembly
        c. Snake
        d. C+++
        ''')
user =input('Answer: ')
if user == 'a':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('''3. What is the additon of 5 and 7?
        a. 11
        b. 12
        c. 17
        d. 19
        ''')
user =input('Answer: ')
if user == 'b':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('''4. Is Python an object-orientented programming language?
        a. True
        b. False
        ''')
user =input('Answer: ')
if user == 'a':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('''5. Who invented the Python programming language?
        a. Python Patrick
        b. Van Ross
        c. Guido van Rossum
        d. Michael Jack
        ''')
user =input('Answer: ')
if user == 'c':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('''6. What year was the Python programming language invented?
        a. 1978
        b. 1990
        c. 1987
        d. 1991
        ''')
user =input('Answer: ')
if user == 'd':
    print('Correct')
    count += 5 
else:
    print('Incorrect')

print('Total count = ', count)
