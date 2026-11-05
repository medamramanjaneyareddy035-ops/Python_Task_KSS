# Write a function to find the sum of elements in a list using a user-defined function.
def find_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [10, 20, 30, 40, 50]

result = find_sum(my_list)

print("Sum of elements in the list:", result)
