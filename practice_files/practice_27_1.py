# Zadatak 21: Presek tri liste
# Napiši funkciju intersection_of_three koja prihvata tri liste. Funkcija treba da pronađe i vrati skup (set) elemenata koji se nalaze u sve tri ulazne liste istovremeno.
#
# Ulaz A: [1, 2, 3, 4]
# Ulaz B: [3, 4, 5, 6]
# Ulaz C: [4, 6, 7, 3]
# Očekivani izlaz: {3, 4}

def intersection_of_three(l_a, l_b,l_c):

    return set(l_a) & set(l_b) & set(l_c)

# Zadatak 22: Sortiranje rečnika po vrednosti opadajuće
# Napiši funkciju sort_dict_by_value_desc koja prihvata rečnik (npr. ime: poeni). Funkcija treba da vrati listu torki (ključ, vrednost) sortiranu opadajuće prema vrednosti.
#
# Primer ulaza: {'Pera': 30, 'Mika': 5, 'Laza': 15}
# Očekivani izlaz: [('Pera', 30), ('Laza', 15), ('Mika', 5)]

def sort_dict_by_value_desc(dict_in: dict[str, int]) -> list[tuple[str, int]]:

    data_list = dict_in.items()
    return sorted(data_list, key=lambda item: -item[1])

out_list = sort_dict_by_value_desc({'Pera': 30, 'Mika': 5, 'Laza': 15})
print(out_list)

# Zadatak 23: Lista neparnih brojeva
# Napiši funkciju odd_numbers_up_to_ten koja ne prima argumente.
# Koristeći list comprehension i range, funkcija treba da kreira i vrati listu koja sadrži sve neparne brojeve od 1 do 10.
#
# Očekivani izlaz: [1, 3, 5, 7, 9]

def odd_numbers_up_to_ten() -> list[int]:

    odd_list = []
    for i in range(1, 10):
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list

odd_ls = odd_numbers_up_to_ten()
print(odd_ls)

# Zadatak 24: Formatiranje numeričkih podataka iz liste stringova
# Napiši funkciju format_numeric_data koja prihvata listu stringova.
# Funkcija treba da vrati novu listu koja sadrži samo one elemente koji se mogu pretvoriti u broj.
# Ti elementi treba da budu pretvoreni u decimalni broj (float) i zaokruženi na dve decimale.
#
# Primer ulaza: ['10.5', 'error', '20.334', '15', 'fail']
# Očekivani izlaz: [10.5, 20.33, 15.0]

def is_numeric(item: str) -> bool:
    try:
        float(item)
        return True
    except ValueError:
        return False

def format_numeric_data(mix_ls) -> list[float]:

    return [round(float(item), 2) for item in mix_ls if is_numeric(item)]

numerics = format_numeric_data(['10.5', 'error', '20.334', '15', 'fail'])
print(numerics)

# Zadatak 25: Zbir kvadrata parova elemenata
# Napiši funkciju sum_of_squares_pairs koja prihvata dve liste brojeva jednakih dužina.
# Koristeći zip i list comprehension, funkcija treba da vrati novu listu gde je svaki element zbir kvadrata odgovarajućih elemenata iz ulaznih listi.
#
# Ulaz A: [1, 2, 3]
# Ulaz B: [4, 5, 6]
# Očekivani izlaz: [17, 29, 45] (Jer je 1²+4²=17, 2²+5²=29, 3²+6²=45)

def sum_of_squares_pairs(ls_a, ls_b) -> list[int]:

    return [num_a**2 + num_b**2 for num_a, num_b in zip(ls_a, ls_b)]

squared_ls = sum_of_squares_pairs([1,2,3], [4,5,6])
print(squared_ls)

# Zadatak 26: Uslovno preimenovanje ključeva u rečniku
# Napiši funkciju conditional_key_rename koja prihvata rečnik (proizvod: cena). Kreiraj novi rečnik gde, ako je cena proizvoda veća od 100, ključu se dodaje prefiks "SKU_". U suprotnom, ključ ostaje isti.
#
# Primer ulaza: {'milk': 50, 'bread': 120, 'cheese': 80}
# Očekivani izlaz: {'milk': 50, 'SKU_bread': 120, 'cheese': 80}

def conditional_key_rename(dict_in) -> dict[str, int]:

    return {
        ("SKU_" + name) if price > 100 else name: price for name, price in dict_in.items()
    }

output_map = conditional_key_rename({'milk': 50, 'bread': 120, 'cheese': 80})
print(output_map)

# Zadatak 27: Sortiranje reči po dužini i abecedi
# Napiši funkciju sort_by_length_then_alphabet_desc koja prima listu stringova. Sortiraj listu po dva kriterijuma:
#
# Primarno po dužini reči, opadajuće (od najduže ka najkraćoj).
# Sekundarno po abecednom redu, takođe opadajuće (od Z ka A).
# Primer ulaza: ['apple', 'pie', 'banana', 'cat']
# Očekivani izlaz: ['banana', 'apple', 'pie', 'cat']

def sort_by_length_then_alphabet_desc(words: list[str]) -> list[str]:

    return sorted(words, key=lambda word: (-len(word), word))

sorted_words = sort_by_length_then_alphabet_desc(['apple', 'pie', 'banana', 'cat'])
print(sorted_words)