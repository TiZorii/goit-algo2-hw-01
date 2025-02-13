import random

def quick_select(arr, k):
    if len(arr) == 1:  
        return arr[0]

    pivot = random.choice(arr)  

    left = [x for x in arr if x < pivot]    
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot]   

    if k <= len(left):  
        return quick_select(left, k) 
    elif k <= len(left) + len(middle):
        return pivot  
    else:
        return quick_select(right, k - len(left) - len(middle)) 

numbers = [6, 7, 10, 4, 3, 20, 15, 11, 1]
k = 4
result = quick_select(numbers, k)
print(f"{k}-th smallest element: {result}")
