# #문자열뒤집기
# #내 CODE
# Data = list(input())
# new = ""
# for i in range(len(Data)):
#     new += Data[-(i+1)]
# print(new)

#
# #연습문제1
# s = "Reverse this string"
# s = s[::-1]
# print(s)

#연습문제
#atoi
#char to int
# '1''2''3' -=> 123
# lst = ['1', '2', '3']
# res = 0
# for i in range(len(lst)):
#     k = ord(lst[i]) - 48
#     res += k * 10**(len(lst) - i -1)
# print(res)
#
#
# #itoa
# #int to char
# i = 123
# res = ''
# k = 0
# check = i
#
# while check > 0 :
#     check = check // (10**k)
#     k += 1
# # print(k) #k=3
#
# for n in range(k):
#     a = i % (10** k-n)
# res += ascii(a)
# print(res)
# print(type(res))

#패턴매칭
# p = 'is'
# t = 'This is a book~!'
# M = len(p)
# N = len(t)
#
# def BruteForce(p, t):
#     i = 0
#     j  = 0
#     while j < M and i< N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i - M
#     else:
#         return -1
# print(BruteForce(p, t))


# 브루트
# N, K = map(int, input().split())
# field = [[0]*(N+1) for _ in range(N+1)]
# visited = [0] *(N+1)
# res = 0
#
# def GetSome(here):
#     global res, ans
#     if here == 7:
#         if res < ans :
#             ans=res
#             return
#
#     for now in range(N+1):
#         if field[here][now] and not visited[now]:
#             res += field[here][now]
#             visited[now] = 1
#             GetSome(now)
#             visited[now] = 0
#             res -= field[here][now]
#
# for k in range(K):
#     start, end, cost = map(int, input().split())
#     field[start][end] = cost
# ans = 987654321
# GetSome(1)
# print(ans)