# Linked List 과제



### 1. 5108 숫자추가

```python
T= int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    lst = list(map(int, input().split()))
    for m in range(M):
        idx, num = map(int, input().split())
        lst.insert(idx, num)

    print("#{} {}".format(t+1, lst[L]))
```



### 2. 5122 수열편집

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:
    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node

        self.before = None
        self.current = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        self.tail.link = new_node
        self.tail = new_node

    def move_to(self, D):
        self.current = self.head.link
        self.before = self.head
        for _ in range(D):
            if self.current == None:
                return False
            self.before = self.current
            self.current = self.current.link
        return True

    def insert(self, idx, data):
        new_node = Node(data)
        self.move_to(idx)
        self.before.link = new_node
        new_node.link = self.current

    def delete(self, idx):
        self.move_to(idx)
        self.before.link = self.current.link

    def change(self, idx, data):
        self.move_to(idx)
        self.current.data = data

    def my_result(self, idx):
        if self.move_to(idx):
            return self.current.data
        else:
            return -1


T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    lst = LinkedList()
    for i in map(int, input().split()):
        lst.append(i)
    for _ in range(M):
        data = list(input().split())
        if data[0] == 'I':
            lst.insert(int(data[1]), int(data[2]))
        elif data[0] == 'D':
            lst.delete(int(data[1]))
        else:
            lst.change(int(data[1]), int(data[2]))
    print('#{} {}'.format(t+1, lst.my_result(L)))

```

