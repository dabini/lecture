class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr): #리스트 삽입(swea 수열합치기)
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new

    if lst.head is None: #빈 리스트 일경우
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: #데이터가 리스트[0]보다 클 경우
                break
            cur = cur.next
        if cur is None: #마지막에 추가
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur == lst.head: #맨 앞에 추가 #cur.prev is None으로 해도 됨
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:#중간에 추가
            prev = cur.prev #이전 노드 정보를 저장..?
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr) #리스트의 개수만큼 노드의 수 추가


def addLast(lst, new): #원소 삽입
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        #새로 추가되는 노드에 대해서 먼저 연결고리를 설정하는 게 오류가 나지 않음..
        new.prev = lst.tail
        #아래 두개 순서가 바뀌면 안됨
        lst.tail.next = new
        lst.tail = new
    lst.size += 1

def printList(lst):
    if lst.head is None:
        return
    #처음부터 출력
    cur = lst.head
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    print()
    #뒤에서부터 출력
    cur = lst.tail
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.prev
    print()


mylist = LinkedList()
arr = [1, 3, 5, 7, 9]
for val in arr:
    addLast(mylist, Node(val))
printList(mylist)

addList(mylist, [0, 1, 2])
printList(mylist)
addList(mylist, [4, 4, 4])
printList(mylist)
addList(mylist, [10, 4, 4])
printList(mylist)