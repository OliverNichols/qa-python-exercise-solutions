def get_isbn(number: int):

    result = 0

    for i, digit in enumerate(map(int, str(number))):

        if not i % 2:  # even
            result += digit
        else:
            result += digit * 3

    result = 10 - result % 10

    return result
