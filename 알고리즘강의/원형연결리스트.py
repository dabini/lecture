class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        #tail은 사용하지 않음!

def addLast(lst, new):
    if lst.head is None: #빈리스트 일 경우
        lst.head = new #head에 new를 저장
        new.prev = new.next = new #node가 하나일 경우에 자기자신을 가리키게 함 ==> None이 있으면 안됨
    else: #마지막에 추가
        tail = lst.head.prev #첫번째 노드의 이전노드를 꼬리처럼 생각해서 tail에 저장
        new.prev = tail
        new.next = lst.head
        tail.next = new
        lst.head.prev = new
    lst.size += 1

def printList(lst):
    if lst.head is None:
        return
    cur = lst.head
    for _ in range(lst.size): #순방향
        print(cur.data, end=" ")
        cur = cur.next
    print()
    cur = lst.head.prev
    for _ in range(lst.size): #역방향
        print(cur.data, end=" ")
        cur= cur.prev
    print()


mylist = LinkedList()
arr = [6, 2, 4, 9, 1, 5]
for val in arr:
    addLast(mylist, Node(val))

cur = mylist.head
for _ in range(3): #M
    for _ in range(3): #k
        cur = cur.next

    prev = cur.prev
    new = Node(prev.data + cur.data, prev, cur)
    prev.next = new
    cur.prev = new
    cur = new #새로 추가된 위치를 시작 위치로 재설정
    mylist.size += 1

printList(mylist)