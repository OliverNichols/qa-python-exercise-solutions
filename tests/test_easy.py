from programs.grade_calculator import get_grade
from programs.isbn import get_isbn
from programs.near import get_near
from programs.times_tables import get_times_tables


def test_get_grade():
    test_cases = (
        ((10, 10, 10), "You failed"),
        ((30, 50, 45), "D"),
        ((50, 50, 50), "C"),
        ((60, 80, 40), "B"),
        ((90, 100, 85), "A"),
    )

    for marks, expected_results in test_cases:
        assert get_grade(*marks) == expected_results


def test_get_isbn():
    assert get_isbn(978030640615) == 7


def test_get_near():
    assert get_near("reset", "rest") == True
    assert get_near("dragoon", "dragon") == True
    assert get_near("eave", "leave") == False
    assert get_near("sleet", "lets") == False


def test_get_times_tables():
    assert get_times_tables(3) == "1\t2\t3\n2\t4\t6\n3\t6\t9"
