file = open(r'C:\Users\okanl\OneDrive\Documents\Python\student_grades.csv', mode='rt')
file_list = file.readlines()
file_list.pop(0)
print(file_list)
names = []
scores = []
grades = []
A = []
B = []
C = []
D = []
E = []
F = []
for line in file_list:
    print(line)
    val = (line.split(','))
    print(val)
    name = val[0].strip(' ')
    print(name)
    score = int(val[1].strip(' '))
    print(score)
    grade = val[2].strip('\n')
    print(grade)
    names.append(name)
    scores.append(score)
    grades.append(grade)

print(names)
print(grades)
print(scores)
for score in scores:
    if score >= 70:
        print('here')
        print(score)
        index_scoreA = int(scores.index(score))
        print(names[index_scoreA])
        A.append((names[index_scoreA], grades[index_scoreA], score))
for score in scores:
    if score >= 60 and score <= 70:
        print(score)
        index_scoreB = scores.index(score)
        print(names[index_scoreB])
        B.append((names[index_scoreB], grades[index_scoreB], score))
for score in scores:
    if score >= 50 and score <= 60:
        print(score)
        index_scoreC = scores.index(score)
        print(names[index_scoreC])
        C.append((names[index_scoreC], grades[index_scoreC], score))
for score in scores:
    if score >= 45 and score <= 50:
        print(score)
        index_scoreD = scores.index(score)
        print(names[index_scoreD])
        D.append((names[index_scoreD], grades[index_scoreD], score))
for score in scores:
    if score >= 40 and score <= 45:
        print(score)
        index_scoreE = scores.index(score)
        print(names[index_scoreE])
        E.append((names[index_scoreE], grades[index_scoreE], score))
for score in scores:
    if score <= 40:
        print(score)
        index_scoreF = scores.index(score)
        print(names[index_scoreF])
        F.append((names[index_scoreF], grades[index_scoreF], score))

print('This is grade A', A) 
print('-' * 100)
print('This is grade B', B) 
print('-' * 100)
print('This is grade C', C)
print('-' * 100) 
print('This is grade D', D) 
print('-' * 100)
print('This is grade E', E) 
print('-' * 100)
print('This is grade F', F) 
print('-' * 100)
