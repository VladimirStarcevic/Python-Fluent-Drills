from typing import Dict, List, Tuple, Any
# Zadatak 17: Sortiranje proizvoda po zalihama i ceni
# Napiši funkciju sort_by_stock_and_price koja prihvata listu torki. Svaka torka predstavlja proizvod sa formatom (ime, cena, zaliha).
# Sortiraj listu po sledećim kriterijumima:
#
# Primarno po broju zaliha, opadajuće.
# Sekundarno po ceni, rastuće (ako su zalihe iste).
# Primer ulaza: [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
# Očekivani izlaz: [('Monitor', 300, 10), ('Miš', 15, 5), ('Laptop', 1200, 5)]

def sort_by_stock_and_price(list_in) -> list:

    return sorted(list_in, key=lambda item: (-item[2], item[1]))

product_list = [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
sorted_product_ls = sort_by_stock_and_price(product_list)
print(sorted_product_ls)

# Zadatak 18: Filtriranje ocena po indeksu i vrednosti
# Napiši funkciju filter_by_index_and_value koja prihvata listu ocena.
# Koristeći enumerate i list comprehension,
# vrati novu listu koja sadrži samo one ocene koje zadovoljavaju oba uslova: nalaze se na indeksu deljivom sa 3 I njihova vrednost je veća od 70.
#
# Primer ulaza: [80, 50, 60, 90, 70, 40, 85]
# Očekivani izlaz: [80, 90, 85]

def filter_by_index_and_value(ls_in: List[int]) -> List[int]:

    return [grade for idx, grade in enumerate(ls_in) if idx % 3 == 0 and grade > 70]

grades = [80, 50, 60, 90, 70, 40, 85]
filtered_grades = filter_by_index_and_value(grades)
print(filtered_grades)

# Zadatak 19: Kvadriranje samo celih brojeva iz mešovite liste
# Napiši funkciju square_only_integers koja prihvata listu sa mešovitim tipovima podataka (brojevi, stringovi...). Koristeći list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih elemenata koji su celi brojevi (tip int).
#
# Primer ulaza: [1, 5.5, 'a', 4, 9, 'b']
# Očekivani izlaz: [1, 16, 81]

def square_only_integers(ls_in: List[Any]) -> List[int]:

    return [num**2 for num in ls_in if isinstance(num, int)]

mix_ls = [1, 5.5, 'a', 4, 9, 'b']
out = square_only_integers(mix_ls)
print(out)

# Zadatak 20: Kreiranje rečnika iz torki pod uslovom
# Napiši funkciju dict_from_tuple_if_high koja prima listu torki u formatu (ime, bodovi).
# Koristeći dictionary comprehension, kreiraj i vrati rečnik, ali uključi samo one parove iz liste čija je vrednost bodova veća od 10.
#
# Primer ulaza: [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
# Očekivani izlaz: {'A': 15, 'C': 20}

def dict_from_tuple_if_high(ls_tuple: List[tuple[str, int]]) -> Dict[str, int]:

    return {
        letter: score for letter, score in ls_tuple if score > 10
    }

in_ls = [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
filtered_score = dict_from_tuple_if_high(in_ls)
print(filtered_score)

# Zadatak 21: Presek tri liste
# Napiši funkciju intersection_of_three koja prihvata tri liste.
# Funkcija treba da pronađe i vrati skup (set) elemenata koji se nalaze u sve tri ulazne liste istovremeno.
#
# Ulaz A: [1, 2, 3, 4]
# Ulaz B: [3, 4, 5, 6]
# Ulaz C: [4, 6, 7, 3]
# Očekivani izlaz: {3, 4}

def intersection_of_three(ls1: List[int], ls2: List[int], ls3: List[int]) -> set[int]:
    return set(ls1) & set(ls2) & set(ls3)

l_a = [1, 2, 3, 4]
l_b = [3, 4, 5, 6]
l_c = [4, 6, 7, 3]

result = intersection_of_three(l_a, l_b, l_c)
print(result)