def convert(num):
    if num.isdigit():
        num = int(num)
    else:
        num = 10 + ord(num.upper()) - ord('A')

    #10진수를 2진수 문자열로 변환하는 코드 1
    temp = ""
    for j in range(3, -1, -1):
        if num & (1<<j):
            temp += '1'
        else:
            temp += '0'
    return temp
    #10진수를 2진수 문자열로 변환하는 코드 2
    # t = [0] * 4
    # for j in range(4):
    #     t[3-j] = str((num >> j) & 1)

hex = input()
bin = ''
for i in range(len(hex)):
    tmp = convert(hex[i])
    bin += tmp
print(bin)
