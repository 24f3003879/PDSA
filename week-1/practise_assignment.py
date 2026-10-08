#q-1

# def fun(s):
#     p = 0
#     S = s.lower()
#     for i in range(len(S)):
#         if S[i] not in S[:i]:
#             p += 1
#     return p 

# print(fun("Goodoooo"))



#q-3

# def f(n):
#     s = 0
#     for i in range(2, n):
#         if n % i == 0 and i % 2 == 1:
#             s = s + 1
#     return (s)

# print(f(60) - f(59))

#q-4


# x = 1
# while True:
#     if x % 5 = = 0:
#         break
#     print(x, end = ' ')
#     x + = 1


#q-5

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def say_hi(self):
#         print("Hello,", self.name)

# p = Person("Good Morning")
# p.say_hi()


#q-6

# a = [1, 2, 3]
# try:
#     print("Second Element = %d" %(a[1]))
#     print("Second Element = %d" %(a[4]))
# except:
#     print("An error occurred")


#q-7

# L = [44, 6, 36]

# def special3Bad(L):
#     try:
#         if L[0] % L[1] == 0 and L[1] != 0:
#             if L[0] / (L[1] ** 2 - L[2]) == 0:
#                 return True
#             return False
#     except ZeroDivisionError:
#         print ("ZeroDivisionError")
#     except:
#         print("Some other exception occurred")
#     else:
#         print("No exception occurred")
# special3Bad(L)

#q-8


# L = [2, 4, 6]

# def isSymmetricBad(L):
#     try:
#         while len(L) > 0:
#             if L.pop(0) != L.pop(-1):
#                 return False
#         return True
#     except IndexError:
#         print("IndexError")
#     except:
#         print("Some other exception occurred")
#     else:
#         print("No exception occurred")
# isSymmetricBad(L)


#q-9

# count = 0
# def gcd(m,n):
#     global count
#     count += 1
    
#     (a, b) = (max(m, n)), (min(m, n))
    
#     if a % b == 0:
#         return (b)
#     else:
#         return(gcd(b, a % b))

        

# print(gcd(24, 130))
# print(count)


#q-10

# class Enrollment:
#     count = 0
#     def __init__(self, n, c):
#         self.name = n
#         self.course = c
#         Enrollment.count += 1
#     def display(self):
#         print(self.name)
#         print(self.course)


#q-11

def fun(n):
    if n == 0:
        return 0
    return (n % 10) + fun(n // 100)



print(123 // 100)


    
