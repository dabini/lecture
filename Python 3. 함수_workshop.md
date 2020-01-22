## Workshop


> Background
    - 제어문
    - 함수

>Goal
    - 조건문 및 반복문에 대한 이해
    - 함수에 대한 이해
 

### Problem

### Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.

### 단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요


```python
word = input()
def palindrome(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)
        
palindrome(word)
```

    토마토
    True
    
