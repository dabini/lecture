def f(n, k): #순열의 n 번 원소 결정
    if n == k:
        print(p)
        return
    else:
        for i in range(k):
            if used[i] == 0:
                used[i] = 1
                p[n] = A[i]
                # used.append(A[i])
                f(n+1, k)
                used[i] = 0
                # used.pop()
A = [1, 2, 3, 4, 5]
used = [0] * 5
p =  [0] * 5
f(0, 5)
