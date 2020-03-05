#스택의 기본 원리
# top = -1
# stack = [0]*100000
#
# for now in range(1, 4):
#     top += 1
#     stack[top] = now
#
# while top != -1 : #스택이 비어있을 동안
#     print(stack[top])
#     top -= 1


#연습문제2: 괄호 검사
# top = -1
# stack = [0] *123456
# info = [0] *128
# info[ord(')')] = '('
# info[ord(']')] = '['
# info[ord('}')] = '{'
# info[ord('>')] = '<'
# Data = input()
# howmany = len(Data)
# for now in range(howmany):
#     if Data[now] == '(' or Data[now] == '{' or Data[now] == '['  or Data[now] == '<':#열린괄호면
#         top +=1
#         stack[top] = Data[now]
#     elif info[ord(Data[now])] == stack[top]: #닫힌괄호 =Data[now]
#         #stack[top] 대신 -1 써도 됨
#         top -= 1
#         stack.pop()
# if top > -1:
#     print("잘못된 괄호를 사용했습니다.")
# else:
#     print("괄호 검사가 완료되었습니다.")

# def recursive(n):
#     if n == 0:
#         return print("end")
#     else:
#         print(n)
#         return recursive(n-1)
# recursive(3)

# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         return n * factorial(n-1)
# print(factorial(6))

# def recursionEX(n):
#     if n <= 1:
#         return n
#     else:
#         return n + recursionEX(n-1)
# print(recursionEX(5))

# def fibo(n):
#     if n <2:
#         return n
#     else:
#         return fibo(n-2) + fibo(n-1)
# print(fibo(5))

# #선택정렬 재귀로 풀어보기!
# lst = [61, 70, 24, 39, 11]
# def selectionSort(here, end):
#     if here >= end:
#         return lst
#     else:
#         mini = lst[here]
#         where = here
#         for now in range(here, end+1):
#             if lst[now] < mini:
#                 mini = lst[now]
#                 where = now
#                 lst[here], lst[where] = lst[where], lst[here]
#         return selectionSort(here+1, end)
# print(selectionSort(0, 4))

#Memoization
# def fibo1(n):
#     global memo
#     if n >=2 and len(memo) <=2:
#         memo.append(fibo1(n-1) +fibo1(n-2))
#     return memo[n]
# memo = [0,1]
# print(fibo1(6))

#연습문제3


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