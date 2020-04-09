def change(A):
    global tmp
    visited = [0] * 10
    tmp = [0]*10
    for i in range(10):
        if A[i] >= 10:
            if i-1 >= 0:
                if not visited[i - 1]:
                    tmp[i - 1] = int(-abs(A[i]) // 2)
                else:
                    tmp[i - 1] += int(-abs(A[i]) // 2)
            else:
                if not visited[i]:
                    tmp[i] += int(abs(A[i]) // 2)
                    visited[i] = 1
                else:
                    tmp[i] = int(abs(A[i]) // 2)

            if i + 1 < 10:  # 범위 내에 있다면!
                if not visited[i + 1]:
                    tmp[i + 1] = int(abs(A[i]) // 2)
                    visited[i + 1] = 1
                else:
                    tmp[i + 1] += int(abs(A[i]) // 2)
            else:
                if not visited[i]:
                    tmp[i] = int(-abs(A[i]) // 2)
                    visited[i] = 1
                else:
                    tmp[i] += int(-abs(A[i]) // 2)

        elif A[i] < 0:
            if i-1 >=0: #범위 내에 있다면!
                if not visited[i-1]:
                    tmp[i-1] = A[i]
                    visited[i-1] = 1
                else:
                    tmp[i-1] += A[i]
            else:
                if not visited[i]:
                    tmp[i] = -(A[i])
                    visited[i] = 1
                else:
                    tmp[i] += -(A[i])
        elif 0< A[i] <10:
            if i+1 < 10: #범위 내에 있다면!
                if not visited[i+1]:
                    tmp[i+1] = A[i]
                    visited[i+1] = 1
                else:
                    tmp[i+1] += A[i]
            else:
                if not visited[i]:
                    tmp[i] = -(A[i])
                    visited[i] = 1
                else:
                    tmp[i] += -(A[i])
    return tmp

T = int(input())
for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    while N:
        change(A)
        A = tmp
        N -= 1

    print("#{}".format(t+1), end=" ")
    print(*A)