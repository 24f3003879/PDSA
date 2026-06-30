#class of statement, marks
#print statement
# update marks

class Question:
    def __init__(self, statement, marks):
        self.statement = statement
        self.marks = marks
        
    def print_statement(self):
        print(self.statement)
        
    def update_marks(self, marks):
        self.marks = marks
        
        
class NAT(Question):
    def __init__(self, statement, marks, answer):
        super().__init__(statement, marks)
        self.answer = answer
    def update_marks(self, marks):
        return super().update_marks(marks)
    
    def update_answer(self, answer):
        self.answer = answer
        

q_nat = NAT('What is 1 + 1?', 1, 2)
q_nat.update_marks(4)
print(q_nat.marks)
