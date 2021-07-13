from programs.best_conjugation import get_conjugate
from programs.route_planner import get_route
from programs.numbers_to_words import get_number_words


def test_get_conjugate():
    test_cases = {
        "Awesomeness": ["Awe", "Some", "Ness"],
        "Something": ["Some", "Thing"],
        "Disproportionate": ["Dis", "Pro", "Port", "Ion", "Ate"],
    }

    for word, expected_result in test_cases.items():
        assert get_conjugate(word) == expected_result


def test_get_route():
    assert get_route("0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15") in ("0 4 6 9 13 15", "0 2 6 9 11 15")


def test_get_number_words():
    test_cases = {
        123: "One hundred and twenty three",
        5011: "Five thousand and eleven",
        923341573943234: "Nine hundred and twenty three trillion, three hundred and forty one billion, five hundred and seventy three million, nine hundred and forty three thousand two hundred and thirty four",
    }

    for num, expected_result in test_cases.items():
        assert get_number_words(num) == expected_result
