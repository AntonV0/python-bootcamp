"""Assignment: Calculating Mean, Median and Mode Outside from Stats Pack Module."""

from stats_pack.calculations import find_mean, find_median, find_mode

sample_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
# Repeated 5 to test mode calculation

sample_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# No repeated numbers (no mode)

sample_list3 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
# Repeated 5 and 9 to test multiple modes


def run_stats():
    """Run the stats calculations and print results."""
    print("Sample List 1:", sample_list)
    print("Mean:", find_mean(sample_list))
    print("Median:", find_median(sample_list))
    print("Mode:", find_mode(sample_list))

    print("\nSample List 2:", sample_list2)
    print("Mean:", find_mean(sample_list2))
    print("Median:", find_median(sample_list2))
    print("Mode:", find_mode(sample_list2))

    print("\nSample List 3:", sample_list3)
    print("Mean:", find_mean(sample_list3))
    print("Median:", find_median(sample_list3))
    print("Mode:", find_mode(sample_list3))


if __name__ == "__main__":
    run_stats()

# ? Output:
# Sample List 1: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
# Mean: 5.0
# Median: 5.0
# Mode: 5

# Sample List 2: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Mean: 5.0
# Median: 5
# Mode: None

# Sample List 3: [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]
# Mean: 5.363636363636363
# Median: 5
# Mode: [5, 9]
