# Zadatak 28: Brojanje samoglasnika
# Napiši funkciju koja prihvata string i vraća ukupan broj samoglasnika (a, e, i, o, u) u njemu, ne praveći razliku između velikih i malih slova.
#
# Primer ulaza: "Programiranje u Pythonu"
# Očekivani izlaz: 7
# Hint: Možeš proći kroz string i proveravati da li se svaki karakter nalazi u setu samoglasnika. Ne zaboravi lower().
from contextlib import nullcontext


def count_vowels(input_str: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counter = 0
    for letter in input_str.lower():
        if letter in vowels:
            counter += 1
    return counter

def pythonic_counter(in_str: str) -> int:

    return sum(1 for letter in in_str.lower() if letter in {'a', 'e', 'i', 'o', 'u'})

print(pythonic_counter("Programiranje u Pythonu"))

# Zadatak 29: Provera palindroma
# Napiši funkciju koja proverava da li je data reč palindrom
# (čita se isto s leva na desno i s desna na levo).
#
# Primer ulaza: "anavolimilovana"
# Očekivani izlaz: True
# Hint: String slicing [::-1] je veoma moćan alat za obrtanje.

def check_palindrome(str_in: str) -> bool:
    return str_in == str_in[::-1]

print(check_palindrome("anavolimilovana"))

# Zadatak 30: Obrtanje redosleda reči u rečenici
# Napiši funkciju koja prihvata rečenicu i vraća novu rečenicu sa obrnutim redosledom reči.
#
# Primer ulaza: "Python je zaista moćan jezik"
# Očekivani izlaz: "jezik moćan zaista je Python"
# Hint: Razmisli o metodama split() i join() za stringove.

def inverse_sentence(sentence: str) -> str:

    word_list = sentence.split()
    return " ".join(word_list[::-1])

print(inverse_sentence("Python je zaista moćan jezik"))

# Zadatak 31: Zamena karaktera u stringu
# Napiši funkciju koja prihvata tri argumenta: originalni string, karakter koji treba zameniti i karakter kojim se zamenjuje.
# Funkcija treba da vrati novi string sa izvršenom zamenom.
#
# Primer ulaza: ("banana", "a", "o")
# Očekivani izlaz: "bonono"

def change_char_in_string(word: str, char_to_replace: str, replicant: str) -> str:

    new_string = ""
    for ch in word:
        if ch == char_to_replace:
            new_string += replicant
        else:
            new_string += ch
    return new_string

def change_char_in_string_pythonic(word: str, char_to_replace: str, replicant: str) -> str:
    return word.replace(char_to_replace, replicant)

def pythonic_char_edition_2(word: str, char_to_replace: str, replicant: str) -> str:
    return "".join(replicant if ch == char_to_replace else ch for ch in word)

string_out = change_char_in_string("banana", "a", "o")
print(string_out)

# Zadatak 32: Ekstrakcija brojeva iz stringa
# Napiši funkciju koja iz datog stringa izdvaja sve cifre i vraća ih kao listu celih brojeva.
#
# Primer ulaza: "Artikl A123 košta 45.99 dinara"
# Očekivani izlaz: [1, 2, 3, 4, 5, 9, 9]
# Hint: Metoda isdigit() može biti korisna za proveru da li je karakter cifra.

def extract_numbers_in_list(string_in: str) -> list[int]:

    return [int(char) for char in string_in if char.isdigit()]

input_string = "Artikl A123 košta 45.99 dinara"
numbs = extract_numbers_in_list(input_string)
print(numbs)