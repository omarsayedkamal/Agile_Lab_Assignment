"""Convert a numeric course score into a letter grade."""

MIN_SCORE = 0
MAX_SCORE = 100
A_MIN = 90
B_MIN = 80
C_MIN = 70
D_MIN = 60


def letter_grade(score: int) -> str:
    """Return the letter grade for a score from 0 to 100."""
    if not MIN_SCORE <= score <= MAX_SCORE:
        raise ValueError("score must be between 0 and 100")
    if score >= A_MIN:
        return "A"
    if score >= B_MIN:
        return "B"
    if score >= C_MIN:
        return "C"
    if score >= D_MIN:
        return "D"
    return "F"
