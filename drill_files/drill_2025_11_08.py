# Zadatak 38: Provera da li je lista sortirana
# Napiši funkciju koja proverava da li je lista brojeva sortirana u rastućem redosledu i vraća True ili False.
#
# Primer ulaza: [1, 3, 5, 8, 12]
# Očekivani izlaz: True


def is_sorted(numbs: list[int]) -> bool:

    sorted_ls = sorted(numbs)
    return numbs == sorted_ls


def is_sorted_ascending(numbers: list[int]) -> bool:

    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return  True

print(is_sorted_ascending( [1, 9, 25, 49, 81]))


# Zadatak 39: Lista kvadrata neparnih brojeva (List Comprehension)
# Koristeći list comprehension, kreiraj listu koja sadrži kvadrate neparnih brojeva od 1 do 10.
#
# Očekivani izlaz: [1, 9, 25, 49, 81]

def squared_list() -> list[int]:

    return [num**2 for num in range(1,11) if num % 2 != 0]

out = squared_list()
print(out)

# Zadatak 40: Filtriranje reči po dužini (List Comprehension)
# Data je lista reči. Koristeći list comprehension, vrati novu listu koja sadrži samo reči kraće od 5 karaktera.
#
# Primer ulaza: ['jabuka', 'auto', 'kuća', 'programiranje', 'most']
# Očekivani izlaz: ['auto', 'kuća', 'most']

def filter_list(words: list[str]) -> list[str]:
    return [word for word in words if len(word) < 5]

# Zadatak 41: Kumulativni zbir liste
# Napiši funkciju koja kao ulaz prima listu brojeva i vraća novu listu kumulativnih zbirova.
#
# Primer ulaza: [1, 2, 3, 4]
# Očekivani izlaz: [1, 3, 6, 10] (jer je 1, 1+2, 1+2+3, 1+2+3+4)
# Hint: Trebaće ti promenljiva koja pamti tekući zbir dok prolaziš kroz listu.

def sum_items_ls(nums: list[int]) -> list[int]:

    result = []
    adjustment_sum = 0
    for i in range(len(nums)):
        adjustment_sum += nums[i]
        result.append(adjustment_sum)
    return result

adjustment_list = sum_items_ls([1, 2, 3, 4])
print(adjustment_list)

# Zadatak 42: Premeštanje nula na kraj liste
# Napiši funkciju koja sve nule iz liste premešta na kraj, zadržavajući relativni redosled ostalih elemenata.
#
# Primer ulaza: [0, 1, 9, 0, 3, 0, 12]
# Očekivani izlaz: [1, 9, 3, 12, 0, 0, 0]
# Hint: Najjednostavnije je da kreiraš novu listu dodajući sve elemente koji nisu nula, a zatim na kraj dodaš potreban broj nula.

def zero_to_the_end(ls_zero: list[int]) -> list[int]:

    zero_ls = [zero for  zero in ls_zero if zero == 0]
    non_zero = [item for item in ls_zero if item != 0]
    return non_zero + zero_ls

transfer_ls = zero_to_the_end([0, 1, 9, 0, 3, 0, 12])
print(transfer_ls)