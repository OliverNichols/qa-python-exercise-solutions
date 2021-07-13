def get_times_tables(number):

    result = ""

    for i in range(1, number + 1):
        for j in range(1, number + 1):

            result += str(i * j)
            if j != number:
                result += "\t"

        if i != number:
            result += "\n"

    return result
