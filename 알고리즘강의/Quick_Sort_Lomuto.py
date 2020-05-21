def quick_sort(arr, left, right):
    if left < right:
        pivot = lomuto_partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)

def lomuto_partition(arr, left, right):
    # 맨 오른쪽 요소를 pivot으로 설정하고 i= left -1, j = 0
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        # arr[j]가 pivot보다작으면,
        if arr[j] < pivot:
        #i를 1 증가
        # arr[j], arr[i] 위치 교환
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    #i가 가리키는 위치가 pivot보다 작은 값의 마지막 인덱스
    #i+1의 위치에 pivot을 두고 i+1 반환
    arr[i+1], arr[right] =  arr[right], arr[i+1]
    return i+1

arr = [4, 5, 1, 2, 9, 8, 3, 6, 7]
quick_sort(arr, 0, len(arr)-1)
print(arr)