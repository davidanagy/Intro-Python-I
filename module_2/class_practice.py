# def centered_average(arr):
#     arr2 = arr.copy()
#     arr_max = max(arr2)
#     arr_min = min(arr2)
#     arr2.remove(arr_max)
#     arr2.remove(arr_min)
#     mean = sum(arr2) // len(arr2)
#     return mean

def centered_average(arr):
    # Go through the list finding largest and smallest,
    # while keeping track of the sum.
    total = 0
    min_value = arr[0]
    max_value = arr[0]
    for num in arr:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
        total += num
    # subtract min/max instead of removing them
    return (total - max_value - min_value) // (len(arr) - 2)
    

arr1 = [1,2,3,4,100]
arr2 = [1,1,5,5,10,8,7]
arr3 = [-10,-4,-2,-4,-2,0]

print(centered_average(arr1))
print(centered_average(arr2))
print(centered_average(arr3))
