import array as arr


arr1 = arr.array('i', [1, 2, 3])

for i in range(0, len(arr1)):
  pass
  print(arr1[::-1])
# Looping through an arry

x = list(range(1, 25))
new_array = arr.array('i', x)

for i in range(0, len(new_array)):
  pass
  print(new_array[i], end=' ')

print(new_array[5]) # Assessing index 5

# Adding element in an Array

# 1 using insert method
print()
arr1.insert(0, 0)
print('arr1 after inserting 0 at arr1[0] = ',arr1)

# 2 using append method
print()
arr1.append(6)
print('arr1 after appending 6  = ',arr1)

# 3 using extend method 
print()
arr1.extend([7, 8])
print('arr1 using expand method  = ',arr1)

# Deleting an element from an array

# 1 using pop method
arr2 = arr.array('i', [1, 2, 3, 4])
print()
arr2.pop()
print('arr2 using pop method = ',arr2)

# alse pop method with arg
print()
arr2.pop(1) # to remove element at endex 1
print('arr2 using pop method with arg = ',arr2)
