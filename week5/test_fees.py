import pytest

from fees import Course, StudentType, fee_report, process_all, tuition_fee
from legacy_fees import calc


def legacy_courses(*hours):
    return [{"h": hour} for hour in hours]


def courses(*hours):
    return [Course(hour) for hour in hours]


def student(name, kind):
    return {
        "name": name,
        "type": kind,
        "courses": legacy_courses(3),
        "summer": False,
    }


@pytest.mark.parametrize(
    ("hours", "legacy_type", "student_type", "summer"),
    [
        ((3, 3, 3), 1, StudentType.REGULAR, False),
        ((3, 3, 3, 3, 3, 3), 1, StudentType.REGULAR, True),
        ((3, 4), 2, StudentType.STAFF_CHILD, False),
        ((3, 3), 3, StudentType.SCHOLARSHIP, True),
    ],
)
def test_same_result_as_legacy(hours, legacy_type, student_type, summer):
    old_result = calc(legacy_courses(*hours), legacy_type, 2026, summer, None)
    new_result = tuition_fee(courses(*hours), student_type, summer)
    assert new_result == old_result


def test_large_fee_gets_reduction():
    assert tuition_fee(courses(6, 6, 6), StudentType.REGULAR) == 6100


def test_scholarship_student_is_not_skipped():
    students = [
        student("Sara", StudentType.REGULAR),
        student("Omar", StudentType.SCHOLARSHIP),
    ]
    assert process_all(students) == {"Sara": 1050, "Omar": 0}


def test_scholarship_first_in_list_is_zero():
    assert process_all([student("Omar", StudentType.SCHOLARSHIP)]) == {"Omar": 0}


def test_extras_are_added_without_mutating_a_default():
    assert tuition_fee(courses(1), StudentType.REGULAR, extras=(25, 50)) == 425
    assert tuition_fee(courses(1), StudentType.REGULAR) == 350


def test_fee_report_returns_text():
    assert fee_report(courses(3), StudentType.REGULAR) == "Student fee: 1050"


def test_staff_child_rate_is_half():
    assert tuition_fee(courses(2), StudentType.STAFF_CHILD) == 350
