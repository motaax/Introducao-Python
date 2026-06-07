def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

print(mdc(12, 8))   
print(mdc(20, 15))  
print(mdc(48, 18))  