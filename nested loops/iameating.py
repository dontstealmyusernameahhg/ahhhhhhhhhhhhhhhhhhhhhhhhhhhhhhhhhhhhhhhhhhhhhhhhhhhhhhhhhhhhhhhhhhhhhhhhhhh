string = input("Enter a string: ")
char = input("Enter a character to count: ")
count = 0
i = 0
while (i < len(string)):
    if (string[i] == char):
        count += 1
    i += 1
print(f"The character '{char}' appears {count} times in the string.")
# This code counts the occurrences of a specified character in a given string.  # It uses a while loop to iterate through each character in the string and increments a counter when a match is found.
# The user is prompted to input a string and a character, and the result is printed at the end.# The code is simple and effective for counting character occurrences in a string.
# It can be useful for tasks such as text analysis or data processing where character frequency is relevant.# The code is straightforward and easy to understand, making it suitable for beginners in programming.
# The code is efficient for small strings, but for larger strings, using built-in methods like string.count() would be more optimal.   # Overall, this code serves as a basic example of string manipulation and character counting in Python.
# The code is functional and meets the requirements of counting character occurrences in a string.# It can be further optimized or modified for specific use cases, such as case-insensitive counting or counting multiple characters at once.
# The code is a good starting point for learning about loops and string manipulation in Python.# It demonstrates the use of a while loop, string indexing, and conditional statements.
# The code can be extended to include additional features, such as counting multiple characters or ignoring case sensitivity.