# DRILL 14: LC
# Zahtev: Primiti listu reči. Vratiti novu listu koja sadrži reči duže od 5 slova I koje počinju sa slovom 'C'.
# Input: ['apple', 'Cucumber', 'cat', 'Computer', 'caravan']
# Output: ['Cucumber', 'Computer', 'caravan']

def filter_by_length_and_start(words: list) -> list:
    """Uses LC with AND condition and string methods (len, startswith)."""
    return [item for item in words if item[0].startswith('C') and len(item) > 5]

in_ls = ['apple', 'Cucumber', 'cat', 'Computer', 'caravan']
out_ls = filter_by_length_and_start(in_ls)
print(out_ls)

# DRILL 15: DC
# Zahtev: Primiti rečnik (ključ: vrednost). Kreirati novi rečnik gde su sve vrednosti pretvorene u negativne (pomnožene sa -1).
# Input: {'prihod': 1000, 'trosak': 500, 'dobit': 500}
# Output: {'prihod': -1000, 'trosak': -500, 'dobit': -500}

def invert_dictionary_values(data: dict) -> dict:
    """Uses DC to transform all values to negative."""
    return {
        key: value * (-1) for key, value in data.items()
    }

in_dict = {'prihod': 1000, 'trosak': 500, 'dobit': 500}
out_dict = invert_dictionary_values(in_dict)
print(out_dict)

# DRILL 16: Zip & DC
# Zahtev: Primiti listu cena i listu imena. Kreirati rečnik, ali ako je cena veća od 100, neka CENA BUDE KLJUČ, a IME VREDNOST. Ako nije, zanemari (filtriraj).
# Input (Names): ['A', 'B', 'C', 'D']
# Input (Prices): [50, 120, 80, 250]
# Output: {120: 'B', 250: 'D'}

def price_as_key_if_high(names: list, prices: list) -> dict:
    """Uses zip and DC to swap key/value pairs based on a condition."""
    return {
        price: name for name, price in zip(names, prices) if price > 100
    }

in_l1 = ['A', 'B', 'C', 'D']
in_l2 = [50, 120, 80, 250]
out_dict = price_as_key_if_high(in_l1, in_l2)
print(out_dict)

# DRILL 17: Lambda & Sort
# Zahtev: Primiti listu toraka (ime, cena, zaliha). Sortirati listu primarno po ZALIHI (opadajuće), a sekundarno po CENI (rastuće).
# Input: [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
# Output: [('Monitor', 300, 10), ('Laptop', 1200, 5), ('Miš', 15, 5)]

def sort_by_stock_and_price(data: list) -> list:
    """Uses lambda to sort by stock (desc) and price (asc)."""
    return sorted(data, key=lambda item: (-item[2], item[1]))

stork_list_in = [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
output = sort_by_stock_and_price(stork_list_in)
print(output)

# DRILL 18: Enumerate & LC
# Zahtev: Primiti listu ocena (int). Vratiti listu ocena, ali samo za one studente čiji je indeks deljiv sa 3 (0, 3, 6...) I čija je ocena veća od 70.
# Input: [80, 50, 60, 90, 70, 40, 85]
# Output: [80, 90] (Indeks 0 i 3)

def filter_by_index_and_value(grades: list) -> list:
    """Uses enumerate and LC with an AND condition on both index and value."""
    return [grade for idx, grade in enumerate(grades) if idx % 3 == 0 and grade > 70]

student_score = [80, 50, 60, 90, 70, 40, 85]
filtered_grades_list =filter_by_index_and_value(student_score)
print(filtered_grades_list)
