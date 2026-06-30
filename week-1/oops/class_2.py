class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
           
    def update_marks(self, marks):
        self.marks = marks
        
    def print_details(self):
        print(f'{self.name}, {self.marks}')
        
anish = Student("Anish", 67)
print(anish.name)
print(anish.marks)
anish.update_marks(98)
print(anish.marks)