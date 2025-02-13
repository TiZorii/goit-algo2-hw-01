def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0] 
    
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1])) 
    
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

numbers = [3, 1, 9, 2, 7, 8, 5, 4]
min_value, max_value = find_min_max(numbers)
print(f"Minimum: {min_value}, Maximum: {max_value}")
