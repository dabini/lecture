def q2(number):
    res = 1
    for n in str(number):
        res *= int(n)
    return res

print(q2(123))
print(q2(2020))
print(q2(123456789))