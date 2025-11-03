# Zadatak 16: Kreiranje rečnika sa cenom kao ključem
# Napiši funkciju price_as_key_if_high koja prima dve liste: listu imena i listu cena.
# Koristeći zip i dictionary comprehension, kreiraj rečnik gde je cena ključ, a ime vrednost, ali samo za one parove gde je cena veća od 100.
#
# Ulaz (Imena): ['A', 'B', 'C', 'D']
# Ulaz (Cene): [50, 120, 80, 250]
# Očekivani izlaz: {120: 'B', 250: 'D'}

def price_as_key_if_high(names: list[str], prices: list[int]) -> dict[int, str]:

    return {
        price: name for name, price in zip(names, prices) if price > 100
    }

filtered_map = price_as_key_if_high(['A', 'B', 'C', 'D'], [50, 120, 80, 250])
print(filtered_map)

# Zadatak 17: Sortiranje proizvoda po zalihama i ceni
# Napiši funkciju sort_by_stock_and_price koja prihvata listu torki.
# Svaka torka predstavlja proizvod sa formatom (ime, cena, zaliha).
# Sortiraj listu po sledećim kriterijumima:
#
# Primarno po broju zaliha, opadajuće.
# Sekundarno po ceni, rastuće (ako su zalihe iste).
# Primer ulaza: [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
# Očekivani izlaz: [('Monitor', 300, 10), ('Miš', 15, 5), ('Laptop', 1200, 5)]

def sort_by_stock_and_price(products: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:

    return sorted(products, key=lambda item: (-item[2],item[1]))

filtered_product_list = sort_by_stock_and_price([('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)])
print(filtered_product_list)

# Zadatak 18: Filtriranje ocena po indeksu i vrednosti
# Napiši funkciju filter_by_index_and_value koja prihvata listu ocena.
# Koristeći enumerate i list comprehension, vrati novu listu koja sadrži samo one ocene koje zadovoljavaju oba uslova: nalaze se na indeksu deljivom sa 3 I njihova vrednost je veća od 70.
#
# Primer ulaza: [80, 50, 60, 90, 70, 40, 85]
# Očekivani izlaz: [80, 90]

def filter_by_index_and_value(grades: list[int]) -> list[int]:

    return [grade for idx, grade in enumerate(grades) if idx % 3 == 0 and grade > 70]

high_grades_list = filter_by_index_and_value([80, 50, 60, 90, 70, 40, 85])
print(high_grades_list)

# Zadatak 19: Kvadriranje samo celih brojeva iz mešovite liste
# Napiši funkciju square_only_integers koja prihvata listu sa mešovitim tipovima podataka (brojevi, stringovi...).
# Koristeći list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih elemenata koji su celi brojevi (tip int).
#
# Primer ulaza: [1, 5.5, 'a', 4, 9, 'b']
# Očekivani izlaz: [1, 16, 81]

def square_only_integers(list_in):

    return [num**2 for num in list_in if isinstance(num, int)]

only_int_square = square_only_integers([1, 5.5, 'a', 4, 9, 'b'])
print(only_int_square)
# Zadatak 20: Kreiranje rečnika iz torki pod uslovom
# Napiši funkciju dict_from_tuple_if_high koja prima listu torki u formatu (ime, bodovi). Koristeći dictionary comprehension,
# kreiraj i vrati rečnik, ali uključi samo one parove iz liste čija je vrednost bodova veća od 10.
#
# Primer ulaza: [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
# Očekivani izlaz: {'A': 15, 'C': 20}

def dict_from_tuple_if_high(students_score: list[tuple[str, int]]) -> dict[str, int]:

    return {
        name: grade for name, grade in students_score if grade > 10
    }

out = dict_from_tuple_if_high([('A', 15), ('B', 5), ('C', 20), ('D', 8)])
print(out)