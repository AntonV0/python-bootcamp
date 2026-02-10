"""Exercises: dictionaries, lists, and sets."""

# ! Exercise 1: Word frequency (dictionary)

SENTENCE = "This is a sentence. This tests the word frequency in this sentence."
# Normalise case and remove punctuation
SENTENCE = SENTENCE.lower().replace('.', '')

words = SENTENCE.split()  # Split sentence into words
word_count = {}  # Initialise empty dictionary

for word in words:  # Count occurrences of each word
    word_count[word] = word_count.get(word, 0) + 1  # Increment count

print(word_count)  # ? Output:
# ? {'this': 3, 'is': 1, 'a': 1, 'sentence': 2, 'tests': 1, 'the': 1, 'word': 1, 'frequency': 1, 'in': 1}

# ! -------------------------------------------------------------

# ! Exercise 2: To-Do list (list of dictionaries)

todo_list = []  # Initialise empty to-do list


def add_task(description):
    """Add a new task to the to-do list."""
    todo_list.append({"description": description,
                     "completed": False})  # Add task as a dictionary


def complete_task(index):
    """Mark a task as completed."""
    if 0 <= index < len(todo_list):  # Check for valid index
        todo_list[index]["completed"] = True  # Mark task as completed


def view_all_tasks():
    """Return a list of pending tasks."""
    return [task["description"] for task in todo_list if not task["completed"]]  # Filter pending tasks


add_task("Buy groceries")
add_task("Read a book")
add_task("Go for a walk")
complete_task(1)  # Mark "Read a book" as completed
print(view_all_tasks())  # ? Output: ['Buy groceries', 'Go for a walk']

# ! -------------------------------------------------------------

# ! Exercise 3: Using Sets for unique items

math_id_set = {101, 102, 103, 104, 105, 109, 110}
science_id_set = {104, 105, 106, 107, 108, 110}

# Find students in both subjects using sets
both_subjects_set = math_id_set & science_id_set
print(both_subjects_set)  # Output: {104, 105, 110}

# Find all unique students enrolled in either course
all_students_set = math_id_set | science_id_set
print(all_students_set)
# Output: {101, 102, 103, 104, 105, 106, 107, 108, 109, 110}

# Find students enrolled in maths but not in science
math_only_set = math_id_set - science_id_set
print(math_only_set)  # Output: {101, 102, 103, 109}

# ! -------------------------------------------------------------

# ! Exercise 4: Diagram of dictionary with nested structures

user = {'id': 101, 'name': 'Alice', 'roles': ['editor', 'viewer']}
# user -> dictionary
# --- 'id'    -> 101
# --- 'name'  -> "Alice"
# --- 'roles' -> list
# ---  --- [0] -> "editor"
# ---  --- [1] -> "viewer"
