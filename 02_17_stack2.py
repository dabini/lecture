# #연습문제 1
#
# cal_num = input()
# res = []
# stack = []
#
# isp = [0] * 300
# isp[ord("(")] = 0
# isp[ord("*")] = 2
# isp[ord("/")] = 2
# isp[ord("+")] = 1
# isp[ord("-")] = 1
#
# icp = [0] * 300
# icp[ord("(")] = 3
# icp[ord("*")] = 2
# icp[ord("/")] = 2
# icp[ord("+")] = 1
# icp[ord("-")] = 1
#
#
# for k in cal_num:
#     if k == "(":
#         stack += [k]
#     elif k == ')':
#         while stack and stack[-1] != '(':
#             res += [stack.pop()]
#         stack.pop()
#     elif k.isnumeric():
#         res += [k]
#     else:
#         while stack and isp[ord(stack[-1])] >= icp[ord(k)]:
#             res += [stack.pop()]
#         stack += [k]
#
# while stack:
#     res += [stack.pop()]
#
# print(*res)


#후위표기법의 수식을 스택을 이용하여 계산
# raw = input()
# stack = []
#
# for r in raw:
#     if r.isnumeric():
#         stack += [r]
#     else:
#         if r == '+':
#             temp = int(stack[-2]) + int(stack[-1])
#         elif r == '-':
#             temp = int(stack[-2]) - int(stack[-1])
#         elif r == '*':
#             temp = int(stack[-2]) * int(stack[-1])
#         elif r == '/':
#             temp = int(stack[-2]) / int(stack[-1])
#         stack.pop()
#         stack.pop()
#         stack += [temp]
#     res = stack[0]
# print(res)



#
# def backtracking(a, k, input):
#     global MaxCandidates
#     c = [1, 0]
#
#     if k == input:
#         for i in range(1, input+1):
#             if a[i] == True:
#                 print(i, end=" ")
#         print()
#     else:
#         k += 1
#
#         for i in range(2):
#             a[k] = c[i]
#             backtracking(a, k, input)
# MaxCandidates = 100
# nmax = 100
# a = [0] *nmax
# backtracking(a, 0, 3)




# def backtracking(a, k, input):
#     global MaxCandidates
#     c = [1, 0]
#
#     if k == input:
#         for i in range(1, input+1):
#             if a[i] == True:
#                 print(i, end=" ")
#         print()
#     else:
#         k += 1
#
#         a[k] = 1
#         backtracking(a, k, input)
#         a[k] = 0
#         backtracking(a, k , input)
#
#
# a = [0] * 100
# backtracking(a, 0, 10)



# 연습문제2
#
# def backtracking(a, k, input):
#     global maxcandidate
#
#     if k == input:
#         total = []
#         for i in range(1, input+1):
#             if a[i] == True:
#                 total += [i]
#         if sum(total) == 10:
#             print(*total)
#
#     else:
#         k += 1
#         a[k] = 1
#         backtracking(a, k, input)
#         a[k] = 0
#         backtracking(a, k , input)
#
# a = list(range(11))
# backtracking(a, 0, 10)
#

# 연습문제 2 _교수님 코드
# def backtracking(a, k, input, s):
#     if k == (input-1):
#         if s == 10:
#             for i in range(input):
#                 if a[i] == True:
#                     print(P[i] , end=" ")
#             print()
#     else:
#         if s <= 10:
#             a[k] = 0
#             backtracking(a, k+1, input, s)
#             a[k] = 1
#             backtracking(a, k+1 , input, s+P[k])
#
# a = [0] * 100
# P = list(range(1, 11))
# backtracking(a, 0, 10, 0)


#연습문제 2 _교수님 코드
# def backtracking(a, k, input):
#     if k == input:
#         psum = 0
#         for i in range(input):
#             if a[i] == 1:
#                 psum += P[i]
#         if psum == 10:
#             for i in range(input):
#                 if a[i] ==1:
#                     print(P[i], end =' ')
#             print()
#         return
#     else:
#         a[k] = 0
#         backtracking(a, k+1, input)
#         a[k] = 1
#         backtracking(a, k+1, input)
#
# a = [0]*5
# P = [1, 3, 5, 7, 9]
# backtracking(a, 0, 5)



# #백트래킹을 이용해 순열 구하기
# def perm_r_1(a, k, N):
#     if k == N:
#         print(a)
#     else:
#         in_perm = [False] * N
#         c = [0] * N
#
#         for i in range(k):
#             in_perm[a[i]] = True
#
#         ncandidates = 0
#         for i in range(N):
#             if in_perm[i] == False:
#                 c[ncandidates] = i
#                 ncandidates += 1
#
#         for i in range(ncandidates):
#             a[k] = c[i]
#             perm_r_1(a, k+1, N)
#
# a = [0] * 3
# perm_r_1(a, 0, 3)


#순열 좀 더 쉽게
# N = 4
# R = 4
# def perm_r_3(k):
#     global N, R
#     if k == R:
#         print(arr[0], arr[1], arr[2], arr[3])
#     else:
#         for i in range(k, N):
#             arr[k], arr[i] = arr[i], arr[k]
#             perm_r_3(k+1)
#             arr[k], arr[i] = arr[i], arr[k]
#
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# perm_r_3(0)


#분할정복_ 거듭제곱
# def Power(base, exponent):
#     if base == 0:
#         return 1
#     result = 1
#     for i in range(exponent):
#         result *= base
#     return result
# print(Power(2, 2))


# #퀵 정렬 알고리즘
# def quickSort(a, begin, end):
#     if begin < end:
#         p = partition(a, begin, end)
#         quickSort(a, begin, p-1)
#         quickSort(a, p+1, end)
#
# def partition(a, begin, end):
#     pivot = (begin + end) //2
#     L = begin
#     R = end
#     while L < R:
#         while(a[L] <a[pivot] and L<R):
#             L += 1
#         while(a[R] >= a[pivot] and L<R):
#             R -=1
#         if L < R:
#             if L == pivot:
#                 pivot = R
#             a[L], a[R] = a[R], a[L]
#
#
#     a[pivot], a[R] = a[R], a[pivot]
#     return R
#
# a = [69, 10, 30, 2, 16, 8, 31, 22]
# quickSort(a, 0, len(a)-1)
# print(a)