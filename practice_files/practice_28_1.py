# Zadatak 28: Brojanje samoglasnika
# Napiši funkciju koja prihvata string i vraća ukupan broj samoglasnika (a, e, i, o, u) u njemu, ne praveći razliku između velikih i malih slova.
#
# Primer ulaza: "Programiranje u Pythonu"
# Očekivani izlaz: 7
# Hint: Možeš proći kroz string i proveravati da li se svaki karakter nalazi u setu samoglasnika. Ne zaboravi lower().


def vowel_counter(sentence: str) -> int:

    counter = 0
    for ch in sentence:
        ch_lower = ch.lower()
        if ch_lower in ['a', 'e', 'i', 'o', 'u']:
            counter += 1
    return counter

number = vowel_counter("Programiranje u Pythonu")
print(f"Number pf vowels in sentence: {number}")

# Zadatak 29: Provera palindroma
# Napiši funkciju koja proverava da li je data reč palindrom (čita se isto s leva na desno i s desna na levo).
#
# Primer ulaza: "anavolimilovana"
# Očekivani izlaz: True
# Hint: String slicing [::-1] je veoma moćan alat za obrtanje.

def checking_palindrome(string_in: str) -> bool:
    return string_in == string_in[::-1]

print(checking_palindrome("anavolimilovana"))

# Zadatak 30: Obrtanje redosleda reči u rečenici
# Napiši funkciju koja prihvata rečenicu i vraća novu rečenicu sa obrnutim redosledom reči.
#
# Primer ulaza: "Python je zaista moćan jezik"
# Očekivani izlaz: "jezik moćan zaista je Python"
# Hint: Razmisli o metodama split() i join() za stringove.

def reverse_order(str_in: str) -> str:

    words = str_in.split()
    return " ".join(reversed(words))

str_out = reverse_order("Python je zaista moćan jezik")
print(str_out)

# Zadatak 31: Zamena karaktera u stringu
# Napiši funkciju koja prihvata tri argumenta: originalni string, karakter koji treba zameniti i karakter kojim se zamenjuje. Funkcija treba da vrati novi string sa izvršenom zamenom.
#
# Primer ulaza: ("banana", "a", "o")
# Očekivani izlaz: "bonono"

def replacing_char(word: str, char: str, replacement: str) -> str:

    return word.replace(char, replacement)

out = replacing_char("banana", "a", "o")
print(out)

# Zadatak 32: Ekstrakcija brojeva iz stringa
# Napiši funkciju koja iz datog stringa izdvaja sve cifre i vraća ih kao listu celih brojeva.
#
# Primer ulaza: "Artikl A123 košta 45.99 dinara"
# Očekivani izlaz: [1, 2, 3, 4, 5, 9, 9]
# Hint: Metoda isdigit() može biti korisna za proveru da li je karakter cifra.

def extract_numbers(mix_string: str) -> list[int]:

    digit_list = []
    for ch in mix_string:
        if ch.isdigit():
            digit_list.append(int(ch))
    return digit_list

def extract_lc(mix: str) -> list[int]:

    return [int(ch) for ch in mix if ch.isdigit()]

digits = extract_lc("Artikl A123 košta 45.99 dinara")
print(digits)