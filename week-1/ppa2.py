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

    def Side_Classification(self):
        if self.Is_valid() == "Valid":
            if self.a == self.b == self.c:
                return ("Equilateral")
            elif self.a == self.b != self.c or self.b == self.c != self.a or self.c == self.a != self.b:
                return ("Isosceles")
            elif self.a != self.b and self.b != self.c and self.a != self.c:
                return ("Scalene")
        else:
            return ("Invalid")
    def Angle_Classification(self):
        if self.Is_valid() == "Valid":
            if self.a**2 + self.b**2 > self.c**2:
                return ("Acute")
            elif self.a**2 + self.b**2 == self.c**2:
                return ("Right")
            elif self.a**2 + self.b**2 < self.c**2:
                return("Obtuse")

        else:
            return ("Invalid")

    def Area(self):
        if self.Is_valid() == "Valid":
            s = (self.a + self.b + self.c)/2

            return ((s*(s - self.a)*(s - self.b)*(s - self.c))**0.5)


        else:
            return("Invalid")






t = Triangle(45, 6, 89)
t1 = Triangle(2, 3, 4)
print(t.Area())
print(t1.Area())
print(t.Is_valid())
print(t1.Is_valid())
print(t.a)
print(t.b)
print(t.c)



    