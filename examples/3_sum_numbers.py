
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    result = sum_numbers(numbers)
    print(result)
