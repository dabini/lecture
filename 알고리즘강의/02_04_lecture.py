#구간합 설명
# Tc = int(input())
#
# for tc in range(1, Tc+1):
#     N,M = map(int, input().split())
#     Data = list(map(int, input().split()))
#
#     sum = 0
#     for now in range(M):
#         sum += Data[now]
#
#     minv = maxv = sum
#
#     for now in range(1, N-M+1):
#         sum = 0
#         for addthis in range(now, now+M):
#             sum += Data[addthis]
#         if maxv < sum : maxv = sum
#         if minv > sum : minv = sum
