class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return ("Valid")
        else:
            return ("Invalid")

t = Triangle(45, 6, 89)
t1 = Triangle(2, 3, 4)
print(t.Is_valid())
print(t1.Is_valid())
print(t.a)
print(t.b)
print(t.c)



    