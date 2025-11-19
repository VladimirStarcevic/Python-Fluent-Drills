# Zadatak 11: Kvadriranje vrednosti na parnim indeksima
# Napiši funkciju square_at_even_indices koja prihvata listu brojeva. Koristeći enumerate i list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih brojeva koji se u originalnoj listi nalaze na parnim indeksima (0, 2, 4, itd.).
#
# Primer ulaza: [1, 2, 3, 4, 5, 6]
# Očekivani izlaz: [1, 9, 25]

def  square_at_even_indices(numbs: list[int]) -> list[int]:

    return [num**2 for idx, num in enumerate(numbs) if idx % 2 == 0]

even_idx_list = square_at_even_indices( [1, 2, 3, 4, 5, 6])
print(even_idx_list)

# Zadatak 12: Sortiranje po ugnežđenim vrednostima
# Napiši funkciju sort_by_nested_tuple koja prima listu torki.
# Svaka torka sadrži ime osobe i drugu (ugnežđenu) torku sa godinama i visinom te osobe ('Ime', (godine, visina)). Sortiraj listu po sledećim kriterijumima:
#
# Primarno po godinama, rastuće.
# Sekundarno po visini, opadajuće (ako su godine iste).
# Primer ulaza: [('Ana', (25, 170)), ('Pera', (30, 180)), ('Mika', (25, 175))]
# Očekivani izlaz: [('Mika', (25, 175)), ('Ana', (25, 170)), ('Pera', (30, 180))]

def sort_by_nested_tuple(data):

    return sorted(data, key=lambda item: (item[1][0], -item[1][1]))


sorted_data = sort_by_nested_tuple([('Ana', (25, 170)), ('Pera', (30, 180)), ('Mika', (25, 175))])
print(sorted_data)

# Zadatak 13: Zamena malih decimalnih brojeva
# Napiši funkciju filter_small_floats koja prihvata listu decimalnih brojeva. Koristeći list comprehension i ternarni operator, vrati novu listu gde je svaki broj veći od 10.0 zadržan, dok je svaki broj manji ili jednak 10.0 zamenjen sa 0.0.
#
# Primer ulaza: [15.5, 9.2, 11.0, 5.0, 10.0]
# Očekivani izlaz: [15.5, 0.0, 11.0, 0.0, 0.0]

def filter_small_floats(numerics: list[float]) -> list[float]:

    return [0.0 if num < 10 else num for num in numerics]

numerics_filtered = filter_small_floats([15.5, 9.2, 11.0, 5.0, 10.0])
print(numerics_filtered)

# Zadatak 14: Filtriranje reči po dužini i početnom slovu
# Napiši funkciju filter_by_length_and_start koja prima listu reči. Koristeći list comprehension, vrati novu listu koja sadrži samo one reči koje istovremeno ispunjavaju oba uslova: duže su od 5 slova I počinju velikim slovom 'C'.
#
# Primer ulaza: ['apple', 'Cucumber', 'cat', 'Computer', 'caravan']
# Očekivani izlaz: ['Cucumber', 'Computer', 'caravan']

def filter_by_length_and_start(words: list[str]) -> list[str]:

    return [word for word in words if len(word) > 5 and word.startswith('C')]


c_upper_words = filter_by_length_and_start(['apple', 'Cucumber', 'cat', 'Computer', 'caravan'])
print(c_upper_words)

# Zadatak 15: Inverzija vrednosti u rečniku
# Napiši funkciju invert_dictionary_values koja prihvata rečnik sa numeričkim vrednostima. Koristeći dictionary comprehension, kreiraj i vrati novi rečnik gde su ključevi isti kao u ulaznom rečniku, ali su sve vrednosti pomnožene sa -1.
#
# Primer ulaza: {'prihod': 1000, 'trosak': 500, 'dobit': 500}
# Očekivani izlaz: {'prihod': -1000, 'trosak': -500, 'dobit': -500}

def invert_dictionary_values(sales_info: dict[str, int]) -> dict[str, int]:

    return {
        key: -value for key, value in sales_info.items()
    }

inverted_sales_info = invert_dictionary_values({'prihod': 1000, 'trosak': 500, 'dobit': 500})
print(inverted_sales_info)

# Zadatak 16: Kreiranje rečnika sa cenom kao ključem
# Napiši funkciju price_as_key_if_high koja prima dve liste: listu imena i listu cena.
# Koristeći zip i dictionary comprehension, kreiraj rečnik gde je cena ključ, a ime vrednost, ali samo za one parove gde je cena veća od 100.
#
# Ulaz (Imena): ['A', 'B', 'C', 'D']
# Ulaz (Cene): [50, 120, 80, 250]
# Očekivani izlaz: {120: 'B', 250: 'D'}

def price_as_key_if_high(products: list[str], prices: list[int]) -> dict[int, str]:

    return {price: product for product, price in zip(products, prices) if price > 100}

ot = price_as_key_if_high(['A', 'B', 'C', 'D'], [50, 120, 80, 250])
print(ot)
# Zadatak 17: Sortiranje proizvoda po zalihama i ceni
# Napiši funkciju sort_by_stock_and_price koja prihvata listu torki. Svaka torka predstavlja proizvod sa formatom (ime, cena, zaliha). Sortiraj listu po sledećim kriterijumima:
#
# Primarno po broju zaliha, opadajuće.
# Sekundarno po ceni, rastuće (ako su zalihe iste).
# Primer ulaza: [('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]
# Očekivani izlaz: [('Monitor', 300, 10), ('Miš', 15, 5), ('Laptop', 1200, 5)]

def sort_by_stock_and_price(products):

    return sorted(products, key=lambda item: (-item[2],item[1]))

out_lst = sort_by_stock_and_price([('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)])
print(out_lst)

# Zadatak 18: Filtriranje ocena po indeksu i vrednosti
# Napiši funkciju filter_by_index_and_value koja prihvata listu ocena. Koristeći enumerate i list comprehension, vrati novu listu koja sadrži samo one ocene koje zadovoljavaju oba uslova: nalaze se na indeksu deljivom sa 3 I njihova vrednost je veća od 70.
#
# Primer ulaza: [80, 50, 60, 90, 70, 40, 85]
# Očekivani izlaz: [80, 90]

def filter_by_index_and_value(grades: list[int]) -> list[int]:

    return [grade for idx, grade in enumerate(grades) if grade > 70 and idx % 3 == 0]

filtered_grade = filter_by_index_and_value([80, 50, 60, 90, 70, 40, 85])
print(filtered_grade)

# Zadatak 19: Kvadriranje samo celih brojeva iz mešovite liste
# Napiši funkciju square_only_integers koja prihvata listu sa mešovitim tipovima podataka (brojevi, stringovi...). Koristeći list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih elemenata koji su celi brojevi (tip int).
#
# Primer ulaza: [1, 5.5, 'a', 4, 9, 'b']
# Očekivani izlaz: [1, 16, 81]

def square_only_integers(mixed_list):

    return [item**2 for item in mixed_list if isinstance(item, int)]


integers = square_only_integers([1, 5.5, 'a', 4, 9, 'b'])
print(integers)

# Zadatak 20: Kreiranje rečnika iz torki pod uslovom
# Napiši funkciju dict_from_tuple_if_high koja prima listu torki u formatu (ime, bodovi).
# Koristeći dictionary comprehension, kreiraj i vrati rečnik, ali uključi samo one parove iz liste čija je vrednost bodova veća od 10.
#
# Primer ulaza: [('A', 15), ('B', 5), ('C', 20), ('D', 8)]
# Očekivani izlaz: {'A': 15, 'C': 20}

def dict_from_tuple_if_high(data: list[tuple[str, int]]) -> dict[str, int]:

    return {
        item[0]: item[1] for item in data if item[1] > 10
    }

info_data = dict_from_tuple_if_high([('A', 15), ('B', 5), ('C', 20), ('D', 8)])
print(info_data)