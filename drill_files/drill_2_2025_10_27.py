# DRILL 19: Nested Filter/Map (LC - Provera Tipa)
# Zahtev: Primiti listu koja sadrži brojeve i stringove. Vratiti novu listu koja sadrži samo kvadrate celih brojeva. Svi stringovi i floatovi se ignorišu.
# Input: [1, 5.5, 'a', 4, 9, 'b']
# Output: [1, 16, 81]
from typing import Any


def square_only_integers(data: list) -> list:
    """Uses LC and isinstance() to filter by data type and transform."""
    return [num**2 for num in data if isinstance(num, int)]

data_in = [1, 5.5, 'a', 4, 9, 'b']
ls_out = square_only_integers(data_in)
print(ls_out)

# DRILL 20: DC - Rečnik sa Uslovnim Ključem (Hashable)
# Zahtev: Primiti listu toraka u formatu (ime, bodovi). Kreirati rečnik, ali samo za parove gde je bodovi veći od 10.
# Input: [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
# Output: {'A': 15, 'C': 20}

def dict_from_tuple_if_high(pairs: list) -> dict:
    """Uses DC to filter list of tuples based on the value."""
    return {
        letter: score for letter, score in pairs if score > 10
    }

in_list = [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
out_dict = dict_from_tuple_if_high(in_list)
print(out_dict)

# DRILL 21: Setovi - Presek Tri Liste
# Zahtev: Primiti tri liste (A, B, C). Vratiti listu jedinstvenih stavki koje se nalaze u sve tri liste (trostruki presek).
# Input A: [1, 2, 3, 4]
# Input B: [3, 4, 5, 6]
# Input C: [4, 6, 7, 3]
# Output: [3, 4] (Redosled nije važan)

def intersection_of_three(l1: list, l2: list, l3: list) -> set[Any]:
    """Converts to sets and uses the intersection() method."""
    # Hint: set1.intersection(set2, set3)
    s1 = set(l1)
    s2 = set(l2)
    s3 = set(l3)
    return s1.intersection(s2, s3)

in_a = [1, 2, 3, 4]
in_b = [3, 4, 5, 6]
in_c = [4, 6, 7, 3]


result = intersection_of_three(in_a, in_b, in_c)
print(result)


# DRILL 22:
# Zahtev: Primiti rečnik (ime: poeni). Vratiti listu torki (ime, poeni) sortiranu opadajuće po poenima.
# Input: {'Pera': 30, 'Mika': 5, 'Laza': 15}
# Output: [('Pera', 30), ('Laza', 15), ('Mika', 5)]

def sort_dict_by_value_desc(data: dict) -> list:
    """Uses sorted() on dict.items() with lambda and reverse=True."""
    return sorted(data.items(), key=lambda item: item[1], reverse=True)

# DRILL 23: LC - Fibonacci
# Zahtev: Koristeći samo List Comprehension (za vežbu sintakse), kreirati listu sa brojevima od 1 do 10, ali samo ako su neparni.
# Input: Implicitno range(1, 11)
# Output: [1, 3, 5, 7, 9]

def odd_numbers_up_to_ten() -> list:
    """Uses LC and range() to filter odd numbers."""
    return [num for num in range(1, 11) if num % 2!= 0]

ls_out = odd_numbers_up_to_ten()
print(ls_out)

