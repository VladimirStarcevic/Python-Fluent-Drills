# Zadatak 22: Sortiranje rečnika po vrednosti opadajuće
# Napiši funkciju sort_dict_by_value_desc koja prihvata rečnik (npr. ime: poeni).
# Funkcija treba da vrati listu torki (ključ, vrednost) sortiranu opadajuće prema vrednosti.
#
# Primer ulaza: {'Pera': 30, 'Mika': 5, 'Laza': 15}
# Očekivani izlaz: [('Pera', 30), ('Laza', 15), ('Mika', 5)]

def sort_dict_by_value_desc(dict_in) -> list:

    return sorted(dict_in.items(), key=lambda item: item[1], reverse=True)

score_results = {'Pera': 30, 'Mika': 5, 'Laza': 15}
out_list = sort_dict_by_value_desc(score_results)
print(out_list)

# Zadatak 23: Lista neparnih brojeva
# Napiši funkciju odd_numbers_up_to_ten koja ne prima argumente.
# Koristeći list comprehension i range, funkcija treba da kreira i vrati listu koja sadrži sve neparne brojeve od 1 do 10.
#
# Očekivani izlaz: [1, 3, 5, 7, 9]

def odd_numbers_up_to_ten(ls_in) -> list:

    return [num for num in range(1, 10) if num % 2 != 0]

# Zadatak 24: Formatiranje numeričkih podataka iz liste stringova
# Napiši funkciju format_numeric_data koja prihvata listu stringova.
# Funkcija treba da vrati novu listu koja sadrži samo one elemente koji se mogu pretvoriti u broj.
# Ti elementi treba da budu pretvoreni u decimalni broj (float) i zaokruženi na dve decimale.
#
# Primer ulaza: ['10.5', 'error', '20.334', '15', 'fail']
# Očekivani izlaz: [10.5, 20.33, 15.0]

def is_float(item):
    try:
        float(item)
        return True
    except ValueError:
        return False

def format_numeric_data(data_mix_ls) -> list[float]:

    return [round(float(item), 2) for item in data_mix_ls if is_float(item)]

mix_ls = ['10.5', 'error', '20.334', '15', 'fail']
result = format_numeric_data(mix_ls)
print(result)

# Zadatak 25: Zbir kvadrata parova elemenata
# Napiši funkciju sum_of_squares_pairs koja prihvata dve liste brojeva jednakih dužina.
# Koristeći zip i list comprehension, funkcija treba da vrati novu listu gde je svaki element zbir kvadrata odgovarajućih elemenata iz ulaznih listi.
#
# Ulaz A: [1, 2, 3]
# Ulaz B: [4, 5, 6]
# Očekivani izlaz: [17, 29, 45] (Jer je 1²+4²=17, 2²+5²=29, 3²+6²=45)

def sum_of_squares_pairs(ls_a, ls_b) -> list[int]:
    return [item_a**2 + item_b**2 for item_a, item_b in zip(ls_a, ls_b)]

numbs_a = [1, 2, 3]
numbs_b = [4, 5, 6]
numbers = sum_of_squares_pairs(numbs_a, numbs_b)
print(numbers)

# Zadatak 26: Uslovno preimenovanje ključeva u rečniku
# Napiši funkciju conditional_key_rename koja prihvata rečnik (proizvod: cena).
# Kreiraj novi rečnik gde, ako je cena proizvoda veća od 100, ključu se dodaje prefiks "SKU_". U suprotnom, ključ ostaje isti.
#
# Primer ulaza: {'milk': 50, 'bread': 120, 'cheese': 80}
# Očekivani izlaz: {'milk': 50, 'SKU_bread': 120, 'cheese': 80}

def conditional_key_rename(products) -> dict[str, int]:

    return {
        ("SKU_" + k) if v > 100 else k: v for k,v in products.items()
    }

dict_in = {'milk': 50, 'bread': 120, 'cheese': 80}
sku_products = conditional_key_rename(dict_in)
print(sku_products)

# Zadatak 27: Sortiranje reči po dužini i abecedi
# Napiši funkciju sort_by_length_then_alphabet_desc koja prima listu stringova.
# Sortiraj listu po dva kriterijuma:
#
# Primarno po dužini reči, opadajuće (od najduže ka najkraćoj).
# Sekundarno po abecednom redu, takođe opadajuće (od Z ka A).
# Primer ulaza: ['apple', 'pie', 'banana', 'cat']
# Očekivani izlaz: ['banana', 'apple', 'pie', 'cat']

def sort_by_length_then_alphabet_desc(words) -> list[str]:

    #first_sort = sorted(words, key= lambda word: len(word), reverse=True)
    #return sorted(first_sort, key=lambda word: word, reverse=True)
    return sorted(words, key=lambda word: (len(word), word), reverse=True)

words_ls = ['apple', 'pie', 'banana', 'cat']
sorted_words_list = sort_by_length_then_alphabet_desc(words_ls)
print(sorted_words_list)