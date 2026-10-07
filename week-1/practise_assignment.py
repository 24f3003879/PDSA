#q-1

def fun(s):
    p = 0
    S = s.lower()
    for i in range(len(S)):
        if S[i] not in S[:i]:
            p += 1
    return p 

print(fun("Goodoooo"))
