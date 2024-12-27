from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15



numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 120



numbers = [1, 5, 3, 9, 2]
result = reduce(lambda x, y: x if x > y else y, numbers)
print(result)  # Output: 9



strings = ["Hello", " ", "World", "!"]
result = reduce(lambda x, y: x + y, strings)
print(result)  # Output: "Hello World!"



lists = [[1, 2], [3, 4], [5]]
result = reduce(lambda x, y: x + y, lists)
print(result)  # Output: [1, 2, 3, 4, 5]
