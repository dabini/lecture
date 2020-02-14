# # 연습문제1
# def MyAbs(y, x):
#     if y > x:
#         return y - x
#     else:
#         return x - y
# def IsSafe(y, x):
#     if y >= 0 and y < 5 and x >= 0 and x < 5:
#         return True
#     else:
#         return False
#
# Data = [[0 for _ in range(5)] for _ in range(5)]
#
# for i in range(5):
#     Data[i] = list(map(int, input().split()))
#
# dy = [-1, 1, 0, 0]
# dx = [0, 0, -1, 1]
#
# sum = 0
#
# for y in range(5):
#     for x in range(5):
#         for dir in range(4):
#             newY = y + dy[dir]
#             newX = x + dx[dir]
#             if IsSafe(newY, newX) :
#                 sum += MyAbs(Data[y][x], Data[newY][newX])
# print("sum = %d" %sum)
#
#
# arr = [3, 6, 7, 1, 5, 4]
# n = len(arr) #n:원소의 개수
#
# for i in range(1<<n): #1<<n: 부분집합의 개수
#     for j in range(n): #원소의 수만큼 비트를 비교함
#         if i & (1<<j): #i의 j번째 비트가 1이면 j번째 원소 출력
#             print(arr[j], end=" ")
#     print()
# print()
#
#
# 연습문제2
# 1부터 5까지 정수의 부분집합을 출력하시오
# arr = list(range(1, 6))
# n = len(arr)
# for i in range(1<<n):
#     out = []
#     for j in range(n):
#         if i & (1<<j):
#             out.append(str(arr[j]))
#     print(", ".join(out))
# print()
#
# #1부터 10까지의 정수의 부분집합의 합이 10이 되는 부분집합을 출력하시오.
# arr = list(range(1, 11))
# n = len(arr)
#
# for i in range(1<<n):
#     out = []
#     total = 0
#     for j in range(n):
#         if i & (1<<j):
#             out.append(arr[j])
#     for a in range(len(out)):
#         total += out[a]
#     if total == 10:
#         print(out)
#
#
# 순차 검색
# def sequentialSearch2(a, n, key):
#     i = 0
#     while i < n and a[i] < key:
#         i += 1
#         if i < n and a[i] == key:
#             return i
#     else:
#         return -1
#
# a = [2,4,7,9,11,19,23]
# n = len(a)
# print(sequentialSearch2(a, n, 11))
# print(sequentialSearch2(a, n, 12))
#
#
# def search_list(a, x):
#     n = len(a)
#     for i in range(n):
#         if x == a[i]:
#             return i
#     return -1
#
# lst = [2, 4, 7, 9, 11, 19, 23]
# print(search_list(lst, 11))
#
#
# 이진 검색 알고리즘
# search_list = [2, 4, 7, 9, 11, 19, 23]
# k = int(input())
# start = 0
# end = len(search_list)
#
# while start <= end:
#     mid = (end + start) // 2
#     if search_list[mid] == k:
#         print(mid)
#         break
#     elif search_list[mid] > k:
#         end = mid - 1
#     elif search_list[mid] < k:
#         start = mid + 1
#
#
# #선택 정렬 과정
# lst = [64, 25, 10, 22, 11]
#
# for i in range(len(lst)):
#     min = i
#     for now in range(i+1, len(lst)):
#         if lst[min] > lst[now]:
#             min = now
#     lst[i], lst[min] = lst[min], lst[i]
# print(lst)
#
#
# # 연습문제_SUM
# field = [[0 for _ in range(100)] for _ in range(100)]
#
# for k in range(10):
#     tc = int(input())
#     for j in range(100):
#         field[j] = list(map(int, input().split()))
#
#     lst = []
#     for y in range(100):
#         total = 0
#         for x in range(100):
#             total += field[y][x]
#         lst.append(total)
#
#     for y in range(100):
#         total = 0
#         for x in range(100):
#             total += field[x][y]
#         lst.append(total)
#
#     total = 0
#     for y in range(100):
#         for x in range(100):
#             if y == x:
#                 total += field[y][x]
#     lst.append(total)
#
#     total = 0
#     for y in range(1, 100):
#         for x in range(1, 100):
#             if y == x:
#                 total += field[-y][-x]
#     lst.append(total)
#     max_num = max(lst)
#     print("#{} {}".format(tc, max_num))


#연습문제 3 달팽이

def isSafe(a, b):
    if a < 5 and a >= 0 and b < 5 and b >= 0:
        return True
    else:
        return False

field = [[0 for _ in range(5)] for _ in range(5)]
out  = [[0 for _ in range(5)] for _ in range(5)]
for j in range(5):
    field[j] = list(map(int, input().split()))

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
min_lst =[]

while True:
    for y in range(5):
        min_lst.append(min(field[y]))
    min_num = min(min_lst)

    for y in range(5):
        for x in range(5):
            if field[y][x] == min_num:
                field[y][x] = 987654321

    for j in range(5):
        for i in range(5):
            for dir in range(4):
                if isSafe( j+ dir_y[dir%4], i+ dir_x[dir%4]) or out[newY][newX] != 0:
                    newY = j + dir_y[dir%4]
                    newX = i + dir_x[dir%4]
                    out[newY][newX] = min_num

    if min_num == 25:
        break
print(out)