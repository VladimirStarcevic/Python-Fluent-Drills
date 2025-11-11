# Zadatak 49: Ažuriranje vrednosti u rečniku
# Napiši funkciju koja prima rečnik i listu ključeva. Za svaki ključ iz liste, udvostručи njegovu vrednost u rečniku.
#
# Primer ulaza: ({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
# Očekivani izlaz: {'a': 2, 'b': 2, 'c': 6}

def double_values_for_keys(data: dict[str, int], keys_to_update: list[str]) -> dict[str, int]:


    if not data:
        return {}
    for key in keys_to_update:

        if key in data:
            data[key] *= 2
    return data

updated_map = double_values_for_keys({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])
print(updated_map)

# Zadatak 50: Rečnik parnih i neparnih brojeva
# Napiši funkciju koja razvrstava brojeve iz liste u rečnik sa dva ključa: 'parni' i 'neparni'.
#
# Primer ulaza: [1, 2, 3, 4, 5, 6]
# Očekivani izlaz: {'parni': [2, 4, 6], 'neparni': [1, 3, 5]}

def group_by_parity(numbers: list[int]) -> dict[str, list[int]]:

    if not numbers:
        return {}
    result = {'even': [], 'odd': []}
    for num in numbers:
        if num % 2 == 0:
            result['even'].append(num)
        else:
            result['odd'].append(num)
    return result


even_odd_map = group_by_parity([1, 2, 3, 4, 5, 6])
print(even_odd_map)