#* Common Elements Using Sets: Given two lists:
 
''' ```python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    ```
 
    Find:
 
    * Common elements.
 
    * Elements present only in the first list.
 
    * All unique elements from both lists.
 '''
#Common elemts
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = set(list1)&set(list2)

print(result)

#Elements present only in the first list.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = set(list1)-set(list2)

print(result)

#All unique elements from both lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = set(list1)|set(list2)

print(result)
