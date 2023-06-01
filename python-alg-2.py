def find_missing_numbers(array):
    found = set(array)
    n = len(array) + 1
    missing_numbers = []

    for num in range(1, n):
        if num not in found:
            missing_numbers.append(num)

    if len(missing_numbers) == 0:
        return "Nothing is missing"
    elif len(missing_numbers) == 1:
        return f"Missing number: {missing_numbers[0]}"
    else:
        return f"Missing numbers: {', '.join(str(num) for num in missing_numbers)}"


# Here I am Prompting the user to input an integer array
user_input = input("Enter an integer array (comma-separated): ")
try:
    arr = [int(num) for num in user_input.split(',')]

    # Checking for negative numbers as asked in the question
    if any(num < 0 for num in arr):
        print("Invalid input, negative number detected")
    else:
        result = find_missing_numbers(arr)
        print(result)
except ValueError:
    print("Invalid input, non-integer value detected")
