# def isEmpty():
#     return front == rear
#
#
# def isFull():
#     return (rear + 1) % len(cQ) == front
#
#
# def enQueue(item):  # 원형 큐의 삽입 연산
#     global rear
#     if isFull():
#         print("Queue_Full")
#     else:
#         rear = (rear + 1) % len(cQ)
#         cQ[rear] = item
#
#
# def deQueue():  # 원형 큐의 삭제 연산
#     global front
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         front = (front + 1) % len(cQ)
#         return cQ[front]
#
#
# cQ_size = 3
# cQ = [0] * cQ_size
#
# # front, rear를 0으로 초기화
# front = rear = 0
#
# enQueue('A')
# enQueue('B')
# enQueue('C')
# print(deQueue())
# print(deQueue())
# print(deQueue())



#원형큐
# def enQueue(item):
#     queue.append(item)
#
#
# def deQueue():
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         return queue.pop(0)
#
#
# def isEmpty():
#     return len(queue) == 0
#
#
# def Qpeek():
#     if isEmpty():
#         print("Queue_Empty")
#     else:
#         return queue[0]
#
#
# queue = []
# # fornt = -1
# # rear: len(queue) -1
#
# enQueue("A")
# enQueue("B")
# enQueue("C")
# print(deQueue())
# print(deQueue())
# print(deQueue())



#연결 큐
# class Node:
#     def __init__(self, item, n=None):
#         self.item = item
#         self.next = n
#
#
# def enQueue(item):
#     global front, rear
#     newNode = Node(item)
#     if front == None:
#         front = newNode
#     else:
#         rear.next = newNode
#     rear = newNode
#
#
# def isEmpty():
#     return front== None
#
#
# def deQueue():
#     global front, rear
#     if isEmpty():
#         print("Queue_Empty")
#         return None
#     item = front.item
#     front = front.next
#     if front == None:
#         rear = None
#     return item
#
#
# def Qpeek():
#     return front.item
#
#
# def printQ():
#     f = front
#     s = ""
#     while f:
#         s += f.item + ""
#         f = f.next
#     return s
#
#
# front = None
# rear = None
#
# enQueue("A")
# enQueue("B")
# enQueue("C")
# printQ()
# print(deQueue())
# print(deQueue())
# print(deQueue())


#큐 모듈 활용
#선입선출의 큐 개념을 구현한 큐 클래스 활용

import queue
q = queue.Queue() #FIFO 구조 큐 생성
q.put('A')
q.put('B')
q.put('C')

while not q.empty():
    print(q.get())