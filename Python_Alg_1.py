def is_palindrome(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1

    return True

# Prompt the user to input a string
user_input = input("Enter a word to check if it's a palindrome: ")

# This will call the is_palindrome function with the user's input
result = is_palindrome(user_input)

# Display the result
if result:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome.")

# Test cases user can comment out this code to ignore it and prevent it showing up in the terminal.
stringA = "radar"
print(is_palindrome(stringA))  # Output: True

stringB = "level"
print(is_palindrome(stringB))  # Output: True

stringC = "Pencil"
print(is_palindrome(stringC))  # Output: False

stringD = "a"
print(is_palindrome(stringD))  # Output: True

