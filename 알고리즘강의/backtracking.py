bit = [0, 0, 0, 0]
def subset(k, n):
    if k==n :
        print(bit)
    else:
        bit[k] = 0
        subset(k+1, n)
        bit[k] =1
        subset(k+1, n)
subset(0, 3)