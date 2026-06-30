class students:
    counter = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        students.counter += 1
    
    def marksUpdate(self, marks):
        self.marks = marks
    
    def printDetails(self):
        print(f'{self.name}:{self.marks}')
        
        
        
madhavan = students('Madhavan', 90)
print('Number of students in the program =', students.counter)
andrew = students('Andrew', 85)
print('Number of students in the program =', students.counter)
usha = students('Usha', 95)
print('Number of students in the program =', students.counter)