
print("Press enter to start the test or '1' to exit")
pers = input('')
if pers == '1':
    exit()
else: 
       numbers = [ x for x in range(1, 21)]
user = int(input('How many students are taking the test: '))
student_list = [input(f'Name of student {student + 1}: ') for student in range(user)]
student_scores = []
score_list = []
for each_student in student_list: 
    print(f'\n{each_student},  its time for your test\n')
    score = 0
    questions = ['''1. What is the capital city of Nigeria?
                         a. Ibadan
                         b. Lagos
                         c. Abuja
                         d. Kano''',
                         '''2. ______ programming language is a high level programming language?
                         a. Python
                         b. Assembly
                         c. Snake
                         d. C+++''',
                         '''3. What is the additon of 5 and 7?
                         a. 11
                         b. 12
                         c. 17
                         d. 19.''',
                         '''4. Is Python an object-orientented programming language?
                         a. True
                         b. False''',
                         '''5. Who invented the Python programming language?
                         a. Python Patrick
                         b. Van Ross
                         c. Guido van Rossum
                         d. Michael Jack''',
                         '''6. What year was the Python programming language invented?
                         a. 1978
                         b. 1990
                         c. 1987
                         d. 1991''',
                         ]            
    answers = ['c', 'a', 'b', 'a', 'c', 'd']
    for question, answer in zip(questions, answers):
        print(question)
        user_ans = input('Answer: ').strip().lower()
        
        if user_ans == answer: 
            print('Correct')
            score +=5
        else:
           print('Incorrect')
            
    print(f'Thanks for taking the test, your total score is {score}')
    score_list.append(score)
print(student_list)
print(score_list)
maximum = max(score_list)
print(maximum)
minimum = min(score_list)
print(minimum)
index_max = score.index(max(score))
print(student_list[index_max])
index_min = score.index(min(score))
print(student_list[index_min])

