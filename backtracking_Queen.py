num = 4
field = [[0]*num for _ in range(num)]

visitedX = [0] * (num+1)
visitedIncrease = [0] *(2*num +1)
visitedDecrease = [0] *(2*num +1)

def GetSome(y):
    global ans
    if y > 4:
        ans += 1
        return
    for x in range(1, 5):
        if not visitedX[x] and not visitedIncrease[y+x] and not visitedDecrease[y-x+4]:
            visitedX[x] = visitedIncrease[y+x] = visitedDecrease[y-x+4] = 1
            GetSome(y+1)
            visitedX[x] = visitedIncrease[y+x] = visitedDecrease[y-x+4] = 0
ans = 0
GetSome(1)
print(ans)