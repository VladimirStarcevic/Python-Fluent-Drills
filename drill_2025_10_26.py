# DRILL 9: Conditional Dictionary Merge (DC & Unpacking)

def conditional_merge(d1: dict, d2: dict) -> dict:
    """Uses DC to filter d1 and Unpacking (**) to merge with d2."""
    filtered_d1 = {k: v for k,v in d1.items() if v > 50}
    return {**filtered_d1, **d2}

d1 = {'A': 90, 'B': 40, 'C': 70}
d2 = {'B': 5, 'D': 100, 'A': 10}
d3 = conditional_merge(d1, d2)
print(d3)


# DRILL 10: Aggregate Points
def aggregate_points(pairs: list) -> dict:
    """Aggregates points by name using a classical for loop and dict.get()."""

    result = {}
    for pair in pairs:
        name, grade = pair
        result[name] = result.get(name, 0) + grade

    return result

students_info = [('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)]
students_total_points = aggregate_points(students_info)
print(students_total_points)

# DRILL 11: Filter by Index and Square (enumerate & LC)

def square_at_even_indices(numbers: list) -> list:
    """Uses enumerate and LC to filter by index and transform value."""
    return [num**2 for idx, num in enumerate(numbers) if idx % 2 == 0]

input_list = [1, 2, 3, 4, 5, 6]
even_idx_list = square_at_even_indices(input_list)
print(even_idx_list)

# DRILL 12: Sort by Nested Tuple Value (Lambda)
def sort_by_nested_tuple(data: list) -> list:
    """Uses lambda to sort by multiple criteria (age: asc, height: desc)."""
    return sorted(data, key=lambda item: (item[1][0], -item[1][1]))

# DRILL 13: Filter

def filter_small_floats(floats: list) -> list:
    """Uses Ternary Operator to conditionally swap values, maintaining float type."""
    return [num if num > 10.0 else 0.0 for num in floats]

floats_list = [15.5, 9.2, 11.0, 5.0, 10.0]
filtered_list = filter_small_floats(floats_list)
print(filtered_list)