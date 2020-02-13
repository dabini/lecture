# 문자열(String)

### 문자의 표현



- ASCII
- 유니코드
- big-endian, little-endian



## 문자열

- 문자열의 분류

![image-20200213132914946](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200213132914946.png)

- python에서의 문자열 처리
  - 문자열은 시퀀스 자료형으로 분류되고, 인덱싱 슬라이싱 연산이 가능
  - 문자열 클래스에서 제공되는 메소드
    - replace(), split(), isalpha(), find()
  - 문자열은 튜플과 같이 요소값을 변경할 수 없음



#### 문자열 뒤집기

```python
#문자열뒤집기
#내 CODE
Data = list(input())
new = ""
for i in range(len(Data)):
    new += Data[-(i+1)]
print(new)


#연습문제1
s = "Reverse this string"
s = s[::-1]
print(s)
```



## 패턴 매칭



- 패턴 매칭에 사용되는 알고리즘들
  - 고지식한 패턴 검색 알고리즘
  - 카프-라빈 알고리즘
  - KMP 알고리즘
  - 보이어-무어 알고리즘



#### 고지식한 알고리즘(Brute Force)

- 본문 문자열을 처음부터 끝까지 차례대로 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식으로 동작





## 문자열 암호화

## 문자열 압축

