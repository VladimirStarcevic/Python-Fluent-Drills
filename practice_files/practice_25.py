# Napiši funkciju square_even_numbers koja prihvata listu brojeva. Koristeći list comprehension, funkcija treba da isfiltrira samo parne brojeve iz ulazne liste i vrati novu listu koja sadrži njihove kvadrate.
# Primer ulaza: [1, 2, 3, 4, 5, 6, 7]
# Očekivani izlaz: [4, 16, 36]
from typing import List, Dict, Any

def square_even_numbers(numbs: List[int]) -> List[int]:
    return [num**2 for num in numbs if num % 2 == 0]

ls_in = [1, 2, 3, 4, 5, 6, 7]
ls_out = square_even_numbers(ls_in)
print(ls_out)

# Zadatak 2: Sortiranje jedinstvenih reči po dužini
# Napiši funkciju sort_unique_by_length koja prihvata listu reči. Funkcija treba prvo da ukloni sve duplikate, a zatim da sortira jedinstvene reči po njihovoj dužini, od najkraće do najduže.
# Primer ulaza: ['apple', 'banana', 'cucumber', 'apple', 'pear']
# Očekivani izlaz: ['pear', 'apple', 'banana', 'cucumber']


def sort_unique_by_length(words: List[str]) -> List[str]:
    filter_duplicate = set(words)
    return sorted(filter_duplicate, key=lambda word: len(word))

words_in = ['apple', 'banana', 'cucumber', 'apple', 'pear']
words_out = sort_unique_by_length(words_in)
print(words_out)

# Zadatak 3: Inverzija brojeva u stringu
# Napiši funkciju invert_and_keep_string koja prihvata listu stringova, gde svaki string predstavlja ceo broj.
# Koristeći list comprehension,
# funkcija treba da promeni znak svakom broju (pozitivan postaje negativan i obrnuto) i vrati novu listu sa promenjenim vrednostima, koje takođe moraju biti tipa string.
# Primer ulaza: ["10", "-5", "2", "-1"]
# Očekivani izlaz: ['-10', '5', '-2', '1']

def invert_and_keep_string(input_list: List[str]) -> List[str]:

    return [str(int(item) * (-1)) for item in input_list]

string_numbers = ["10", "-5", "2", "-1"]
inverted_numbs = invert_and_keep_string(string_numbers)
print(inverted_numbs)

# Napiši funkciju find_cheapest_product koja prihvata listu torki (tuples).
# Svaka torka se sastoji od naziva proizvoda (string) i njegove cene (broj).
# Koristeći min() funkciju i lambda izraz, pronađi i vrati kompletnu torku koja predstavlja najjeftiniji proizvod.
# Primer ulaza: [('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)]
# Očekivani izlaz: ('Mouse', 15)

def find_cheapest_product(products: List[tuple[str, int]]) -> tuple[str, int]:

    return min(products, key=lambda item: item[1])

products_ls = [('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)]
cheapest_product = find_cheapest_product(products_ls)
print(cheapest_product)

# Zadatak 5: Mapiranje liste u rečnik sa indeksima
# Napiši funkciju index_to_dictionary koja prihvata listu stavki.
# Koristeći petlju i enumerate, kreiraj i vrati rečnik (dictionary) gde su ključevi indeksi elemenata iz ulazne liste, a vrednosti su sami elementi.
# Primer ulaza: ['milk', 'bread', 'eggs']
# Očekivani izlaz: {0: 'milk', 1: 'bread', 2: 'eggs'}

def index_to_dictionary(item_list: List[str]) -> Dict[int, str]:
    dict_items = {}
    for idx, item in enumerate(item_list):
        dict_items[idx + 1] = item
    return dict_items

items = ['milk', 'bread', 'eggs']
items_list = index_to_dictionary(items)
print(items_list)

# Napiši funkciju filter_high_grades koja prihvata dve liste iste dužine: listu sa imenima učenika i listu sa njihovim ocenama.
# Koristeći zip funkciju i list comprehension, spoji svakog učenika sa njegovom ocenom i vrati novu listu formatiranih stringova,
# ali samo za one učenike čija je ocena veća od 80.
# Primer ulaza: names=['Pera', 'Mika', 'Laza', 'Ana'], grades=[95, 78, 88, 65]
# Očekivani izlaz: ['Pera has 95', 'Laza has 88']

def filter_high_grades(names_ls: List[str], grade_list: List[int]) -> List[str]:

    return [f"{name} has {grade}" for name, grade in zip(names_ls, grade_list) if grade > 80]

names=['Pera', 'Mika', 'Laza', 'Ana']
grades=[95, 78, 88, 65]

ls_out = filter_high_grades(names, grades)
print(ls_out)

# Napiši funkciju fizz_swap koja prihvata listu brojeva. Koristeći list comprehension i ternarni operator,
# funkcija treba da vrati novu listu u kojoj je svaki broj deljiv sa 3 zamenjen stringom "Fizz". Ostali brojevi treba da ostanu nepromenjeni.
# Primer ulaza: [1, 3, 5, 6, 8, 9, 10]
# Očekivani izlaz: [1, 'Fizz', 5, 'Fizz', 8, 'Fizz', 10]

def fizz_swap(nums: List[int]) -> List[Any]:
    return ["Fizz" if num % 3 == 0 else num for num in nums]

num_in = [1, 3, 5, 6, 8, 9, 10]
fizz_num_out = fizz_swap(num_in)
print(fizz_num_out)

# Napiši funkciju price_markup koja prihvata listu cena. Koristeći list comprehension,
# funkcija treba da filtrira samo one cene koje su veće od 100 i da na njih primeni povećanje od 10%.
# Funkcija treba da vrati novu listu koja sadrži samo preračunate, uvećane cene.
# Primer ulaza: [50, 120, 99, 200, 10]
# Očekivani izlaz: [132.0, 220.0]

def price_markup(prices: List[int]) -> List[float]:
    return [round(float(price + price * 0.1), 2) for price in prices if price > 100]

prices_in = [50, 120, 99, 200, 10]
prices_out = price_markup(prices_in)
print(prices_out)