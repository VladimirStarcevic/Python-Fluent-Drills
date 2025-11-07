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



