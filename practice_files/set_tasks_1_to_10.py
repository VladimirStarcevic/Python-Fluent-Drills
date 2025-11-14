# Zadatak 1: Kvadriranje parnih brojeva
# Napiši funkciju square_even_numbers koja prihvata listu brojeva. Koristeći list comprehension, funkcija treba da isfiltrira samo parne brojeve iz ulazne liste i vrati novu listu koja sadrži njihove kvadrate.
#
# Primer ulaza: [1, 2, 3, 4, 5, 6, 7]
# Očekivani izlaz: [4, 16, 36]
from fontTools.misc.cython import returns


def square_even_numbers(nums: list[int]) -> list[int]:

    return [num**2 for num in nums if num % 2 == 0]

even_list = square_even_numbers([1, 2, 3, 4, 5, 6, 7])
print(even_list)

# Zadatak 2: Sortiranje jedinstvenih reči po dužini
# Napiši funkciju sort_unique_by_length koja prihvata listu reči. Funkcija treba prvo da ukloni sve duplikate, a zatim da sortira jedinstvene reči po njihovoj dužini, od najkraće do najduže.
#
# Primer ulaza: ['apple', 'banana', 'cucumber', 'apple', 'pear']
# Očekivani izlaz: ['pear', 'apple', 'banana', 'cucumber']

def sort_unique_by_length(words: list[str]) -> list[str]:

    unique = set(words)
    return sorted(unique, key=lambda word: len(word))

sorted_words = sort_unique_by_length( ['apple', 'banana', 'cucumber', 'apple', 'pear'])
print(sorted_words)

# Zadatak 3: Inverzija brojeva u stringu
# Napiši funkciju invert_and_keep_string koja prihvata listu stringova, gde svaki string predstavlja ceo broj. Koristeći list comprehension, funkcija treba da promeni znak svakom broju (pozitivan postaje negativan i obrnuto) i vrati novu listu sa promenjenim vrednostima, koje takođe moraju biti tipa string.
#
# Primer ulaza: ["10", "-5", "2", "-1"]
# Očekivani izlaz: ['-10', '5', '-2', '1']

def invert_and_keep_string(ls_in: list[str]) -> list[str]:

    return [str(-int(item)) for item in ls_in]

inverted_items = invert_and_keep_string(["10", "-5", "2", "-1"])
print(inverted_items)

# Zadatak 4: Pronalaženje najjeftinijeg proizvoda
# Napiši funkciju find_cheapest_product koja prihvata listu torki (tuples). Svaka torka se sastoji od naziva proizvoda (string) i njegove cene (broj). Koristeći min() funkciju i lambda izraz, pronađi i vrati kompletnu torku koja predstavlja najjeftiniji proizvod.
#
# Primer ulaza: [('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)]
# Očekivani izlaz: ('Mouse', 15)

def find_cheapest_product(product_list: list[tuple[str, int]]) -> tuple[str, int]:

    return min(product_list,key=lambda product_price: product_price[1])

cheapest_product = find_cheapest_product([('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)])
print(cheapest_product)

# Zadatak 5: Mapiranje liste u rečnik sa indeksima
# Napiši funkciju index_to_dictionary koja prihvata listu stavki. Koristeći petlju i enumerate, kreiraj i vrati rečnik (dictionary) gde su ključevi indeksi elemenata iz ulazne liste, a vrednosti su sami elementi.
#
# Primer ulaza: ['milk', 'bread', 'eggs']
# Očekivani izlaz: {0: 'milk', 1: 'bread', 2: 'eggs'}

def index_to_dictionary(product_list: list[str]) -> dict[int, str]:

    return {
        idx: name for idx, name in enumerate(product_list)
    }

idx_keys_map_of_products = index_to_dictionary(['milk', 'bread', 'eggs'])
print(idx_keys_map_of_products)

# Zadatak 6: Filtriranje ocena
# Napiši funkciju filter_high_grades koja prihvata dve liste iste dužine: listu sa imenima učenika i listu sa njihovim ocenama.
# Koristeći zip funkciju i list comprehension, spoji svakog učenika sa njegovom ocenom i vrati novu listu formatiranih stringova,
# ali samo za one učenike čija je ocena veća od 80.
#
# Primer ulaza: names=['Pera', 'Mika', 'Laza', 'Ana'], grades=[95, 78, 88, 65]
# Očekivani izlaz: ['Pera has 95', 'Laza has 88']

def filter_high_grades(names_list: list[str], grades: list[int]) -> list[str]:

    return [f"{name} has {grade}" for name, grade in zip(names_list, grades) if grade > 80]


info_student_list = filter_high_grades(['Pera', 'Mika', 'Laza', 'Ana'], [95, 78, 88, 65])
print(info_student_list)

# Zadatak 7: Uslovna zamena vrednosti ("Fizz" zadatak)
# Napiši funkciju fizz_swap koja prihvata listu brojeva. Koristeći list comprehension i ternarni operator,
# funkcija treba da vrati novu listu u kojoj je svaki broj deljiv sa 3 zamenjen stringom "Fizz". Ostali brojevi treba da ostanu nepromenjeni.
#
# Primer ulaza: [1, 3, 5, 6, 8, 9, 10]
# Očekivani izlaz: [1, 'Fizz', 5, 'Fizz', 8, 'Fizz', 10]

def fizz_swap(numbers: list[int]):

    return ['Fizz' if num % 3 == 0 else num for num in numbers]

fizz_ls = fizz_swap([1, 3, 5, 6, 8, 9, 10])
print(fizz_ls)

# Zadatak 8: Povećanje cena za skuplje proizvode
# Napiši funkciju price_markup koja prihvata listu cena.
# Koristeći list comprehension, funkcija treba da filtrira samo one cene koje su veće od 100 i da na njih primeni povećanje od 10%.
# Funkcija treba da vrati novu listu koja sadrži samo preračunate, uvećane cene.
#
# Primer ulaza: [50, 120, 99, 200, 10]
# Očekivani izlaz: [132.0, 220.0]

def calculate_markup(product_price, percentage):
     return round(float(product_price + product_price*percentage), 2)


def price_markup(prices: list[int]) -> list[float]:
    return [calculate_markup(price, 0.1) for price in prices if price > 100]


markup_price = price_markup([50, 120, 99, 200, 10])
print(markup_price)

# Zadatak 9: Uslovno spajanje rečnika
# Napiši funkciju conditional_merge koja prihvata dva rečnika, d1 i d2. Funkcija treba da kreira novi rečnik na sledeći način:
#
# Prvo, iz rečnika d1 filtriraj i zadrži samo one parove ključ-vrednost gde je vrednost veća od 50.
# Zatim, spoji taj filtrirani rečnik sa celokupnim rečnikom d2.
# Ako neki ključ postoji u oba rečnika (u filtriranom d1 i u d2), vrednost iz d2 ima prednost.
#
# Ulaz 1: d1 = {'A': 90, 'B': 40, 'C': 70}
# Ulaz 2: d2 = {'B': 5, 'D': 100, 'A': 10}
# Očekivani izlaz: {'C': 70, 'B': 5, 'D': 100, 'A': 10}

def conditional_merge(d1, d2):

    filtered_d1 = {k: v for k, v in d1.items() if v > 50}
    return {**d2, **filtered_d1}

filtered_map = conditional_merge({'A': 90, 'B': 40, 'C': 70}, {'B': 5, 'D': 100, 'A': 10})
print(filtered_map)

# Zadatak 10: Agregacija (sabiranje) poena
# Napiši funkciju aggregate_points koja prihvata listu torki.
# Svaka torka sadrži ime studenta i broj poena koje je osvojio. Funkcija treba da prođe kroz listu i sabere sve poene za svakog studenta, vraćajući rečnik gde su ključevi imena studenata, a vrednosti ukupan zbir njihovih poena.
#
# Primer ulaza: [('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)]
# Očekivani izlaz: {'Pera': 30, 'Mika': 5, 'Laza': 15}


def aggregate_points(student_score: list[tuple[str, int]]) -> dict[str, int]:

    result = {}
    for item in student_score:
        name = item[0]
        grade = item[1]
        result[name] = result.get(name, 0) + grade
    return result

out = aggregate_points([('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)])
print(out)
