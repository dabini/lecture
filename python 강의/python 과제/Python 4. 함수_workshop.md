# Python 4. 함수 2

>Background
>
>	- 제어문
>	- 함수

>Goal
>
>	- 조건문 및 반복문에 대한 이해
>	- 함수에 대한 이해



## Problem

- 양의 정수 x를 입력 받아 제곱근의 근사값을 반환하는 함수를 작성하세요.
- sqrt() 사용 금지



```python
def my_Sqrt(a):
    compare = 0.5*(1+(a))
    tmp = 0
    while True:
        tmp = compare
        compare = 0.5*(tmp+(a/tmp))

        if (tmp-compare < 0.000000000000000000000001 or tmp-compare < - 0.000000000000000000000001):
            break

    return tmp
print(my_Sqrt(2))
```

