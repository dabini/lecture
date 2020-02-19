def plus(a, b):
    res = a + b
    return res

def minus(a, b):
    res = a - b
    return res

def multi(a, b):
    res = a * b
    return res

def divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("'0'으로는 나눌 수 없습니다.")
    else:
        return res