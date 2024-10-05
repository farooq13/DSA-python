# numbers = [2, 3, 4, 5, 3, 4, 5, 7, 2]


# for i in range(len(numbers)):
#   for j in range(i+1, len(numbers)):
#     if numbers[i] == numbers[j]:
#       print(f'{numbers[i]} -----> is a duplicate')
#       break

# USING HashMap
numbers = [2, 3, 4, 5, 3, 4, 5, 7, 2]

def find_duplicates(numbers):
    count_map = {}
    duplicates = []

    for num in numbers:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    for num, count in count_map.items():
        if count > 1:
            duplicates.append(num)
    
    return duplicates

duplicates = find_duplicates(numbers)
print("Duplicates:", duplicates)
