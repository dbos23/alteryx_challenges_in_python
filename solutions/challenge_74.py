# numbers provided as the input in the Alteryx workflow
nums = [1, 2, 3, 4, 5, 10]

# calculates the factorial of an input number
def calc_factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result

# print result
for num in nums:
    print(f'The factorial of {num} is {calc_factorial(num)}')