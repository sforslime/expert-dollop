""" 7. write a recursive searching algorithm to search for a number entered by user in a list of numbers. """

def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return -1
    if numbers[index] == target:
        return index
    return recursive_search(numbers, target, index + 1)

numbers = [5, 12, 7, 23, 45, 8, 19, 34]
user_number = int(input("\n7. Enter a number to search: "))
result = recursive_search(numbers, user_number)
if result != -1:
    print(f"   Found at position {result}")
else:
    print(f"   Not found in list")