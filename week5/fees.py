"""Tuition fee calculations with a small, explicit data model."""

from dataclasses import dataclass
from enum import Enum


HOURLY_FEE = 350
STAFF_CHILD_RATE = 0.5
HIGH_FEE_LIMIT = 6000
HIGH_FEE_REDUCTION = 200
SUMMER_SURCHARGE = 150


class StudentType(Enum):
    """The fee category assigned to a student."""

    REGULAR = 1
    STAFF_CHILD = 2
    SCHOLARSHIP = 3


@dataclass(frozen=True)
class Course:
    """A course represented by its number of credit hours."""

    hours: int


FEE_RATES = {
    StudentType.REGULAR: 1.0,
    StudentType.STAFF_CHILD: STAFF_CHILD_RATE,
    StudentType.SCHOLARSHIP: 0.0,
}


def tuition_fee(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
    extras: tuple[float, ...] = (),
) -> float:
    """Calculate a student's tuition without printing anything."""
    rate = FEE_RATES[student_type]
    total = sum(course.hours * HOURLY_FEE * rate for course in courses)

    if total > HIGH_FEE_LIMIT:
        total -= HIGH_FEE_REDUCTION
    if summer:
        total += SUMMER_SURCHARGE

    total -= discount
    total += sum(extras)
    return total


def fee_report(
    courses: list[Course],
    student_type: StudentType,
    summer: bool = False,
    discount: float = 0,
) -> str:
    """Return a readable fee report instead of printing from the calculation."""
    amount = tuition_fee(courses, student_type, summer, discount)
    label = {
        StudentType.REGULAR: "Student",
        StudentType.STAFF_CHILD: "Staff child",
        StudentType.SCHOLARSHIP: "Scholarship",
    }[student_type]
    report = f"{label} fee: {amount:g}"
    if amount > HIGH_FEE_LIMIT:
        report += "\nHigh fee"
    return report


def process_all(students: list[dict]) -> dict[str, float]:
    """Calculate fees for all students, including scholarship students."""
    results = {}
    for student in students:
        student_type = student["type"]
        if isinstance(student_type, int):
            student_type = StudentType(student_type)
        course_list = [Course(item["h"]) for item in student["courses"]]
        results[student["name"]] = tuition_fee(
            course_list,
            student_type,
            student.get("summer", False),
        )
    return results
