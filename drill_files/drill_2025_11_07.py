# Zadatak 33: Uklanjanje duplikata iz liste (bez set)
# Napiši funkciju koja uklanja sve duplikate iz liste, ali zadržava originalni redosled elemenata. Ne koristi set za rešavanje.
#
# Primer ulaza: [1, 2, 5, 2, 3, 5, 1, 4]
# Očekivani izlaz: [1, 2, 5, 3, 4]
# Hint: Kreiraj praznu listu i dodaj elemente iz originalne samo ako se već ne nalaze u novoj listi.

def remove_duplicate(numbs: list[int]) -> list[int]:

    filtered_list = []
    for num in numbs:
        if num not in filtered_list:
            filtered_list.append(num)
    return  filtered_list

out_ls = remove_duplicate( [1, 2, 5, 2, 3, 5, 1, 4])
print(out_ls)

# Zadatak 34: Spajanje i sortiranje dve liste
# Napiši funkciju koja spaja dve liste u jednu i zatim sortira tu novu listu u rastućem redosledu.
#
# Primer ulaza: ([3, 1, 5], [2, 4])
# Očekivani izlaz: [1, 2, 3, 4, 5]

def merge_lists(tuple_ls):

    items_1, items_2 = tuple_ls
    new_list = items_1 + items_2
    return sorted(new_list, key=lambda num: num)

out = merge_lists(([3, 1, 5], [2, 4]))
print(out)

# Zadatak 35: Rotacija liste ulevo
# Napiši funkciju koja rotira (pomera) elemente liste za N mesta ulevo.
#
# Primer ulaza: ([1, 2, 3, 4, 5, 6], 2)
# Očekivani izlaz: [3, 4, 5, 6, 1, 2]
# Hint: Slicing može da podeli listu na dva dela koja zatim možeš ponovo spojiti u drugačijem redosledu.

def rotate_list_left(data: list, n: int) -> list:

    result_list = list(data)
    for _ in range(n):
        first_item = result_list.pop(0)

        result_list.append(first_item)
    return result_list

def rotate_list_pythonic(data: list, n: int) -> list:

    return data[n:] + data[:n]

rot_ls = rotate_list_pythonic([1, 2, 3, 4, 5, 6], 2)
print(rot_ls)

# Zadatak 36: Pronalaženje drugog najvećeg broja
# Napiši funkciju koja pronalazi i vraća drugi po veličini broj u listi brojeva.
#
# Primer ulaza: [10, 45, 99, 4, 20]
# Očekivani izlaz: 45
# Hint: Jednostavan način je da sortiraš listu. Pazi na slučajeve sa duplikatima ili ako lista ima manje od dva elementa.


def find_second_value_item(numbers: list[int]) -> int:

    sorted_ls = sorted(numbers, reverse=True)
    return sorted_ls[1]


def find_second_largest_unique(numbers: list[int]) -> int:
    # 1. Ukloni duplikate konverzijom u set
    unique_numbers = set(numbers)

    # Provera: Šta ako ima manje od dva jedinstvena broja?
    if len(unique_numbers) < 2:
        return None  # Ili baci grešku, zavisno od zahteva

    # 2. Sortiraj jedinstvene brojeve
    sorted_unique = sorted(list(unique_numbers), reverse=True)

    # 3. Vrati drugi element
    return sorted_unique[1]

print(find_second_value_item([10, 45, 99, 4, 20]))

# Zadatak 37: "Spljoštavanje" ugnežđene liste
# Napiši funkciju koja listu listi (ugnežđenu listu) pretvara u jednu jedinstvenu listu.
#
# Primer ulaza: [[1, 2], [3, 4, 5], [6]]
# Očekivani izlaz: [1, 2, 3, 4, 5, 6]
# Hint: Možeš koristiti ugnežđenu petlju (nested loop) ili list comprehension.

def get_list_from_mtx(matrix: list[list[int]]) -> list[int]:

    return [num for sublist in matrix for num in sublist]

ls_1d = get_list_from_mtx([[1, 2], [3, 4, 5], [6]])
print(ls_1d)