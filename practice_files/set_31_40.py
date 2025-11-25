# Zadatak 31: Zamena karaktera u stringu
# Napiši funkciju koja prihvata tri argumenta: originalni string, karakter koji treba zameniti i karakter kojim se zamenjuje.
# Funkcija treba da vrati novi string sa izvršenom zamenom.
#
# Primer ulaza: ("banana", "a", "o")
# Očekivani izlaz: "bonono"

def replace_chars(string_in: str, char: str, replacement: str) -> str:

    return string_in.replace(char, replacement)

out = replace_chars("banana", "a", "o")
print(out)

# Zadatak 32: Ekstrakcija brojeva iz stringa
# Napiši funkciju koja iz datog stringa izdvaja sve cifre i vraća ih kao listu celih brojeva.
#
# Primer ulaza: "Artikl A123 košta 45.99 dinara"
# Očekivani izlaz: [1, 2, 3, 4, 5, 9, 9]
# Hint: Metoda isdigit() može biti korisna za proveru da li je karakter cifra.

def extract_numbs(str_in: str) -> list[int]:

    return [int(ch) for ch in str_in if ch.isdigit()]


digits = extract_numbs("Artikl A123 košta 45.99 dinara")
print(digits)

# Zadatak 33: Uklanjanje duplikata iz liste (bez set)
# Napiši funkciju koja uklanja sve duplikate iz liste, ali zadržava originalni redosled elemenata. Ne koristi set za rešavanje.
#
# Primer ulaza: [1, 2, 5, 2, 3, 5, 1, 4]
# Očekivani izlaz: [1, 2, 5, 3, 4]
# Hint: Kreiraj praznu listu i dodaj elemente iz originalne samo ako se već ne nalaze u novoj listi.

def remove_duplicates(ls_in: list[int]) -> list[int]:

    new_ls = []
    for num in ls_in:
        if num not in new_ls:
            new_ls.append(num)
    return new_ls


og_ls = remove_duplicates( [1, 2, 5, 2, 3, 5, 1, 4])
print(og_ls)

# Zadatak 34: Spajanje i sortiranje dve liste
# Napiši funkciju koja spaja dve liste u jednu i zatim sortira tu novu listu u rastućem redosledu.
#
# Primer ulaza: ([3, 1, 5], [2, 4])
# Očekivani izlaz: [1, 2, 3, 4, 5]

def merging_lists(l1: list[int], l2: list[int]) -> list[int]:

    num1, num2 = l1, l2
    new_ls = num1 + num2

    return sorted(new_ls, key=lambda item: item)

merged_ls = merging_lists([3, 1, 5], [2, 4])
print(merged_ls)

# Zadatak 35: Rotacija liste ulevo
# Napiši funkciju koja rotira (pomera) elemente liste za N mesta ulevo.
#
# Primer ulaza: ([1, 2, 3, 4, 5, 6], 2)
# Očekivani izlaz: [3, 4, 5, 6, 1, 2]
# Hint: Slicing može da podeli listu na dva dela koja zatim možeš ponovo spojiti u drugačijem redosledu.

def rotate_list(numbs: list[int], n_rotations: int)-> list[int]:

    first_part = numbs[n_rotations:]
    second_part = numbs[:n_rotations]
    return first_part + second_part

ls_out = rotate_list([1, 2, 3, 4, 5, 6], 2)
print(ls_out)
