## Analysis of Algorithms & Divide and Conquer Strategy  

### Welcome! 🙂  

The homework consists of two independent tasks:  
1. **Mandatory Task**: Finding the maximum and minimum elements in an array.  
2. **Optional Task**: Finding the k-th smallest element in an unsorted array.  

---

## Task 1: Finding Maximum and Minimum Elements (Mandatory)  

### Description
Implement a function that finds the maximum and minimum elements in an array using the Divide and Conquer method.  

### Requirements  
Your solution must meet the following criteria:  
- The function should accept an array of numbers of any length.  
- A recursive approach must be used.  
- The function should return a tuple containing two values: `(minimum, maximum)`.  
- The algorithm must have a time complexity of **O(n)**.  

## Task 2: Finding the k-th Smallest Element (Optional)  

### Description
Implement an algorithm to find the k-th smallest element in an unsorted array using the **Quick Select** method.  

### Requirements  
Your solution must meet the following criteria:  
- The function should accept an array of numbers and an integer `k`.  
- The **pivot** element selection approach must be used.  
- The array should not be fully sorted.  
- The expected average time complexity is **O(n)**.  

### Notes  
**Quick Select** is an example of the Divide and Conquer method, but in this case, the Combine step does not require extra work. Once the desired element is found, it is returned immediately.  
