class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def print(self):
        print(f'({self.x},{self.y})')
        
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def scale(self, s):
        self.x, self.y = self.x * s, self.y * s
        return (self.x , self.y)
        
    def rotate_xaxis(self):
        self.x = -self.x
        return self.x
    
    def rotate_yaxis(self):
        self.y = -self.y
        return self.y
        
    def add(self, P):
        result = Vector(0, 0)
        result.x, result.y = self.x + P.x, self.y + P.y
        return result
        
        






vector1 = Vector(34, 56)
vector1.print()
print(vector1.magnitude())
print(vector1.scale(5))
print(vector1.rotate_xaxis())
print(vector1.rotate_yaxis())
