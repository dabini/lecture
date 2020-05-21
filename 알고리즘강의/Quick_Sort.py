def quick_sort(arr, left, right): #왼쪽 시작점과, 오른쪽 끝지점
    #pivot 위치 결정(피봇을 기준으로 큰값은 오른쪽, 작은 값은 왼쪽으로 구분)
    #왼쪽 부분집합 정렬
    #오른쪽 부분집합 정렬
    if left < right:
        #피봇 구하기
        pivot = hoare_partition(arr, left, right)
        #왼쪽부분집합 정렬 실행
        quick_sort(arr, left, pivot-1)
        #오른쪽 부분집합 정렬 실행
        quick_sort(arr, pivot+1, right)

def hoare_partition(arr, left, right):
    # i, j 를 설정하고, 큰값 찾고 작은값 찾아서 위치 바꿔주기
    i = left
    j = right
    pivot = arr[left]

    # i가 j보다 작을 때까지 반복
    while i <= j:
        #피봇보다 큰 값이 나올때까지 i증가
        while i <= j and arr[i] <= pivot:
            i += 1
        # 피봇보다 작은값이 나올때까지 j감소
        while i <= j and arr[j] >= pivot:
            j -= 1

        # i가 j보다 작으면, 위치 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    return j

arr = [4, 5, 1, 2, 9, 8, 3, 6, 7]
quick_sort(arr, 0, len(arr)-1)
print(arr)