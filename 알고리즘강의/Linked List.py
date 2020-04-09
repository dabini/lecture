# class Node:
#     def __init__(self, d=0, n=None):
#         self.data = d
#         self.next = n
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#         self.tail = None
#
#
# lst = LinkedList()
#
# def printList(lst):
#     if lst.head is None:
#         return
#
#     cur = lst.head #cur에 lst의 주소를 붙여놓음
#     while cur is not None:
#         print(cur.data)
#         cur = cur.next
#
# def insertLast(lst, new):
#     if lst.head is None:
#         lst.head = lst.tail = new
#     else:
#         lst.tail.next = new
#         lst.tail = new
#     lst.size += 1
#
# def insertFirst(lst, new):
#     if lst.head is None:
#         lst.head = lst.tail = new
#     else:
#         new.next = lst.head
#         lst.head = new
#
#
# def deleteLast(lst):
#     if lst.head is None:
#         return
#     cur = lst.head
#     while cur.next is not None:
#         pre = cur
#         cur = cur.next
#     if pre is None:
#         lst.head = lst.tail = None
#     else:
#         pre.next = None
#         lst.tail = pre
#     lst.size -= 1
#
# def deleteFirst(lst):
#     if lst.head is None:
#         return
#     else:
#         lst.head = lst.head.next
#         if lst.head is None:
#             lst.tail = None
#         lst.size -=1
#
# def insertAt(lst, idx, new):
#     # 빈리스트일 경우, idx == 0
#     if lst.head is None:
#         insertFirst(lst, new)
#     elif idx >= lst.size:
#         insertLast(lst, new)
#     else:
#         pre, cur = None, lst.head
#         for _ in range(idx):
#             pre = cur
#             cur = cur.next
#         new.next = cur
#         pre.next = new
#         lst.size += 1
#
# def deleteAt(lst, idx):


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.size = 0


    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.size += 1

    def delete(self):
        pop_data = self.current.data

        if self.current is self.tail:
            self.tail = self.before

        self.before.next = self.current.next
        self.current = self.before

        self.size -= 1

        return pop_data

    def first(self):
        if self.size == 0:
            return None
        self.before = self.head
        self.current = self.head.next

        return self.current.data

    def next(self):
        if self.current.next == None:
            return None
        self.before = self.current
        self.current = self.current.next

        return self.current.data

    def size(self):
        return self.size