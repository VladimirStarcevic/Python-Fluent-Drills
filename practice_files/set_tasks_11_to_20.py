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