def merge_sort(arr):
    if len(arr) ==  1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(arr1, arr2):
    result = list()

    #병합과정 실행
    #각각의 최솟값들을 (가장 앞쪽값) 비교해서 더 작은 요소를 결과에 추가
    # 두 부분집합의 요소가 없어질 때까지 반복
    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] <= arr2[0]:
                result.append(arr1.pop(0))
            else:
                result.append(arr2.pop(0))
        elif arr1:
            result.append(arr1.pop(0))
        elif arr2:
            result.append(arr2.pop(0))
    return result

arr = [5, 2, 4, 1, 7, 8, 9, 6, 3]
print(merge_sort(arr))