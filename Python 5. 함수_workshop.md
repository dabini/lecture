# 5. Python_Workshop



> Background
>
> 	- 모듈
> 	- 에러 및 예외 처리



> Goal
>
> 	- 모듈에 추가하여 코드를 작성하기
> 	- Python에서 발생할 수 있는 다양한 에러에 대한 이해



## Problem

### 1. 2개의 숫자를 인자로 받아 더하기, 빼기, 곱하기, 나누기 연산의 결과를 반환하는 4개의 함수를 calc.py에 작성하시오. 단, 나누기 연산에서는 try except 구문을 사용하여 '0'으로 나누려고 하는 경우에는 문자열 '0'으로는 나눌 수  없습니다.'를 반환하시오



```python
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
```



### 2. 1번에서 작성한 calc.py 모듈을 import하여, 각 연산을 수행하는 함수들을 실행하는 코드를 작성하시오.

```python
from calc import *

print(plus(3, 5))
print(minus(7, 1))
print(multi(4, 5))
print(divide(20, 5))
print(divide(20, 0))
```

