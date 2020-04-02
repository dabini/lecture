num = 20 #마이쮸개수
q = [(1, 0)] #1번이 줄을 서고 아직 받지 않은 상태
j = 1 #새롭게 줄을 서는 사람 번호
last = 0
while num > 0 :
    i, m = q.pop(0)
    m += 1 #이번에 받을 개수
    num -= m #남은 마이쮸 개수
    j += 1 #새로 줄을 서는 사람의 번호
    q.append((i, m))
    q.append((j, 0))
    last = i
print(last)