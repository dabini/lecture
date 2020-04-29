inp = input()
for i in range(0, len(inp), 7):
    cnt = res = 0
    j = i
    while j < len(inp) and cnt < 7:
        res = res *2 + int(inp[j])
        cnt += 1
        j += 1
    print(res, end=" ")