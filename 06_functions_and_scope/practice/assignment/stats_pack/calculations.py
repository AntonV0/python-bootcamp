"""Functions for stats pack calculations."""


def find_mean(data_list):
    """Calculate the mea (average) of a list of numbers."""
    if not data_list:  # Check if the list is empty to avoid division by zero
        return 0
    return sum(data_list) / len(data_list)


def find_median(data_list):
    """Calculate the median (middle value) of a list of numbers."""
    if not data_list:
        return 0
    # Sort the list by default in ascending order
    sorted_list = sorted(data_list)
    n = len(sorted_list)  # Get the number of elements in the list
    mid = n // 2  # Calculate the middle index
    if n % 2 == 0:  # Even number of elements
        # Average of the two middle values
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:  # Odd number of elements
        # Return the middle value
        return sorted_list[mid]


def find_mode(data_list):
    """Calculate the mode (most frequent value) of a list of numbers."""
    if not data_list:
        return None
    frequency = {}  # Dictionary to count frequency of each number
    for num in data_list:
        frequency[num] = frequency.get(num, 0) + 1  # Increment count
    max_freq = max(frequency.values())  # Find the maximum frequency
    # Get all numbers with max frequency
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    if len(modes) == len(frequency):  # If all numbers are equally frequent, there is no mode
        return None
    if len(modes) == 1:  # If there is only one mode, return it as a single value
        return modes[0]
    return modes  # If there are multiple modes, return the list of modes
