## Day3 문제 풀이



### 1. 정곤이의 단조증가하는 함수

```python
# import sys
# sys.stdin = open('input.txt', 'r')

def increase(k):
    k = str(k)
    for a in range(len(k)-1):
        if (int(k[a])) <= int(k[a+1]):
            pass
        else:
            return False
    return True

T = int(input())
for t in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    out = [-1]

    for i in range(N-1):
        for j in range(i+1, N):
            if increase(num_list[i] * num_list[j]):
                out += [num_list[i] * num_list[j]]

    # for a in lst:
    #     for b in range(len(a)-1):
    #         if (int(a[b])) <= int(a[b+1]):
    #             out += [int(a)]

    print("#{} {}".format(t+1, max(out)))
```



### 2. 다솔이의 다이아몬드 장식

```python
T = int(input())

for t in range(T):
    word = input()
    res = ''
    print("..#."*len(word)+".")
    print(".#.#"*len(word)+".")
    for i in range(len(word)):
        res += "#.{}.".format(word[i])
    print(res + "#")
    print(".#.#" * len(word) + ".")
    print("..#." * len(word) + ".")
```



### 3. 영준이의 카드 카운팅

```python
T = int(input())

for t in range(T):
    check = True
    card_lst = []
    num_lst = [13, 13, 13, 13] #SDHC

    card = input()
    for i in range(0, len(card), 3):
        card_lst += [card[i] + card[i+1] + card[i+2]]

    for c in card_lst:
        if card_lst.count(c) > 1:
            check = False
        else:
            if c[0] == 'S':
                num_lst[0] -= 1
            elif c[0] == 'D':
                num_lst[1] -= 1
            elif c[0] == 'H':
                num_lst[2] -= 1
            elif c[0] == 'C':
                num_lst[3] -= 1


    if check is True:
        print("#{} {}".format(t+1, " ".join(list(map(str, num_lst)))))
    else:
        print("#{} ERROR".format(t + 1))
```



### 4. 파스칼의 삼각형

```python
T = int(input())

for t in range(T):
    print('#{}'.format(t+1))
    num = int(input())
    pascal = [['']*num for nu in range(num)]

    for i in range(num):
        pascal[i][0] = 1
        pascal[i][i] = 1

    for i in range(2, num):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

    for i in range(num):
        print(*pascal[i])
```



### 5. 스위치



```python
def switch(lst, i):
    if lst[i] == 1:
        lst[i] -= 1
    elif lst[i] == 0:
        lst[i] += 1
    return lst

num = int(input()) #스위치 개수
sw_lst = list(map(int, input().split())) #스위치 상태 켜져있으면 1 꺼져있으면 0
stu_num = int(input()) #학생수 남학생1 여학생2
for stu in range(stu_num):
    s, n = map(int, input().split())  #s 성별 n 비교할 수

    if s == 1:
        for i in range(num):
            if (i+1) % n == 0:
                switch(sw_lst, i)

    elif s == 2:
        k = 0
        for i in range(num):
            if i == n-1:
                while i-1-k >= 0 and i+1+k <= num-1:
                    if sw_lst[(i-1)-k] != sw_lst[i+1+k]:
                        break
                    else:
                        switch(sw_lst, i-1-k)
                        switch(sw_lst, i+1+k)
                    k += 1
                switch(sw_lst, i)
                break
for i in range(0, num, 20):
    print(*sw_lst[i:i+20])
```
