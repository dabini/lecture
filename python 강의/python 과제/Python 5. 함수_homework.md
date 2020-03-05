# 5. Python



> 학습해야 할 내용
>
> 	- 모듈
> 	- 에러 및 예외 처리



```python
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)
```



### 1. 위와 같은 코드가 fibo.py 파일에 작성되어 있을 때, 아래와 같이 함수를 실행할 수 있도록 하는 import 구문을 채워 넣어 완성하시오

```python
from fibo import fibo_recursion as recursion
recursion(4)
```



### 2. 다음 에러들이 어떠한 경우에 발생하는지 간단하게 작성하시오.

- ZeroDivisionError 
  - 0으로 나눌 때 에러 발생
- NameError  
  - 지역 혹은 전역 이름 공간 내에서 유효하지 않는 이름, 즉 정의되지 않은 변수를 호출했을 때 에러 발생
- TypeError 
  - 자료형에 대한 타입이 잘못 되었을 때 에러 발생
-  IndexError 
  - 자료형에서 없는 인덱스를 불렀을 때 에러 발생
-  KeyError 
  - 딕셔너리 자료형에 존재하지 않는 key를 입력했을 때 발생
-  ModuleNotFoundError 
  - 없는 모듈을 입력했을 때 에러 발생
-  ImportError
  - 모듈은 있으나 잘못된 클래스나 메소드를 불러올 때 에러 발생