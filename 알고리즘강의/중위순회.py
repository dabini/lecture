def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][1])
        print("%c" %tree[T][0], end='')
        inorder_traverse(tree[T][2])

n = int(input())
tree = [[0]*3 for _ in range(n+1)]

templ = list(map(int, input().split()))

for i in range(1, n+1):
    templ = input().split()
    tree[i][:len(templ)-1 ] = tree[1:len(templ)]

inorder_traverse(1)
print()
