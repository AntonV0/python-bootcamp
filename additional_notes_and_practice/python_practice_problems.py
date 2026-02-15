"""Python Practice Problems"""


# ! 1.) Count frequency of each character (ignore spaces)
# ? Input: "data science"
# ? Output: {'d':1, 'a':2, 't':1, ...}


def count_frequency(string):
    """Counts the frequency of each character in the given string, ignoring spaces."""
    frequency = {}  # Create an empty dictionary to store the frequency of characters
    for char in string:
        if char != ' ':  # If character is empty, ignore spaces
            if char in frequency:  # If character is in the frequency dictionary, increment
                frequency[char] += 1
            else:  # If character is not in the frequency dictionary, add it with count 1
                frequency[char] = 1
    return frequency


print(count_frequency("data science"))
# ? Output: {'d': 1, 'a': 2, 't': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}

# ! ------------------------------------------------------------------------------------------------

# ! 2.) Check if two strings are anagrams
# ? listen → silent → True


def are_strings_anagrams(string1, string2):
    """Checks if two strings are anagrams of each other."""

    # # sorted() function returns a sorted list of the characters in the string
    return sorted(string1) == sorted(string2)  # Comparing both string


print(are_strings_anagrams("listen", "silent"))  # ? Output: True
print(are_strings_anagrams("hello", "world"))    # ? Output: False

# ! ------------------------------------------------------------------------------------------------

# ! 3.) Find first non-repeating character
# ? Input: "programming"
# ? Output: "p"


def first_non_repeating_character(string):
    """Finds the first non-repeating character in the given string."""
    frequency = {}  # Create an empty dictionary to store the frequency of characters
    for char in string:
        if char in frequency:  # If character is already in the frequency dictionary, increment
            frequency[char] += 1
        else:  # If character is not in the frequency dictionary, add it with count 1
            frequency[char] = 1

    for char in string:  # Iterate through string again to find the first non-repeating character
        # If the frequency of the character is 1, it means it is non-repeating
        if frequency[char] == 1:
            return char  # Return the first non-repeating character
    return None  # Explicit return if no non-repeating character is found


print(first_non_repeating_character("programming"))
# ? Output: "p"

# ! ------------------------------------------------------------------------------------------------

# ! 4.) Reverse words without reversing sentence order
# ? Input: "Python is easy"
# ? Output: "nohtyP si ysae"


def reverse_words(string):
    """Reverses each word in the given string without changing the order of the words."""
    words = string.split()  # Split the string into a list of words
    reverse = [word[::-1] for word in words]  # Reverse each word using slicing
    # ::1 means to reverse the string. The first : means to take the whole string,
    # the second : means to take every character, -1 means to take the characters in reverse order.
    return ' '.join(reverse)  # Join the reversed words back into a string.
    # String starts with a space and then we join the reversed words with a space in between them.
    # Strings are immutable in Python, so the original string cannot be changed.
    # A new string will be created with the reversed words.


print(reverse_words("Python is easy"))
# ? Output: "nohtyP si ysae"

# ! ------------------------------------------------------------------------------------------------

# ! 5.) Rotate list by k positions
# ? [1,2,3,4,5], k=2
# ? Output: [4,5,1,2,3]


def rotate_list(list1, k):
    """Rotates the given list by k positions to the right."""
    return list1[-k:] + list1[:-k]  # Rotate the list by slicing and concatenating
    # Slicing rule for list slicing: list[start:stop:step]
    # The list1[-k:] gives the last k elements of the list
    # (the elements that will be moved to the front of the list),
    # and the list1[:-k] gives the elements of the list except the last k elements
    # (the elements that will be moved to the back of the list).
    # This slices the list into two parts: the last k elements and the rest of the elements.
    # By concatenating these two slices (with the + operator), we get the rotated list.


print(rotate_list([1, 2, 3, 4, 5], 2))
# ? Output: [4, 5, 1, 2, 3]

# ? Explanation:
# The original list is [1, 2, 3, 4, 5] and we want to rotate it by 2 (k) positions to the right.
# The last 2 elements of the list are [4, 5] (moved to the front of the list with list1[-k:]).
# Rest of the elements of the list are [1, 2, 3] (moved to the back of the list with list1[:-k]).
# By concatenating these two parts, we get the rotated list: [4, 5] + [1, 2, 3] = [4, 5, 1, 2, 3].

# ! ------------------------------------------------------------------------------------------------

# ! 6.) Flatten a nested list
# ? [1,[2,3],[4,[5,6]]] → [1,2,3,4,5,6]


def flatten_list(nested_list):
    """Flattens a nested list into a single list."""
    flat_list = []  # Create an empty list to store the flattened elements
    for item in nested_list:  # Iterate through each item in the nested list
        # isinstance() function checks if the item is an instance of a specified type (here, list)
        if isinstance(item, list):  # If the item is a list, we need to flatten it
            # Flatten the sublist and extend the flat_list with its elements
            flat_list.extend(flatten_list(item))
            # The extend() method adds the elements of the flattened sublist to the flat_list.
        else:  # If the item is not a list, we can directly add it to the flat_list
            flat_list.append(item)  # Append the non-list item to the flat_list
    return flat_list  # Return the flattened list


print(flatten_list([1, [2, 3], [4, [5, 6]]]))
# ? Output: [1, 2, 3, 4, 5, 6]

# ? Explanation:
# The original nested list is [1, [2, 3], [4, [5, 6]]].
# 1st item is 1, which is not a list, so it is added to the flat_list using the append() method.
# 2nd item is [2, 3], which is a list, so we need to flatten it using recursion.
# Recursion is a programming technique where a function calls itself in order to solve a problem.
# In this case, the flatten_list() function calls itself to flatten the sublist [2, 3].
# The flattened version of [2, 3] is added to the flat_list using the extend() method.
# 3rd item is [4, [5, 6]], which is also a list, so we need to flatten it using recursion as well.
# Recursion will call the flatten_list() function.
# It will flatten until we reach the innermost nested level/list [5, 6].
# The flattened version of [4, [5, 6]] is added to the flat_list using the extend() method.
# Finally, the flat_list contains all the elements from the original nested list in a single list.

# ! ------------------------------------------------------------------------------------------------

# ! 7.) Group words by length
# ? ["cat","dog","tiger","lion"]
# ? Output:
# ? {
# ?   3:['cat','dog'],
# ?   5:['tiger'],
# ?   4:['lion']
# ? }


def group_words_by_length(words):
    """Groups words by their length."""
    grouped_words = {}  # Create an empty dictionary to store the grouped words
    for word in words:  # Iterate through each word in the list of words
        word_length = len(word)  # Get the length of the word
        # If the length in the grouped dictionary is already a key (already exists),
        if word_length in grouped_words:
            # append the word to the list of words for that length
            grouped_words[word_length].append(word)
        # If the length is not a key in the grouped dictionary,
        # create a new key with the length and set its value to a list containing the word
        else:
            grouped_words[word_length] = [word]
    return grouped_words  # Return the dictionary containing the grouped words


print(group_words_by_length(["cat", "dog", "tiger", "lion"]))
# ? Output:
# ? {
# ?   3:['cat','dog'],
# ?   5:['tiger'],
# ?   4:['lion']
# ? }
