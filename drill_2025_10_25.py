# DRILL 1: Even Numbers Squared (LC)
def square_even_numbers(numbers: list) -> list:
    """Uses LC to filter even numbers and return their squares."""
    return [num**2 for num in numbers if num % 2 == 0]

numbs = [1, 2, 3, 4, 5, 6, 7]
square_even_list = square_even_numbers(numbs)
print(square_even_list)

# DRILL 2: Unique Sorted by Length (Setovi & Sorted)

def sort_unique_by_length(words: list) -> list:
    """Removes duplicates and sorts by length using set() and sorted(key=len)."""
    unique_words = set(words)
    return  sorted(unique_words, key=len)

words = ['apple', 'banana', 'cucumber', 'apple', 'pear']
sorted_by_length = sort_unique_by_length(words)
print(sorted_by_length)

# DRILL 3: Invert and Keep String Type (LC)

def invert_and_keep_string(number_strings: list) -> list:
    """Uses LC with nested type casting to invert sign and convert back to string."""
    return [str(int(num)* -1) for num in number_strings]


input_list =["10", "-5", "2", "-1"]
output_list = invert_and_keep_string(input_list)
print(output_list)

# DRILL 4: Find Cheapest Product (Lambda & Min)

def find_cheapest_product(products: list) -> tuple:
    """Uses min() with a lambda function to compare by price (index 1)."""
    return min(products,key=lambda product: product[1])

dict_in = [('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)]
product_out = find_cheapest_product(dict_in)
print(product_out)