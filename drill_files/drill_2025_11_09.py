# Zadatak 43: Inverzija rečnika
# Napiši funkciju koja zamenjuje mesta ključevima i vrednostima u rečniku. Pretpostavi da su sve vrednosti jedinstvene.
#
# Primer ulaza: {'ime': 'Pera', 'grad': 'Beograd'}
# Očekivani izlaz: {'Pera': 'ime', 'Beograd': 'grad'}

def inversion_of_map(data: dict[str, str]) -> dict[str, str]:

    return {v: k for k, v in data.items()}

out_dict = inversion_of_map({'ime': 'Pera', 'grad': 'Beograd'})
print(out_dict)

# Zadatak 44: Brojanje frekvencije reči u tekstu
# Napiši funkciju koja prihvata tekst (string) i vraća rečnik gde su ključevi reči iz teksta, a vrednosti broj njihovih pojavljivanja.
#
# Primer ulaza: "pas mačka pas ptica mačka pas"
# Očekivani izlaz: {'pas': 3, 'mačka': 2, 'ptica': 1}
# Hint: Rečnik je idealan za ovo. Metoda dict.get(kljuc, 0) može biti veoma korisna za elegantno brojanje.

def count_letters(sentence: str) -> dict[str, int]:

    word_counter = {}
    words = sentence.split()
    for word in words:
        word_counter[word] = word_counter.get(word, 0) + 1
    return word_counter

counter_strike = count_letters("pas mačka pas ptica mačka pas")
print(counter_strike)

# Zadatak 45: Pronalaženje ključa sa najvećom vrednošću
# Napiši funkciju koja vraća ključ koji ima najveću numeričku vrednost u rečniku.
#
# Primer ulaza: {'fizika': 88, 'matematika': 95, 'hemija': 91}
# Očekivani izlaz: 'matematika'
# Hint: Istraži kako se koristi key argument u max() funkciji.

def get_key_with_max_value(dict_in: dict[str, int]) -> str:

    return max(dict_in, key=lambda item: dict_in[item])

key_with_max_score = get_key_with_max_value({'fizika': 88, 'matematika': 95, 'hemija': 91})
print(key_with_max_score)

# Zadatak 46: Rečnik kvadrata (Dictionary Comprehension)
# Koristeći dictionary comprehension, kreiraj rečnik gde su ključevi brojevi od 1 do 5, a vrednosti njihovi kvadrati.
#
# Očekivani izlaz: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def get_map_of_squares() -> dict[int, int]:

    squares_map = {}
    for idx in range(1, 6):
        squares_map[idx] = idx**2
    return squares_map

sq_map = get_map_of_squares()
print(sq_map)

# Zadatak 47: Filtriranje rečnika po vrednosti (Dictionary Comprehension)
# Dat je rečnik (proizvod: cena). Vrati novi rečnik koji sadrži samo proizvode čija je cena veća od 100.
#
# Primer ulaza: {'Laptop': 1200, 'Miš': 50, 'Tastatura': 150}
# Očekivani izlaz: {'Laptop': 1200, 'Tastatura': 150}

def filter_map(data: dict[str, int]) -> dict[str, int]:

    return {k: v for k,v in data.items() if v > 100}


out_map = filter_map({'Laptop': 1200, 'Miš': 50, 'Tastatura': 150})
print(out_map)

# Zadatak 48: Grupisanje elemenata po nekoj osobini
# Data je lista reči. Grupiši ih u rečnik gde je ključ dužina reči, a vrednost lista svih reči te dužine.
#
# Primer ulaza: ['jedan', 'dva', 'tri', 'četiri', 'pet']
# Očekivani izlaz: {5: ['jedan', 'četiri'], 3: ['dva', 'tri', 'pet']}
# Hint: Prolazi kroz listu reči. Za svaku reč, proveri da li ključ (njena dužina) postoji u rečniku. Ako ne, kreiraj ga sa listom, a zatim dodaj reč.

# Kreiraj prazan rečnik (groups = {}).
# Iteriraj kroz listu reči.
# Za svaku reč:
# Izračunaj njenu dužinu (key = len(word)).
# Proveri da li taj ključ (dužina) već postoji u groups.
# Ako ne postoji, kreiraj novi unos: groups[key] = [word].
# Ako postoji, samo dodaj reč u postojeću listu: groups[key].append(word).
# Vrati rečnik.
def get_words_map(data: list[str]) -> dict[int, list[str]]:

    groups = {}
    for word in data:
        key = len(word)
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return groups

def get_words_map_setdefault(data: list[str]) -> dict[int, list[str]]:
    groups = {}
    for word in data:
        # "Pronađi ključ. Ako ne postoji, postavi ga na []. Zatim na tu listu dodaj reč."
        groups.setdefault(len(word), []).append(word)
    return groups

recnik = get_words_map(['jedan', 'dva', 'tri', 'četiri', 'pet'])
print(recnik)




