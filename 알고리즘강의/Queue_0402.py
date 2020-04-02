def enq(n):
    global rear
    if rear == len(q) -1:
        print('Full')
    else:
        rear += 1
        q[rear] = n

q = [0]*3
front = -1
rear = -1

#enq(1) 간단하게 구현하는 법
# rear += 1
# q[rear]= 1

while q:
    front += 1
    print(q[front])

Q = []
Q.append(1)
print(Q.pop(0))