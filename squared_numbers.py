def get_squared_numbers(numbers):
  squared_numbers = []
  for number in numbers:
    squared_numbers.append(number*number)
  return squared_numbers


numbers = [2, 4, 6, 8]
squared_numbers = get_squared_numbers(numbers)
print(squared_numbers)