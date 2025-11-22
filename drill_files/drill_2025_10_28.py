 # DRILL 24:
 # Zahtev: Primiti listu sirovih stringova. Filtrirati i vratiti listu stringova koja sadrži samo brojeve. Brojeve formatirati tako da budu Float tipa sa dve decimale.
 # Input: ['10.5', 'error', '20.334', '15', 'fail']
 # Output: [10.50, 20.33, 15.00]

def is_item_convertable(item) -> bool:
    try:
        float(item)
        return True
    except ValueError:
        return False

def format_numeric_data(data_list: list) -> list:
    """Filters list for numeric strings, converts to float, and handles formatting."""

    return [
        round(float(str_item), 2) for str_item in data_list if is_item_convertable(str_item)
    ]

data = ['10.5', 'error', '20.334', '15', 'fail']
clean_digit_list = format_numeric_data(data)
print(clean_digit_list)


# DRILL 25:
# Zahtev: Primiti dve liste brojeva (koje su iste dužine). Vratiti listu koja sadrži zbir kvadrata odgovarajućih elemenata.
# Input A: [1, 2, 3]
# Input B: [4, 5, 6]
# Output: [17, 29, 45]

def sum_of_squares_pairs(list_a: list, list_b: list) -> list:
    """Uses zip and LC to calculate the sum of squares for paired elements."""
    return [(item1**2 + item2**2) for item1, item2 in zip(list_a, list_b)]

in_a = [1, 2, 3]
in_b = [4, 5, 6]
out_c = sum_of_squares_pairs(in_a, in_b)
print(out_c)

# DRILL 26:
 # Zahtev: Primiti rečnik (proizvod: cena). Kreirati novi rečnik. Ako je cena veća od 100, ključ treba da postane "SKU_" + proizvod. U suprotnom, ključ ostaje isti.
 # Input: {'milk': 50, 'bread': 120, 'cheese': 80}
 # Output: {'milk': 50, 'SKU_bread': 120, 'cheese': 80}

def conditional_key_rename(prices: dict) -> dict:
    """Uses DC and Ternary Operator to conditionally rename the dictionary key."""
    return {
        ("SKU_" + product) if (price > 100) else product: price for product, price in prices.items()
    }

product_list =  {'milk': 50, 'bread': 120, 'cheese': 80}
filtered_list = conditional_key_rename(product_list)
print(filtered_list)

# DRILL 27:
 # Zahtev: Primiti listu stringova. Sortirati listu primarno po dužini reči (rastuće) i sekundarno po abecedi (opadajuće).
 # Input: ['apple', 'pie', 'banana', 'cat']
 # Output: ['pie', 'cat', 'apple', 'banana']

def sort_by_length_then_alphabet_desc(words: list) -> list:
    """Uses lambda to sort by multiple criteria (length: asc, word: desc)."""
    return sorted(words, key=lambda word: (len(word), word), reverse=True)

in_ls = ['apple', 'pie', 'banana', 'cat']
out_ls = sort_by_length_then_alphabet_desc(in_ls)
print(out_ls)

# Zadatak 29: Provera palindroma
 # Napiši funkciju koja proverava da li je data reč palindrom (čita se isto s leva na desno i s desna na levo).
 #
 # Primer ulaza: "anavolimilovana"
 # Očekivani izlaz: True
 # Hint: String slicing [::-1] je veoma moćan alat za obrtanje.




