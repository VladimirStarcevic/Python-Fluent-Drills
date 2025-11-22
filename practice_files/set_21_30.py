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

# Zadatak 23: Lista neparnih brojeva
# Napiši funkciju odd_numbers_up_to_ten koja ne prima argumente.
# Koristeći list comprehension i range, funkcija treba da kreira i vrati listu koja sadrži sve neparne brojeve od 1 do 10.
#
# Očekivani izlaz: [1, 3, 5, 7, 9]

def odd_numbers_up_to_ten():
    return [i for i in range(1, 11) if i % 2 != 0]

odd_numbs = odd_numbers_up_to_ten()
print(odd_numbs)

# Zadatak 24: Formatiranje numeričkih podataka iz liste stringova
# Napiši funkciju format_numeric_data koja prihvata listu stringova.
# Funkcija treba da vrati novu listu koja sadrži samo one elemente koji se mogu pretvoriti u broj.
# Ti elementi treba da budu pretvoreni u decimalni broj (float) i zaokruženi na dve decimale.
#
# Primer ulaza: ['10.5', 'error', '20.334', '15', 'fail']
# Očekivani izlaz: [10.5, 20.33, 15.0]

def format_numeric_data(data):

    return [round(float(item), 2) for item in data if item.isdigit() or item.__contains__('.')]

floats_ls = format_numeric_data(['10.5', 'error', '20.334', '15', 'fail'])
print(floats_ls)

# Zadatak 25: Zbir kvadrata parova elemenata
# Napiši funkciju sum_of_squares_pairs koja prihvata dve liste brojeva jednakih dužina.
# Koristeći zip i list comprehension,
# funkcija treba da vrati novu listu gde je svaki element zbir kvadrata odgovarajućih elemenata iz ulaznih listi.
#
# Ulaz A: [1, 2, 3]
# Ulaz B: [4, 5, 6]
# Očekivani izlaz: [17, 29, 45] (Jer je 1²+4²=17, 2²+5²=29, 3²+6²=45)

def sum_of_squares_pairs(l1, l2):

    return [i1**2 + i2**2 for i1, i2 in zip(l1,l2)]

output = sum_of_squares_pairs([1, 2, 3], [4, 5, 6])
print(output)

# Zadatak 26: Uslovno preimenovanje ključeva u rečniku
# Napiši funkciju conditional_key_rename koja prihvata rečnik (proizvod: cena).
# Kreiraj novi rečnik gde, ako je cena proizvoda veća od 100, ključu se dodaje prefiks "SKU_".
# U suprotnom, ključ ostaje isti.
#
# Primer ulaza: {'milk': 50, 'bread': 120, 'cheese': 80}
# Očekivani izlaz: {'milk': 50, 'SKU_bread': 120, 'cheese': 80}

def conditional_key_rename(data):

    return {
        f"SKU_{key}" if (value > 100) else key: value for key, value in data.items()
    }

output = conditional_key_rename( {'milk': 50, 'bread': 120, 'cheese': 80})
print(output)

# Zadatak 27: Sortiranje reči po dužini i abecedi
# Napiši funkciju sort_by_length_then_alphabet_desc koja prima listu stringova. Sortiraj listu po dva kriterijuma:
#
# Primarno po dužini reči, opadajuće (od najduže ka najkraćoj).
# Sekundarno po abecednom redu, takođe opadajuće (od Z ka A).
# Primer ulaza: ['apple', 'pie', 'banana', 'cat']
# Očekivani izlaz: ['banana', 'apple', 'pie', 'cat']

def sort_by_length_then_alphabet_desc(words):

    return sorted(words, key=lambda word: (len(word), word), reverse=True)

sorted_words = sort_by_length_then_alphabet_desc(['apple', 'pie', 'banana', 'cat'])
print(sorted_words)

# Zadatak 28: Brojanje samoglasnika
# Napiši funkciju koja prihvata string i vraća ukupan broj samoglasnika (a, e, i, o, u) u njemu,
# ne praveći razliku između velikih i malih slova.
#
# Primer ulaza: "Programiranje u Pythonu"
# Očekivani izlaz: 7
# Hint: Možeš proći kroz string i proveravati da li se svaki karakter nalazi u setu samoglasnika. Ne zaboravi lower().

def count_vowels(str_in: str) -> int:

    count = 0
    for ch in str_in:
        ch_lower = ch.lower()
        if ch_lower in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count

def count_vowels_2(str_in: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'} # Set je brži za pretragu od liste
    return sum(1 for ch in str_in.lower() if ch in vowels)

print(count_vowels("Programiranje u Pythonu"))

# Zadatak 29: Provera palindroma
# Napiši funkciju koja proverava da li je data reč palindrom (čita se isto s leva na desno i s desna na levo).
#
# Primer ulaza: "anavolimilovana"
# Očekivani izlaz: True
# Hint: String slicing [::-1] je veoma moćan alat za obrtanje.

def is_pal(str_in):

    return str_in == str_in[::-1]

# Zadatak 30: Obrtanje redosleda reči u rečenici
# Napiši funkciju koja prihvata rečenicu i vraća novu rečenicu sa obrnutim redosledom reči.
#
# Primer ulaza: "Python je zaista moćan jezik"
# Očekivani izlaz: "jezik moćan zaista je Python"
# Hint: Razmisli o metodama split() i join() za stringove.

def reverse_string(str_in):

    words = str_in.split()
    reversed_words = reversed(words)
    return " ".join(reversed_words)

out = reverse_string( "Python je zaista moćan jezik")
print(out)