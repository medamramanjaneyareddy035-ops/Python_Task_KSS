#* Remove Duplicates: Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.

numbers = [1,2, 3, 2, 4, 1, 5, 3]

result = []

for num in numbers:
    if num not in result:
        result.append(num)
print(result)        
