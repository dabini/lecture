#  Queue



## 1. Queue 자료 구조의 개념



### 1) Queue 특성

 - 삽입, 삭제의 위치가 제한적인 자료구조
   	- 큐 뒤: 삽입/ 큐 앞: 삭제

- 선입선출구조(FIFO: First In First Out)
  - 큐에 삽입한 순서대로 원소가 저장
  - 가장 먼저 삽입된 원소는 가장 먼저 삭제됨
- 큐의 예
  - 서비스 대기 행렬



### 2) Queue의 구조 및 기본 연산

![큐의 구조 이미지 검색결과](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F25757B4556384E322B)

- 큐의 기본 연산
  - 삽입: enQueue
  - 삭제: deQueue



### 3) Queue의 주요 연산

1. enQueue(item): 큐의 뒤쪽(rear 다음)에 원소를 삽입하는 연산
2. deQueue(): 큐의 앞쪽(front)에서 원소를 삭제하고 반환하는 연산
3. createQueue(): 공백 상태의 큐를 생성하는 연산
4. isEmpty(): 큐가 공백상태인지를 확인하는 연산
5. isFull(): 큐가 포화상태인지를 확인하는 연산
6. Qpeek(): 큐의 앞쪽(front)에서 원소를 삭제 없이 반환하는 연산



### 4) Queue의 연산 과정

- 큐의 기본 연산 과정

  1. 공백 큐 생성: createQueue()

     front = rear = -1

  2. 원소 A 삽입: enQueue(A)

     front = -1 / A =rear

  3. 원소 B 삽입: enQueue(B)

     front = -1, rear = B

  4. 원소 반환/삭제: deQueue()

     A반환된 후, front값이 0이 되고 rear값이 B가 있는 1

  5. 원소 C 삽입: enQueue(C)

     rear값이 2가 됨

  6. 원소 반환/삭제: deQueue()

     B삭제 되고, front 값이 1으로 증가

  7. 원소 반환/삭제: deQueue()

     C삭제되고, front 값이 2로 변경, 남아 있는 원소가 없음

     => front == rear일 경우, Queue는 비어있는 상태

     ![큐의 구조 이미지 검색결과](https://lh3.googleusercontent.com/proxy/D579IRaiRLvLios7kr6HbZSuxOqmNS1XszsbxEcpIobA05CKH33VNNK0phu6TLTYf1U0oWAhqlGzG-oxlaHto_lvy2jOlGvyAr6FWBJ0yaIF_GQ3_fkLBicAz9wrH5oPB0VWu1iQb0ZXZrhySUOGR-zMWff4eqTJiDBrbhe3qsyhYUmWRf-J35RZs3-cgLng-EazNAXnlQ)

     



### 5) Queue의 종류

1. 선형 큐

   간단하고 기본적인 형태

   리스트 사용

2. 원형 큐

   선형에서 발전된 형태

   리스트 사용

3. 연결 큐

   연결 리스트 형식을 이용

4. 우선순위 큐

   큐를 응용





## 2. Queue의 종류

### 1) 선형 Queue

- 선형 큐의 특징

  1. 1차원 리스트를 이용한 큐

     - 큐의 크기 = 리스트의 크기

     - front = 저장된 첫 번째 원소의 인덱스

     - rear = 저장된 마지막 원소의 인덱스

  2. 상태표현

     - 초기 상태: front = rear = -1
     - 공백 상태: front = rear
     - 포화 상태: rear = n-1(n:리스트의 크기, n-1: 리스트의 마지막 인덱스)



 - 선형 큐의 구현

   1. 초기 createQueue()

      - 초기 공백큐 생성
        - 크기 n인 1차원 리스트 생성
        - front, rear = -1로 초기화

   2. enQueue(item)

      - 삽입: enQueue(item)

        - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해

          rear값을 하나 증겨시켜 새로운 원소를 삽입하 자리를 마련함

          그 인덱스에 해당하는 리스트원소 Q[rear]에 item을 저장

   ``` python
   def enQueue(item):
       global rear
       if isFull():
           print("Queue_Full")
       else:
           rear += 1
           Q[rear] = item
   ```

   3. deQueue

      - 삭제: deQueue()

        - 가장 앞에 있는 원소를 삭제하기 위해

          front 값을 하나 증가시켜 큐에 남아 있는 첫 번째 원소로 이동

          새로운 첫 번째 원소를 리턴함으로써 삭제와 동일한 기능을 함

   ```python
   def deQueue():
       global front
       if isEmpty():
           print("Queue_Empty")
       else:
           fromt += 1
           return Q[front]
   ```

    	4. isEmpty(), isFull()
        - 공백상태 및 포화상태 검사: isEmpty(), isFull()
          - 공백상태: front = rear
          - 포화상태: rear = n-1

   ```python
   def isEmpty():
       return fromt == rear
   def isFull():
       return rear == len(Q) -1
   ```

   5. Qpeek()
      - 검색: Qpeek()
        - 가장 앞에 있는 원소를 검색하여 반환하는 연산
        - 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환

   ``` python
   def Qpeek():
       if isEmpty():
           print("Queue_Empty")
       else:
           return Q[front+1]
   ```

- 선형 큐의 문제점: 잘못된 포화상태 인식
  1. 리스트 크기를 고정 -> 사용할 큐의 크기만큼을 미리 확보 -> 메모리의 낭비 발생
     - 삽입, 삭제를 계속할 경우 리스트의 앞부분을 활용할 수 있는 공간이 있음에도 불구하고, rear = n-1인 상태, 즉 포화상태로 인식
     - 더 이상의 삽입을 수행할 수 없음

![선형 큐 문제 이미지 검색결과](https://img1.daumcdn.net/thumb/R720x0.q80/?scode=mtistory2&fname=http%3A%2F%2Fcfile28.uf.tistory.com%2Fimage%2F236962475638645E30DB80)

- 선형 큐의 단점 해결 방법

  > 선형 큐는 삽입 삭제의 처리 속도가 빠르다는 장점이 있으며
  >
  > 메모리 낭비가 심하다는 단점이 있음

  - 원형 큐 사용으로 메모리 절약
  - 파이썬의 리스트 특성을 사용한 큐 사용으로 메모리 절약
    - 단점: 삽입, 삭제 시 복사, 데이터 이동시키는 연산 수행에 많은 시간 소모
  - 단순 연결 리스트로 구현한 큐 사용으로 메모리 동적 확보
  - 큐 라이브러리 사용

### 2) 원형 큐

- 1차원 리스트를 사용하되, 논리적으로 리스트의 처음과 끝이 연결되어 원형형태의 큐를 이룬다고 가정하고 사용함.
- 원형 큐의 논리적 구조

![원형 큐 구조 이미지 검색결과](https://lh3.googleusercontent.com/proxy/YEhE6yp2Em1-SOMO8WmLHicW8fKJymjZLXfrmKRD4GlbuQqSKd1wzXpj1zeVfwkz8bJfrMJMrQB_67snsNHqbanZhSj3aSCr7OMn3npv7Ll7nPx9YVND7qD5FAgDBnUo10d0geM_pGgqfquVDWHNS4zI2Qv3KxcHTLcc2Twwx8ehfjrZfQ)



- 원형 큐의 특징

  1. 초기 공백 상태

     front = rear = 0

  2. Index의 순환

     front와 rear의 위치가 리스트의 마지막 인덱스인 n-1을 가리킨 후, 논리적 순환을 이루어 리스트의 처음 인덱스인 0으로 이동해야 함

     이를 위해 나머지 연산자 %를 사용

  3. front 변수

     공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠

  4. 삽입 위치 및 삭제 위치

     삽입 위치: rear = (rear+1)%n

     삭제 위치: front = (front+1)%n

- 원형 큐의 기본 연산 과정 

![원형 큐 삽입 삭제 이미지 검색결과](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2506CD3C52F8C8C505)

- 원형 큐의 구현

  1. 초기 CreateQueue()
     - 초기 공백큐 생성
       - 크기 n인 1차원 리스트 생성
       - front = real = 0으로 초기화
  2. IsEmpty(), IsFull()
     - 공백상태 및 포화상태 검사: isEmpty(), isFull()
       - 공백상태: front = rear
       - 포화상태: 삽입할 rear값의 다음 위치가 현재 front 값일 때
       - (rear + 1) % n = front

  ``` python
  def isEmpty():
      return fromt == rear
  def isFull():
      return (rear+1)%len(cQ) == front
  ```

   3. enQueue(item)

      - 삽입: enQueue(item)

        - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해 

          rear 값을 조정하여 새로운 원소를 삽입할 자리를 마련함:

          rear <=  (rear +1) %n

          인덱스에 해당하는 리스트원소 cQ[rear]에 item을 저장

  ```python
  def enQueue(item):
      global rear
      if isFull():
          print("Queue_Full")
      else:
          rear = (rear +1) %len(cQ)
          cQ[rear] = item
  ```

  

  4. deQueue

     - 삭제: deQueue(), delete()

       - 가장 앞에 있는 원소를 삭제하기 위해

         front 값을 조정하여 삭제할 자리를 준비함

         새로운 front원소를 리턴함으로써 삭제와 동일한 기능을 함

  ```python
  def deQueue():
      global front
      if isEmpty():
          print("Queue_Empty")
      else:
          front = (front +1)% len(cQ)
          return cQ[front]
      
  def delete():
      global front
      if is Empty():
          print("Queue_Empty")
      else:
          front = (front+1)%len(cQ)
  ```

  

- 파이썬으로 구현한 원형 큐의 삽입 및 삭제 함수

```python
def isEmpty():
    return front == rear
def isFull():
    return (rear+1)%len(cQ) == front

def enQueue(item): #원형 큐의 삽입 연산
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear = (rear+1)%len(cQ)
        cQ[rear] = item
        
def deQueue(): #원형 큐의 삭제 연산
    global front
    if isEmpty():
        print("Queue_Empty")
    else:
        front = (front +1 )% len(cQ)
        return cQ[front]
    
cQ_size = 3
cQ = [0] * cQ_size

#front, rear를 0으로 초기화
front = rear = 0

enQueue('A')
enQueue('B')
enQueue('C')
print(deQueue())
print(deQueue())
print(deQueue())
```



### 3) 리스트 특성을 사용한 Queue

1. 파이썬 리스트 특성을 사용한 큐
   - 리스트는 크기를 동적으로 변경할 수 있음.
   - 메모리 절약(사용한 만큼만 확보)
   - 삽입, 삭제 시 복사, 데이터를 이동시키는 연산을 수행하는데 많은 시간 소모
2. front는 리스트의 맨 앞: -1
3. rear는 리스트의 맨 뒤: len(queue) -1



- 파이썬으로 구현한 원형 큐의 삽입 및 삭제 함수

```python
def enQueue(item):
    queue.append(item)
    
def deQueue():
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue.pop(0)
def isEmpty():
    return len(queue) == 0

def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return queue[0]
    
queue = []
#fornt = -1
#rear: len(queue) -1

enQueue("A")
enQueue("B")
enQueue("C")
print(deQueue())
print(deQueue())
print(deQueue())
```



### 4) 연결 큐

- 연결 큐의 특징

  1. 단순 연결 리스트(Linked List)를 이용한 큐
     - 큐의 원소: 단순 연결리스트의 각 노드
     - 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음
     - front: 첫 번째 노드를 가리키는 링크
     - rear: 마지막 노드를 가리키는 링크
  2. 상태 표현
     - 초기 상태: front = rear = None
     - 공백 상태: front = rear = None
     - 연결 큐의 포화상태는 없음!

  

- 연결 큐의 연산 과정

  

![연결 큐 연산 이미지 검색결과](https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F220C004D5639ABC51A)

- 연결 큐의 구현

  1. createdLinkedQueue()

     - 초기 공백 큐 생성
       - 리스트 노드 없이 포인터 변수만 생성함
       - front와 rear값을 None으로 초기화

  2. isEmpty()

     - 공백상태 검사
     - 공백상태: front = rear = None

     ```python
     def isEmpty():
         return front == None
     ```

     

  3. enQueue(item)

     - 삽입
       - 새로운 노드를 생성한 후 데이터 필드에 item 저장
       - 연결 큐가 공백인 경우, 아닌 경우에 따라 front, rear 변수 지정

     ```python
     def enQueue(item):
         global front, rear
         newNode = Node(item) #새로운 노드 생성
         if isEmpty():
             front = newNode
         else:
             rear.next = newNode
         rear = newNode
     ```

     

  4. deQueue()

     - 삭제
       - old가 지울 노드를 가리키게 하고, front 재설정
       - 삭제 후 공백 큐가 되는 경우, rear도 None값으로 설정
       - old가 가리키는 노드를 삭제하고 메모리 반환

  ```python
  def deQueue():
      global front, rear
      if isEmpty():
          print("Queue_Empty")
          return None
      item = front.item
      front = front.next
      if isEmpty():
          rear = None
      return item
  ```



- 파이썬으로 구현한 연결 큐

  ```python
  class Node:
      def __init__(self, item, n=None):
          self.item = item
          self.next = n
  
  
  def enQueue(item):
      global front, rear
      newNode = Node(item)
      if front == None:
          front = newNode
      else:
          rear.next = newNode
      rear = newNode
  
  
  def isEmpty():
      return front== None
  
  
  def deQueue():
      global front, rear
      if isEmpty():
          print("Queue_Empty")
          return None
      item = front.item
      front = front.next
      if front == None:
          rear = None
      return item
  
  
  def Qpeek():
      return front.item
  
  
  def printQ():
      f = front
      s = ""
      while f:
          s += f.item + ""
          f = f.next
      return s
  
  
  front = None
  rear = None
  
  enQueue("A")
  enQueue("B")
  enQueue("C")
  printQ()
  print(deQueue())
  print(deQueue())
  print(deQueue())
  ```



### 5) Queue 라이브러리

- 큐 모듈
  1. 큐 모듈에 정의된 클래스
     - queue.Queue(maxsize): 선입선출(FIFO) 큐 객체를 생성
     - queue.LifoQueue(maxsize): 스택개념의 후입선출 큐 객체 생성
     - queue.PriorityQueue(maxsize): 우선순위 큐 객체를 생성, 입력되는 아이템의 형식은(순위, 아이템)의 튜플로 입력되며, 우선 순위는 숫자가 작을수록 높은 순위를 가짐
  2. maxsize는 최대 아이템수, 지정하지 않거나 음수이면 내용만큼 늘어남
  3. 제시된 3개의 클래스는 다음과 같은 메서드를 동일하게 가짐
     - qsize(): 큐 객체에 입력된 아이템의 개수를 반환
     - put(item[, block[, timeout]]): 큐 객체에 아이템을 입력
     - get([block[, timeout]]): 생성된 큐 객체 특성에 맞추어, 아이템 1개를 반환함
     - empty(): 큐 객체가 비어있으면 True 리턴
     - full():  큐 객체가 꽉 차있으면 True 리턴
  4. 클래스의 정렬방식에 따라 get 계열의 메서드 결과가 달라짐



- 큐 모듈 활용

  > 선입선출의 큐 개념을 구현한 큐 클래스 활용

```python
import queue
q = queue.Queue() #FIFO 구조 큐 생성
q.put('A')
q.put('B')
q.put('C')

while not q.empty():
    print(q.get())  
```







## 3. Queue의 활용

### 1) 우선순위 Queue

- 우선순위 큐

  - 우선순위를 가진 항목들을 저장하는 큐

  - FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 됨

  - 적용 분야

    시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 태스크 스케쥴링

- 구현

  - 리스트를 이용한 우선순위 큐
  - 우선 순위 큐 라이브러리 사용

- 기본 연산

  - 삽입: enQueue
  - 삭제: deQueue

![우선순위 큐 이미지 검색결과](https://www.includehelp.com/ds/Images/priority-queue.jpg)

- 리스트를 이용한 우선순위 큐의 구현

  1. 리스트를 이용하여 자료 저장

  2. 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입하는 구조

  3. 가장 앞에 최고 우선순위 원소가 위치하게 됨.

     

- 문제점

  - 리스트를 사용하므로, 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생

  - 소요되는 시간이 많이 걸림

    => 연결리스트를 이용하거나

    Priority Queue(maxsize) 클래스 사용

    힙 사용



### 2) 버퍼

- 버퍼의 의미

  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
  - 버퍼링: 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

- 버퍼의 자료구조

  - 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용
  - 순서대로 입력/출력/전달 되어야 하므로 FIFO 방식의 자료구조인 큐가 활용됨

- 버퍼 활용 - 키보드 버퍼의 수행 과정

  사용자 키보드 입력 "A P S enter"

  키보드 입력 버퍼 "A P S enter"

  => 키보드 입력 버퍼에 Enter 키 입력이 들어오면

  프록램 실행 영역 "A P S enter"

  => 연산