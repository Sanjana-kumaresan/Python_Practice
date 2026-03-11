"""Functions for organizing and calculating student exam scores."""

def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores
    :return: list - student scores rounded to nearest integer
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students.

    :param student_scores: list - containing int student scores
    :return: int - number of students with score <= 40
    """
    return len([score for score in student_scores if score <= 40])


def above_threshold(student_scores, threshold):
    """Return scores that are above or equal to threshold.

    :param student_scores: list - student scores
    :param threshold: int - threshold value
    :return: list - scores >= threshold
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create grade thresholds.

    :param highest: int - highest possible score
    :return: list - lower threshold scores for each grade
    """
    step = (highest - 40) // 4
    return [41, 41 + step, 41 + 2 * step, 41 + 3 * step]


def student_ranking(student_scores, student_names):
    """Create a list of ranked students.

    :param student_scores: list - student scores
    :param student_names: list - student names
    :return: list - ranking strings
    """
    result = []
    for i in range(len(student_scores)):
        result.append(f"{i + 1}. {student_names[i]}: {student_scores[i]}")
    return result


def perfect_score(student_info):
    """Return first student who scored 100.

    :param student_info: list of tuples (student_name, score)
    :return: tuple - first student with score 100
    """
    for student in student_info:
        if student[1] == 100:
            return student
    return []