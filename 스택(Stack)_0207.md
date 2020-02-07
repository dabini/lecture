# 스택(Stack)

> 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
>
> 스택에 저장된 자료 구조는 선형구조를 갖는다
>
> > 선형구조: 자료간의 관계가 1대 1관계를 갖는다.
> >
> > 비선형구조: 자료 간의 관계가 1대N의 관계를 갖는다.(예)트리)
>
> 스택에 자료를 삽입하거나 스택에서 자료를 꺼낼 수 있다.
>
> 마지막에 삽입한 자료를 가장 먼저 꺼낸다. 후입선출(Last-In-First-Out)이라고 부른다
>
> > 예를 들어 스택에 1,2, 3 순으로 자료를 삽입한 후 꺼내면 역순으로 즉, 321 순으로 꺼낼 수 있다.



## 스택의 구현

- 스택을 프로그램에서 구현하기 위해서 필요한 자료구조와 연산

  - 자료구조: 자료를 선형의로 저장할 저장소

    - C언어에서는 배열을 사용할 수 있다.
    - 저장소 자체를 스택이라 부르기도 한다.
    - 스택에서 마지막 삽입된 원소의 위치를 top이라 부른다.

  - 연산

    - 삽입: 저장소에 자료를 저장한다. 보통 push라 부른다.

    - 삭제: 저장소에서 자료를 꺼낸다. 꺼낸 자료는 삽입한 자료의 역순으로 꺼낸다. 보통 pop이라고 부른다.

      => 뒤에서부터 꺼냄

    - 스택이 공백인지 아닌지를 확인하는 연산: isEmpty

    - 스택의 top에 있는 item을 반환하는 연산 peek

- 스택의 삽입/삭제 과정

  - 빈 스택에 원소 A,B,C를 차례로 삽입 후 한 번 삭제하는 연산과정

![image-20200207091529727](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200207091529727.png)

```python
#스택의 기본 원리
top = -1
stack = [0]*100000

for now in range(1, 4):
    top += 1
    stack[top] = now

while top != -1 : #스택이 비어있을 동안
    print(stack[top])
    top -= 1
```



### 스택의 응용1: 괄호검사



- 괄호의 종류: 대괄호('[]'), 중괄호('{}'), 소괄호('()')
- 조건
  1. 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다.
  2. 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 한다.
  3. 괄호 사이에는 포함관계만 존재한다.

![image-20200207092730824](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200207092730824.png)

	열린 괄호가 나오면 push
	
	닫힌 괄호가 나오면 맨 마지막  요소를 pop 해서 비교

 



```python
top = -1
stack = [0] *123456
info = [0] *128
info[ord(')')] = '('
info[ord(']')] = '['
info[ord('}')] = '{'
info[ord('>')] = '<'
Data = input()
howmany = len(Data)
for now in range(howmany):
    if Data[now] == '(' or Data[now] == '{' or Data[now] == '['  or Data[now] == '<':#열린괄호면
        top +=1
        stack[top] = Data[now]
    elif info[ord(Data[now])] == stack[top]: #닫힌괄호 =Data[now]
        #stack[top] 대신 -1 써도 됨
        top -= 1
        stack.pop()
if top > -1:
    print("잘못된 괄호를 사용했습니다.")
else:
    print("괄호 검사가 완료되었습니다.")
```



## 재귀호출

>자기 자신을 호출하여 순환 수행되는 것
>
>함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램의 킉를 줄이고 간단하게 작성





- 재귀호출의 예) Factorial

![image-20200207101734216](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20200207101734216.png)

```python
def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n-1)
print(factorial(6))
```



재귀 연습문제1

```python
def recursionEX(n):
    if n <= 1:
        return n
    else:
        return n + recursionEX(n-1)
print(recursionEX(5))
```



재귀 연습문제 2

```python
def recursive(n):
    if n == 0:
        return print("end")
    else:
        print(n)
        return recursive(n-1)
recursive(3)
```



재귀 연습문제3

```python
#선택정렬 재귀로 풀어보기!
lst = [61, 70, 24, 39, 11]
def selectionSort(here, end):
    if here >= end:
        return lst
    else:
        mini = lst[here]
        where = here
        for now in range(here, end+1):
            if lst[now] < mini:
                mini = lst[now]
                where = now
                lst[here], lst[where] = lst[where], lst[here]
        return selectionSort(here+1, end)
print(selectionSort(0, 4))
```



### Memoization

- 메모이제이션은 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.



```python
def fibo1(n):
    global memo
    if n >=2 and len(memo) <=2:
        memo.append(fibo1(n-1) +fibo1(n-2))
    return memo[n]
memo = [0,1]
print(fibo1(6))
```



## DFS(깊이 우선 탐색)



- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요함.
- 두 가지 방법
  - 깊이 우선 탐색(Depth Fisrt Search,DFS)
  - 너비 우선 탐색(Breadth First Search,BFS)

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조의 스택 사용



### DFS 알고리즘

1. 시작 정점 v를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서 
   1. 방문하지 않은 정점 w가 있으면, 정점 v를 스택에 push하고 정점 w를 방문한다. 그리고 w를 v로 하여 다시 2.를 반복한다.
   2. 방문하지 않는 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2.를 반복한다.
3. 스택이 공백이 될 때까지 2.를 반복한다. 



#### 연습문제3



```python
Data = list(map(int, input().split()))
howmany = len(Data)>>1
mymap = [[0]*howmany for _ in range(howmany)]
visited = [0] * howmany

def DFS(here):
    print(here)
    visited[here] = True
    for next in range(0, howmany):
        if mymap[here][next] and not visited[next]:
            DFS(next)

for i in range(howmany):
    start = Data[i*2]
    stop = Data[i*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

DFS(1)
```

