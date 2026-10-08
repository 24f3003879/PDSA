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

L = [44, 6, 36]

def special3Bad(L):
    try:
        if L[0] % L[1] == 0 and L[1] != 0:
            if L[0] / (L[1] ** 2 - L[2]) == 0:
                return True
            return False
    except ZeroDivisionError:
        print ("ZeroDivisionError")
    except:
        print("Some other exception occurred")
    else:
        print("No exception occurred")
special3Bad(L)


