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
    i = j = 0

    while i < len(arr1) or j <len(arr2):
        if i < len(arr1) and j < len(arr2):
            if arr1[i]  <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        elif i < len(arr1):
            result.append(arr1[i])
            i += 1
        elif j < len(arr2):
            result.append(arr2[j])
            j += 1
    return result

arr = [5, 2, 4, 1, 7, 8, 9, 6, 3]
print(merge_sort(arr))