#6. Multi-Level List Transformation (Advanced List Comprehension) 
'''A dataset contains: 
data = [[1, 2, 3], [4, 5], [6]] 
Task: 
● Flatten the list using list comprehension. 
● Then create a new list containing squares of only even numbers.
'''
data = [[1, 2, 3], [4, 5], [6]]

# Step 1: Flatten the list
flat_list = [num for sublist in data for num in sublist]

# Step 2: Find squares of even numbers
even_squares = [num**2 for num in flat_list if num % 2 == 0]

print("Original List:", data)
print("Flattened List:", flat_list)
print("Squares of Even Numbers:", even_squares)
