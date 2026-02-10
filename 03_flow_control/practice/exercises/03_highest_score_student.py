"""Iterating Through Dictionaries to Find the Highest Score Student."""

student_scores = {
    "Alice": 78,
    "Bob": 95,
    "Charlie": 82,
    "Diana": 55,
    "Ethan": 40
}

def highest_score_student(students_scores):
    """Return the name of the student with the highest score."""
    highest_score = -1 # initialise highest score
    top_student = "" # initialise top student name

    for student, score in students_scores.items(): # iterate through dictionary items
        if score > highest_score:
            highest_score = score # update highest score
            top_student = student # update top student name

    return top_student

print("The student with the highest score is:", highest_score_student(student_scores))
# Output: The student with the highest score is: Bob
