import pytest

from grades import letter_grade


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (0, "F"),
        (59, "F"),
        (60, "D"),
        (69, "D"),
        (70, "C"),
        (79, "C"),
        (80, "B"),
        (89, "B"),
        (90, "A"),
        (100, "A"),
    ],
)
def test_letter_grade_boundaries(score, expected):
    assert letter_grade(score) == expected


@pytest.mark.parametrize("score", [-1, 101])
def test_out_of_range_scores_are_rejected(score):
    with pytest.raises(ValueError):
        letter_grade(score)
