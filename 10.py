class student:
    def read(self):
        self.name = input('Enter name:')
        self.roll = int(input('Enter roll number:'))
        self.branch = input('Enter branch:')
    def display(self):
        print(f'student name:{self.name}')
        print(f'student roll:{self.roll}')
        print(f'student branch:{self.branch}')
    
s = student()
s.read()
s.display()