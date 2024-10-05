# Time grows proportionally

nums = [1, 2, 3]
sum(nums)  # sum of Array

for n in nums:  # Looping
  print(n)



nums.insert(1, 100)  # Insert middle (Array)
nums.remove(100)     # Remove middle (Array)
print(100 in nums)   # Search


import heapq
result = heapq.heapify(nums)    # Build heap

# Sometimes even nested loops can be O(n)
# eg Monotonic stack or sliding window
 