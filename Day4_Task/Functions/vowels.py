#. Write a function that takes a string as input and returns the number of vowels.
def count_vowels(string):
    count = 0
    for ch in string:
        if ch.lower() in "aeiou":
            count += 1
    return count

text = input("Enter a string: ")

result = count_vowels(text)

print("Number of vowels:", result)
