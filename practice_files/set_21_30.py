# Zadatak 21: Presek tri liste
# Napiši funkciju intersection_of_three koja prihvata tri liste.
# Funkcija treba da pronađe i vrati skup (set) elemenata koji se nalaze u sve tri ulazne liste istovremeno.
#
# Ulaz A: [1, 2, 3, 4]
# Ulaz B: [3, 4, 5, 6]
# Ulaz C: [4, 6, 7, 3]
# Očekivani izlaz: {3, 4}


def intersection_of_three(ls1, ls2, ls3):
    l1 = set(ls1)
    l2 = set(ls2)
    l3 = set(ls3)

    return l1.intersection(l2).intersection(l3)

out = intersection_of_three([1, 2, 3, 4], [3, 4, 5, 6], [4, 6, 7, 3])
print(out)

# Zadatak 22: Sortiranje rečnika po vrednosti opadajuće
# Napiši funkciju sort_dict_by_value_desc koja prihvata rečnik (npr. ime: poeni).
# Funkcija treba da vrati listu torki (ključ, vrednost) sortiranu opadajuće prema vrednosti.
#
# Primer ulaza: {'Pera': 30, 'Mika': 5, 'Laza': 15}
# Očekivani izlaz: [('Pera', 30), ('Laza', 15), ('Mika', 5)]


def sort_dict_by_value_desc(student_score_data: dict[str, int]) -> list[tuple[str, int]]:

    return sorted(student_score_data.items(), key=lambda item: item[1], reverse=True)