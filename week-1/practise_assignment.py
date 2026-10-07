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

def f(n):
    s = 0
    for i in range(2, n):
        if n % i == 0 and i % 2 == 1:
            s = s + 1
    return (s)

print(f(60) - f(59))

