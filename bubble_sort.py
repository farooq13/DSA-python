my_array = [30, 50, 23, 42, 5, 6, 8, 1, 2]
n = len(my_array)

for i in range(n-1):
  for j in range(n-i-1):
    if my_array[j] > my_array[j+1]:
      my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted Array: ", my_array)