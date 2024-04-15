import pygame
import datetime as dt
import time

class ToDo:
    def __init__(self):
        self.tasks = []

    def home(self):
        print('Welcome to ToDo')
        self.choice = input('''
            1. Add Task
            2. Delete Task
            3. View Tasks 
            4. Exit 
            Option:   
        ''')

        if self.choice == '1':
            self.AddTask()
        elif self.choice == '2':
            self.DeleteTask()
        elif self.choice == '3':
            self.ViewTask()
        elif self.choice == '4':
            exit()
        else:
            print('Invalid Option')
    
    def AddTask(self):
        file = (r'C:\Users\okanl\OneDrive\Documents\Python\Kizz-Daniel-My-G-(JustNaija.com).mp3')
        x = input('''
            Input Task: 
            ''')
        self.tasks.append(x)
        alarmHour = int(input('Enter time as hour(1-12): '))
        alarmMin = int(input('Enter time as minute(0-59): '))
        alarmAm = input('Enter AM/PM: ').strip().capitalize()
        if alarmAm == 'PM':
            alarmHour += 12
        pygame.init()
        pygame.mixer.init()
        while True:
            if alarmHour == dt.datetime.now().hour and alarmMin == dt.datetime.now().minute:
                print("Its time to ", x)
                pygame.mixer.music.load(file)
                pygame.mixer.music.play()
                time.sleep(10)
                break

    def DeleteTask(self):
        self.ViewTask()
        y = int(input('Which task do you want to delete? '))
        self.tasks.pop(y)

    def ViewTask(self):
        print(self.tasks)


todo = ToDo()
todo.home()