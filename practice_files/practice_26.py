from typing import Dict, List, Any
# Zadatak 9: Uslovno spajanje rečnika
# Napiši funkciju conditional_merge koja prihvata dva rečnika, d1 i d2.
# Funkcija treba da kreira novi rečnik na sledeći način:
#
# Prvo, iz rečnika d1 filtriraj i zadrži samo one parove ključ-vrednost gde je vrednost veća od 50.
# Zatim, spoji taj filtrirani rečnik sa celokupnim rečnikom d2.
# Ako neki ključ postoji u oba rečnika (u filtriranom d1 i u d2), vrednost iz d2 ima prednost.
#
# Ulaz 1: d1 = {'A': 90, 'B': 40, 'C': 70}
# Ulaz 2: d2 = {'B': 5, 'D': 100, 'A': 10}
# Očekivani izlaz: {'C': 70, 'B': 5, 'D': 100, 'A': 10}

def conditional_merge(d1: Dict[str, int], d2: Dict[str, int]) -> Dict[str, int]:

    filtered_d1 = {k: v for k, v in d1.items() if v > 50}
    return {**filtered_d1,**d2}


d1 = {'A': 90, 'B': 40, 'C': 70}
d2 = {'B': 5, 'D': 100, 'A': 10}
d_out = conditional_merge(d1, d2)
print(d_out)

# Zadatak 10: Agregacija (sabiranje) poena
# Napiši funkciju aggregate_points koja prihvata listu torki. Svaka torka sadrži ime studenta i broj poena koje je osvojio.
# Funkcija treba da prođe kroz listu i sabere sve poene za svakog studenta, vraćajući rečnik gde su ključevi imena studenata, a vrednosti ukupan zbir njihovih poena.
#
# Primer ulaza: [('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)]
# Očekivani izlaz: {'Pera': 30, 'Mika': 5, 'Laza': 15}

def aggregate_points(data: List[tuple[str, int]]) -> Dict[str, int]:

    dict_out = {}
    for item in data:
        name = item[0]
        grade = item[1]
        dict_out[name] = dict_out.get(name, 0) + grade
    return dict_out

ls_in = [('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)]
dc_out = aggregate_points(ls_in)
print(dc_out)

# Zadatak 11: Kvadriranje vrednosti na parnim indeksima
# Napiši funkciju square_at_even_indices koja prihvata listu brojeva.
# Koristeći enumerate i list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih brojeva koji se u originalnoj listi nalaze na parnim indeksima (0, 2, 4, itd.).
#
# Primer ulaza: [1, 2, 3, 4, 5, 6]
# Očekivani izlaz: [1, 9, 25]

def square_at_even_indices(numbs: List[int]) -> List[int]:

    return [num**2 for idx, num in enumerate(numbs) if idx % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
ls_out = square_at_even_indices(numbers)
print(ls_out)

# Zadatak 12: Sortiranje po ugnežđenim vrednostima
# Napiši funkciju sort_by_nested_tuple koja prima listu torki.
# Svaka torka sadrži ime osobe i drugu (ugnežđenu) torku sa godinama i visinom te osobe ('Ime', (godine, visina)). Sortiraj listu po sledećim kriterijumima:
#
# Primarno po godinama, rastuće.
# Sekundarno po visini, opadajuće (ako su godine iste).
# Primer ulaza: [('Ana', (25, 170)), ('Pera', (30, 180)), ('Mika', (25, 175))]
# Očekivani izlaz: [('Mika', (25, 175)), ('Ana', (25, 170)), ('Pera', (30, 180))]

def sort_by_nested_tuple(ls_tpl: list) -> list:

    return sorted(ls_tpl, key=lambda item: (item[1][0], -item[1][1]))

data_ls = [('Ana', (25, 170)), ('Pera', (30, 180)), ('Mika', (25, 175))]
sorted_data_ls = sort_by_nested_tuple(data_ls)
print(sorted_data_ls)

# Zadatak 13: Zamena malih decimalnih brojeva
# Napiši funkciju filter_small_floats koja prihvata listu decimalnih brojeva.
# Koristeći list comprehension i ternarni operator, vrati novu listu gde je svaki broj veći od 10.0 zadržan, dok je svaki broj manji ili jednak 10.0 zamenjen sa 0.0.
#
# Primer ulaza: [15.5, 9.2, 11.0, 5.0, 10.0]
# Očekivani izlaz: [15.5, 0.0, 11.0, 0.0, 0.0]

def filter_small_floats(float_ls: List[float]) -> List[float]:

    return [0.0 if num <= 10.0 else num for num in float_ls]

fl_ls = [15.5, 9.2, 11.0, 5.0, 10.0]
filtered_floats = filter_small_floats(fl_ls)
print(filtered_floats)

# Zadatak 14: Filtriranje reči po dužini i početnom slovu
# Napiši funkciju filter_by_length_and_start koja prima listu reči.
# Koristeći list comprehension, vrati novu listu koja sadrži samo one reči koje istovremeno ispunjavaju oba uslova: duže su od 5 slova I počinju velikim slovom 'C'.
#
# Primer ulaza: ['apple', 'Cucumber', 'cat', 'Computer', 'caravan']
# Očekivani izlaz: ['Cucumber', 'Computer']

def filter_by_length_and_start(words: List[str]) -> List[str]:

    return [word for word in words if len(word) > 5 and word.startswith('C')]

word_list = ['apple', 'Cucumber', 'cat', 'Computer', 'caravan']
filter_ls = filter_by_length_and_start(word_list)
print(filter_ls)

# Zadatak 15: Inverzija vrednosti u rečniku
# Napiši funkciju invert_dictionary_values koja prihvata rečnik sa numeričkim vrednostima.
# Koristeći dictionary comprehension, kreiraj i vrati novi rečnik gde su ključevi isti kao u ulaznom rečniku, ali su sve vrednosti pomnožene sa -1.
#
# Primer ulaza: {'prihod': 1000, 'trosak': 500, 'dobit': 500}
# Očekivani izlaz: {'prihod': -1000, 'trosak': -500, 'dobit': -500}

def invert_dictionary_values(dc_in: Dict[str, int]) -> Dict[str, int]:

    return {
        k: -1*v for k, v in dc_in.items()
    }

dc = {'prihod': 1000, 'trosak': 500, 'dobit': 500}
inverted_dc = invert_dictionary_values(dc)
print(inverted_dc)

# Zadatak 16: Kreiranje rečnika sa cenom kao ključem
# Napiši funkciju price_as_key_if_high koja prima dve liste: listu imena i listu cena.
# Koristeći zip i dictionary comprehension, kreiraj rečnik gde je cena ključ, a ime vrednost, ali samo za one parove gde je cena veća od 100.
#
# Ulaz (Imena): ['A', 'B', 'C', 'D']
# Ulaz (Cene): [50, 120, 80, 250]
# Očekivani izlaz: {120: 'B', 250: 'D'}

def price_as_key_if_high(names: List[str], prices: List[int]) -> Dict[int, str]:

    return {
        k: v for k, v in zip(prices, names) if k > 100
    }

name_ls = ['A', 'B', 'C', 'D']
price_ls = [50, 120, 80, 250]
out = price_as_key_if_high(name_ls, price_ls)
print(out)