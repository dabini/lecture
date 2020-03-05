Data = list(map(int, input().split()))

def GetSome():
    if len(res) == r:
        print(res)
        return
    start = Data.index(res[-1]) + 1 if res else 0
    for next in range(start, len(Data)):
        res.append(Data[next])
        GetSome()
        res.pop()

n = 5
r = 3
res = []
GetSome()