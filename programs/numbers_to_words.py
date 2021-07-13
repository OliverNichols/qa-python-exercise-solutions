DIGITS = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
TEENS = "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
TENS = "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
MAJORS = "thousand", "million", "billion", "trillion"


def get_number_words(num):

    digits = list(map(int, str(num)))

    result = ""
    terms = []

    for i, digit in enumerate(digits):
        power = len(digits) - i

        if power % 3 == 0:
            if digit:
                terms.extend([DIGITS[digit - 1], "hundred", "and"])

        elif (power + 1) % 3 == 0:
            if digit:
                if digit == 1 and digits[i + 1]:
                    terms.append(TEENS[digits[i + 1] - 1])

                else:
                    terms.append(TENS[digit - 1])

        else:
            if digit and not (terms and terms[-1] in TEENS):
                terms.append(DIGITS[digit - 1])

            if terms:
                if power // 3:
                    terms.append(MAJORS[power // 3 - 1])

                elif result and "and" not in terms:
                    terms.insert(0, "and")

                if result and power // 3:
                    result = f"{result}, {' '.join(terms)}"

                else:
                    result = f"{result} {' '.join(terms)}".lstrip()

                terms.clear()

    return result.capitalize()
