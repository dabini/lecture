# 순열을 생성하는 함수
# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)
#baby gin
#
# num  = int(input("6자리 숫자를 입력하시오: ")) #Baby Gin 확인할 6자리 수 문자열
# c = [0] * 12 #6자리 수로부터 각 자리수를 추출하여 개수를 누적할 리스트
# for i in range(6):
#     c[num % 10] += 1
#     num //= 10
#
# i = 0
# tri = run = 0
# while i < 10 :
#     if c[i] >= 3: #triplet 조사 후 데이터 삭제
#         c[i] -= 3
#         tri += 1
#         continue; #다시 while로 돌아감
#     if c[i] >= 1 and c[i+1] >= 1 and c [i+2] >=1: #run 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i+1] -= 1
#         c[i+2] -= 1
#         run += 1
#         continue
#     i += 1
#
# if run + tri == 2 :
#     print("Baby Gin")
# else:
#     print("Not Baby Gin")


# #버블 정렬 알고리즘
# def BubbleSort(a) :
#     for i in range(len(a)-1, 0, -1): #범위의 끝 위치
#         for j in range(0, i):
#             if a [j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
# a = [79, 80, 7, 56, 41]
# print(BubbleSort(a))


#카운팅 정렬 알고리즘
# def Counting_Sort(A, B, k):
# # A [1 .. n] --입력 배열(1 to k)
# # B [1 .. n] -- 정렬된 배열.
# # C [1 .. k] -- 카운트 배열.
#
#     C = [0] * k
#
#     for i in range(0, len(B)):
#         C[A[i]] += 1
#
#     for i in range(1, len(C)):
#         C[i] += C[i-1]
#
#     for i in range(len(B)-1, -1, -1):
#         B[C[A[i]]-1] = A[i]
#         C[A[i]] -= 1
#
# inp = [1, 1, 2, 3, 1 ,2, 1, 4, 3, 4, 2, 0]
# out = [0] * len(inp)
# k = 5
# Counting_Sort(inp, out, k)
# print(out)
#알고리즘 숙제
# import sys
# sys.stdin = open("0128input.txt", 'r')
# tc = 10
# for i in range(1, tc+1):
#     N = int(input())
#     Hs = list(map(int, input().split(" ")))
#     cnt = 0
#     vSum = 0
#     for j in range(2, N-1):
#         if Hs[j] - Hs[j+1] >=1 and Hs[j] - Hs[j+2] >= 1 and Hs[j] - Hs[j-1] >=1 and Hs[j] - Hs[j-2] >=1:
#             cnt = min([Hs[j] - Hs[j+1], Hs[j] - Hs[j+2], Hs[j] - Hs[j-1],Hs[j] - Hs[j-2]])
#             vSum += cnt
#
#     print("#{0} {1}".format(i, vSum))


#6차시 1일차 min_max
# T = int(input())
#
# for t in range(T):
#     N = int(input())
#     a = list(map(int, input().split()))
#     lst = []
#
#     def my_max(a):
#         for i in a:
#             if i not in lst:
#                 lst.append(i)
#             if i > lst[0]:
#                 lst[0] = i
#         return lst[0]
#
#
#     def my_min(a):
#         for i in a:
#             if i not in lst:
#                 lst.append(i)
#             if i < lst[0]:
#                 lst[0] = i
#         return lst[0]
#
#     print('#{0} {1}'.format(t+1, my_max(a)-my_min(a)))


#7차시 1일차 -전기버스
# T = int(input())
# for t in range(T):
#     K, N, M = map(int, input().split())
#     busstops = list(map(int, input().split()))
#     lst = [0] *  (N+1)
#
#     for i in range(len(busstops)):
#         lst[busstops[i]] += 1
#
#     start = 0
#     end = K
#     cnt = 0
#
#     while True:
#         zero = 0
#         for i in range(start +1, end+1) :
#             if lst[i] == 1:
#                 start = i
#             else:
#                 zero += 1
#         if zero == K:
#             cnt = 0
#             break
#         cnt += 1
#         end = start + K
#
#         if end >= N:
#             break
#     print('#{0} {1}'.format(t+1, cnt))



#1일차 숫자카드

# T = int(input())
# for i in range(T):
#     N = int(input())
#     a = list(input())
#     dict = {}
#     cnt = 1
#     for n in range(N):
#         if a[n] not in dict.keys():
#             dict[a[n]] = cnt
#         else:
#             dict[a[n]] += 1
#     lst = []
#     for k, v in dict.items():
#         if v == max(sorted(dict.values(), reverse=True)):
#             lst.append(k)
#             if len(lst) == 1:
#                 print(k, v)
#                 break
#             else:
#                 print(lst[0], v)
#                 break

# TC = int(input())
# for tc in range(1, TC+1):
#     N = int(input())
#     Data = input()
#     Data = [int(_) for _ in Data]
#     cnt_lst = [0]*10
#
#     for i in range(N):
#         cnt_lst[Data[i]] += 1
#
#     max_index, max_num = 0, 0
#     for i in range(len(cnt_lst)-1,-1,-1):
#         if cnt_lst[i] > max_index:
#             max_index = cnt_lst[i]
#             max_num = i
#
#     print('#%s %d %d'%(tc, max_num, max_index))

