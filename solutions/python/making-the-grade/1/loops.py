"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores."""
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students."""
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return scores that are at or above the threshold."""
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create grade thresholds."""
    step = (highest - 40) // 4
    return [41, 41 + step, 41 + 2 * step, 41 + 3 * step]


def student_ranking(student_scores, student_names):
    """Return ranking list."""
    result = []
    for i in range(len(student_scores)):
        result.append(f"{i+1}. {student_names[i]}: {student_scores[i]}")
    return result


def perfect_score(student_info):
    """Return first student with perfect score."""
    for student in student_info:
        if student[1] == 100:
            return student
    return []