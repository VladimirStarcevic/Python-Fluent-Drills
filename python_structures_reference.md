# Python Motorika - Kompletna Referenca za Strukture i Metode

**Autor**: Vladimir Starčević  
**Datum**: 25. oktobar 2025.  
**Svrha**: Centralizovana dokumentacija za NotebookML i dnevnu upotrebu

---

## I. TIPOVI PODATAKA I MUTABILNOST

### Pregled Osnovnih Struktura

| Tip | Sintaksa | Povratna Vrednost | Mutabilnost | Ključna Karakteristika |
|-----|----------|-------------------|-------------|------------------------|
| **Lista** | `[]` ili `list()` | `list` | ✅ MUTABILNA | Glavna sekvenca. Može se menjati na mestu (in-place) |
| **Torka** | `()` ili `tuple()` | `tuple` | ❌ IMUTABILNA | Za fiksne podatke (koordinate, konstante). Ne može se menjati |
| **Rečnik** | `{}` ili `dict()` | `dict` | ✅ MUTABILAN | Hash tabela. Brz lookup O(1). Key-value parovi |
| **Set** | `{1, 2}` ili `set()` | `set` | ✅ MUTABILAN | Samo jedinstveni elementi. Brza provera pripadnosti O(1) |

### Mutabilnost - Dubinsko Objašnjenje

#### Mutabilne Strukture (Lista, Rečnik, Set)

```python
# MUTABILNO: Menja se NA MESTU (isti objekat u memoriji)
lista = [1, 2, 3]
print(id(lista))  # npr. 140234567890
lista.append(4)
print(id(lista))  # ISTI ID! 140234567890

# Ovo znači da sve reference pokazuju na ISTU izmenjenu listu
originalna = [1, 2, 3]
kopija = originalna  # NE pravi kopiju, samo pokazuje na isti objekat!
kopija.append(4)
print(originalna)  # [1, 2, 3, 4] - izmenjena!
```

**Implikacija**: Kada funkcija prima mutabilnu strukturu, ona može da je izmeni bez `return` (side effect).

#### Imutabilne Strukture (Torka, String, Int, Float)

```python
# IMUTABILNO: Svaka "izmena" kreira NOVI objekat
torka = (1, 2, 3)
print(id(torka))  # npr. 140234567890
# torka.append(4)  # AttributeError! Torka nema metode za izmenu
nova_torka = torka + (4,)  # Kreira NOVU torku
print(id(nova_torka))  # DRUGAČIJI ID!

#Stringovi su takođe imutabilni
s = "Hello"
s_upper = s.upper()  # Kreira NOVI string, ne menja originalni
```

**Implikacija**: Sigurnost od nenamerne izmene. Torke su idealne za ključeve u rečnicima (jer su hashable).

---

## II. METODE LISTE - MODIFIKUJUĆE (In-Place)

Ove metode **menjaju originalnu listu** i vraćaju `None`.

### 1. `list.append(item)` - Dodavanje na Kraj

```python
# Sintaksa
lista.append(element)

# Povratna vrednost: None
# Složenost: O(1) - konstantno vreme

# Primer
imena = ['Ana', 'Marko']
imena.append('Petar')
print(imena)  # ['Ana', 'Marko', 'Petar']

# Greška početnnika:
result = imena.append('Jovana')  # result je None!
```

**Motorika**: `append()` je najčešće korišćena metoda za akumulaciju u petljama.

---

### 2. `list.insert(index, item)` - Ubacivanje na Poziciju

```python
# Sintaksa
lista.insert(indeks, element)

# Povratna vrednost: None
# Složenost: O(N) - mora da pomeri sve elemente desno od indeksa

# Primer
brojevi = [1, 2, 4]
brojevi.insert(2, 3)  # Ubaci 3 na indeks 2
print(brojevi)  # [1, 2, 3, 4]

# OPREZ: insert na početak je SPOR!
brojevi.insert(0, 0)  # O(N) - pomera sve elemente
```

**Motorika**: Retko se koristi (jer je spor). Preferiraj `append()` i `sort()` ili `deque` za efikasne operacije na početku.

---

### 3. `list.pop(index=-1)` - Uklanjanje i Vraćanje

```python
# Sintaksa
element = lista.pop(indeks)  # Default: -1 (poslednji)

# Povratna vrednost: Uklonjeni element
# Složenost: O(1) za kraj, O(N) za početak/sredinu

# Primer
stack = [1, 2, 3, 4]
poslednji = stack.pop()  # 4
print(stack)  # [1, 2, 3]

# Uklanjanje sa početka (SPORO!)
prvi = stack.pop(0)  # 1 (O(N) operacija)
```

**Motorika**: `pop()` je osnova za LIFO Stack implementaciju. `pop(0)` = FIFO Queue (ali SPORO - koristi `collections.deque`).

---

### 4. `list.remove(value)` - Uklanjanje po Vrednosti

```python
# Sintaksa
lista.remove(vrednost)

# Povratna vrednost: None
# Složenost: O(N) - mora pronaći element
# OPREZ: ValueError ako element ne postoji!

# Primer
voće = ['jabuka', 'kruška', 'jabuka', 'banana']
voće.remove('jabuka')  # Uklanja PRVO pojavljivanje
print(voće)  # ['kruška', 'jabuka', 'banana']

# Bezbedno uklanjanje (ako ne znaš da li postoji)
if 'višnja' in voće:
    voće.remove('višnja')
```

**Motorika**: Uklanja **samo prvo pojavljivanje**. Za uklanjanje svih: koristi List Comprehension.

---

### 5. `list.sort(key=None, reverse=False)` - Sortiranje na Mestu

```python
# Sintaksa
lista.sort(key=funkcija, reverse=True/False)

# Povratna vrednost: None (sortira IN-PLACE!)
# Složenost: O(N log N) - Timsort algoritam

# Osnovno sortiranje
brojevi = [3, 1, 4, 1, 5]
brojevi.sort()
print(brojevi)  # [1, 1, 3, 4, 5]

# Opadajuće sortiranje
brojevi.sort(reverse=True)
print(brojevi)  # [5, 4, 3, 1, 1]

# Sortiranje po custom logici (key funkcija)
studenti = [
    {'ime': 'Ana', 'ocena': 85},
    {'ime': 'Marko', 'ocena': 92},
    {'ime': 'Petar', 'ocena': 78}
]
studenti.sort(key=lambda s: s['ocena'], reverse=True)
# Sorted: Marko (92), Ana (85), Petar (78)
```

**Motorika**: `sort()` vs `sorted()` - `sort()` menja originalnu listu (`None`), `sorted()` vraća NOVU sortiranu listu (originalna netaknuta).

---

## III. METODE LISTE - NE-MODIFIKUJUĆE (Query)

Ove metode **ne menjaju** originalnu listu, već vraćaju informaciju.

### 1. `list.count(value)` - Prebrojavanje

```python
# Sintaksa
broj = lista.count(vrednost)

# Povratna vrednost: int
# Složenost: O(N)

# Primer
ocena = [5, 4, 5, 3, 5, 4]
broj_petica = ocena.count(5)
print(broj_petica)  # 3
```

**Motorika**: Korisno za frekventnu analizu (koliko puta se nešto pojavljuje).

---

### 2. `list.index(value, start=0, stop=len)` - Pronalaženje Indeksa

```python
# Sintaksa
indeks = lista.index(vrednost, start, stop)

# Povratna vrednost: int (indeks prvog pojavljivanja)
# Složenost: O(N)
# OPREZ: ValueError ako element ne postoji!

# Primer
slova = ['a', 'b', 'c', 'b', 'd']
pozicija = slova.index('b')
print(pozicija)  # 1 (prvo pojavljivanje)

# Bezbedno pronalaženje
if 'x' in slova:
    print(slova.index('x'))
else:
    print("Element ne postoji")
```

**Motorika**: Vraća **samo prvi indeks**. Za sve indekse: koristi List Comprehension sa `enumerate()`.

---

## IV. REČNIK (DICT) - METODE I MOTORIKA

Rečnik je **hash tabela** (lookup u O(1)). Ključevi moraju biti **hashable** (imutabilni tipovi).

### 1. `dict[key] = value` - Dodavanje/Ažuriranje

```python
# Sintaksa
d[ključ] = vrednost

# Ponašanje:
# - Ako ključ ne postoji → dodaje novi par
# - Ako ključ postoji → PREPISUJE vrednost

# Primer
student = {'ime': 'Ana', 'ocena': 85}
student['fakultet'] = 'ETF'  # Dodaje novi ključ
student['ocena'] = 90  # Ažurira postojeću vrednost
print(student)  # {'ime': 'Ana', 'ocena': 90, 'fakultet': 'ETF'}
```

**Motorika**: **Nema potrebe** za `if key in dict:` provere kada ažuriraš/dodaješ. Direktna dodela UVEK radi.

---

### 2. `dict.get(key, default=None)` - Bezbedno Dohvatanje

```python
# Sintaksa
vrednost = d.get(ključ, default_vrednost)

# Povratna vrednost: Vrednost ključa ILI default (ako ključ ne postoji)
# Složenost: O(1)

# Problem: KeyError
d = {'a': 1, 'b': 2}
# print(d['c'])  # KeyError!

# Rešenje 1: Provera
if 'c' in d:
    print(d['c'])

# Rešenje 2: .get() (PREFERIRANO!)
print(d.get('c', 0))  # 0 (default)

# ČEST PATTERN: Brojač
counter = {}
for slovo in 'hello':
    counter[slovo] = counter.get(slovo, 0) + 1
print(counter)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

**Motorika**: `get()` je **must-have** za brojače, akumulatore, i bilo koji pattern gde ključ možda ne postoji.

---

### 3. `dict.items()` - Iteracija preko Parova

```python
# Sintaksa
for kljuc, vrednost in d.items():
    # ...

# Povratna vrednost: dict_items view (iterable of tuples)
# Složenost: O(N) za iteraciju

# Primer
student = {'ime': 'Ana', 'ocena': 85, 'smer': 'IT'}
for k, v in student.items():
    print(f"{k}: {v}")
# ime: Ana
# ocena: 85
# smer: IT

# Dictionary Comprehension (filter)
visoke_ocene = {k: v for k, v in student.items() if isinstance(v, int) and v > 80}
```

**Motorika**: `items()` je najčešći način za iteraciju preko rečnika kada ti trebaju **i ključ i vrednost**.

---

### 4. `dict.pop(key, default=None)` - Uklanjanje i Vraćanje

```python
# Sintaksa
vrednost = d.pop(ključ, default)

# Povratna vrednost: Vrednost uklonjenog ključa ILI default (ako ključ ne postoji)
# Složenost: O(1)

# Primer
d = {'a': 1, 'b': 2, 'c': 3}
vrednost = d.pop('b')
print(vrednost)  # 2
print(d)  # {'a': 1, 'c': 3}

# Bezbedno uklanjanje
nepostojeća = d.pop('x', 'Nema ga')
print(nepostojeća)  # 'Nema ga'
```

**Motorika**: `pop()` je atomska operacija (ukloni + vrati vrednost). Korisno za "consume" pattern.

---

### 5. `{**dict1, **dict2}` - Unpacking Operator (Spajanje)

```python
# Sintaksa
novi_dict = {**d1, **d2}

# Ponašanje: Kreira NOVI rečnik spajanjem d1 i d2
# PRAVILO: d2 prepisuje preklapajuće ključeve iz d1

# Primer
base = {'ime': 'Ana', 'ocena': 85}
update = {'ocena': 90, 'smer': 'IT'}
merged = {**base, **update}
print(merged)  # {'ime': 'Ana', 'ocena': 90, 'smer': 'IT'}

# Praktična Primena: FastAPI response formatting
def format_response(data, status='success'):
    return {**data, 'status': status, 'timestamp': '2025-10-25'}

result = format_response({'user': 'Vladimir', 'score': 100})
# {'user': 'Vladimir', 'score': 100, 'status': 'success', 'timestamp': '2025-10-25'}
```

**Motorika**: Unpacking je **elegantan način** za spajanje rečnika bez mutacije originala. Korisno za immutability pattern.

---

## V. BUILT-IN FUNKCIJE - COMPREHENSIONS

### 1. List Comprehension (LC)

```python
# Sintaksa
nova_lista = [izraz for element in iterable if uslov]

# Povratna vrednost: list
# Složenost: O(N) za iteraciju + O(f(x)) za svaki izraz

# Osnovni Primeri
# 1. Transformacija
brojevi = [1, 2, 3, 4, 5]
kvadrati = [x**2 for x in brojevi]  # [1, 4, 9, 16, 25]

# 2. Filtriranje
parni = [x for x in brojevi if x % 2 == 0]  # [2, 4]

# 3. Transformacija + Filtriranje
parne_kvadrate = [x**2 for x in brojevi if x % 2 == 0]  # [4, 16]

# 4. Ternarni operator (if-else NA POČETKU)
kategorizacija = ['parno' if x % 2 == 0 else 'neparno' for x in brojevi]
# ['neparno', 'parno', 'neparno', 'parno', 'neparno']
```

**Motorika**: LC je **najčešće korišćena tehnika** za transformaciju/filtriranje. Zamenjuje `map()` i `filter()`.

#### Napredni Primeri

```python
# Nested LC (matrica)
matrica = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Flattening (ravnanje nested liste)
nested = [[1, 2], [3, 4], [5]]
flat = [x for sublist in nested for x in sublist]
# [1, 2, 3, 4, 5]

# Sa funkcijom
def kvadriraj(x):
    return x ** 2

rezultat = [kvadriraj(x) for x in range(5)]  # [0, 1, 4, 9, 16]
```

---

### 2. Dictionary Comprehension (DC)

```python
# Sintaksa
novi_dict = {kljuc_izraz: vrednost_izraz for element in iterable if uslov}

# Povratna vrednost: dict
# Složenost: O(N)

# Primeri

# 1. Kreiranje rečnika iz liste
imena = ['Ana', 'Marko', 'Petar']
duzine = {ime: len(ime) for ime in imena}
# {'Ana': 3, 'Marko': 5, 'Petar': 5}

# 2. Filtriranje postojećeg rečnika
ocene = {'Ana': 85, 'Marko': 92, 'Petar': 78, 'Jovana': 88}
visoke_ocene = {k: v for k, v in ocene.items() if v >= 85}
# {'Ana': 85, 'Marko': 92, 'Jovana': 88}

# 3. Transformacija vrednosti
cene_eur = {'jabuka': 2, 'kruška': 3, 'banana': 1.5}
cene_din = {voće: cena * 117 for voće, cena in cene_eur.items()}
# {'jabuka': 234, 'kruška': 351, 'banana': 175.5}

# 4. Invertovanje rečnika (swap key-value)
original = {'a': 1, 'b': 2, 'c': 3}
invertovan = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b', 3: 'c'}
```

**Motorika**: DC je **ključan alat** za transformaciju/filtriranje rečnika bez petlji. Kraći, čitljiviji kod.

---

### 3. Ternarni Operator (Ternary Expression)

```python
# Sintaksa
vrednost = A if USLOV else B

# Ponašanje:
# - Ako USLOV je True → vraća A
# - Ako USLOV je False → vraća B

# PRAVILO: Mora imati 'else' deo (za razliku od if-filtera u LC)

# Primeri

# 1. Jednostavna dodela
x = 10
status = 'pozitivan' if x > 0 else 'negativan'

# 2. U List Comprehension (if-else NA POČETKU)
brojevi = [1, 2, 3, 4, 5]
kategorije = ['parno' if x % 2 == 0 else 'neparno' for x in brojevi]

# 3. U funkcijama
def apsolutna(x):
    return x if x >= 0 else -x

# 4. Nested Ternary (kompleksno, ali moguće)
ocena = 92
rang = 'A' if ocena >= 90 else 'B' if ocena >= 80 else 'C' if ocena >= 70 else 'F'
```

**Motorika**: Ternarni operator je **obavezan** za transformaciju sa uslovima u LC. Kompaktniji od `if-else` bloka.

#### Kritična Razlika: if-else vs if-filter u LC

```python
brojevi = [1, 2, 3, 4, 5]

# GREŠKA: if bez else na početku
# nevalidan = [x**2 if x % 2 == 0 for x in brojevi]  # SyntaxError!

# ISPRAVNO 1: Ternarni (if-else na početku) - TRANSFORMACIJA
kvadrati_ili_nula = [x**2 if x % 2 == 0 else 0 for x in brojevi]
# [0, 4, 0, 16, 0]

# ISPRAVNO 2: if-filter (if na kraju) - FILTRIRANJE
samo_parni_kvadrati = [x**2 for x in brojevi if x % 2 == 0]
# [4, 16]
```

---

## VI. ALATI ZA ITERACIJU

### 1. `enumerate(iterable, start=0)` - Indeksiranje + Iteracija

```python
# Sintaksa
for indeks, element in enumerate(lista, start=0):
    # ...

# Povratna vrednost: enumerate objekat (iterator of tuples)
# Složenost: O(N)

# Primeri

# 1. Osnovno (indeksiranje od 0)
voće = ['jabuka', 'kruška', 'banana']
for i, v in enumerate(voće):
    print(f"{i}: {v}")
# 0: jabuka
# 1: kruška
# 2: banana

# 2. Sa custom start (npr. rangiranje od 1)
studenti = ['Ana', 'Marko', 'Petar']
for rang, ime in enumerate(studenti, start=1):
    print(f"#{rang}: {ime}")
# #1: Ana
# #2: Marko
# #3: Petar

# 3. U List Comprehension
indexed_lista = [(i, x) for i, x in enumerate(voće)]
# [(0, 'jabuka'), (1, 'kruška'), (2, 'banana')]

# 4. Filtriranje po indeksu
parni_indeksi = [x for i, x in enumerate(voće) if i % 2 == 0]
# ['jabuka', 'banana']
```

**Motorika**: `enumerate()` **eliminiše potrebu** za ručnim brojačem (`i = 0; i += 1`). Pythoničniji pristup.

---

### 2. `zip(*iterables)` - Sinhronizovano Spajanje

```python
# Sintaksa
for elem1, elem2, ... in zip(iter1, iter2, ...):
    # ...

# Povratna vrednost: zip objekat (iterator of tuples)
# Složenost: O(min(len(iter1), len(iter2), ...))
# PRAVILO: Zaustavlja se na najkraćoj listi

# Primeri

# 1. Osnovno spajanje dve liste
imena = ['Ana', 'Marko', 'Petar']
ocene = [85, 92, 78]
for ime, ocena in zip(imena, ocene):
    print(f"{ime}: {ocena}")
# Ana: 85
# Marko: 92
# Petar: 78

# 2. Kreiranje rečnika
student_dict = {ime: ocena for ime, ocena in zip(imena, ocene)}
# {'Ana': 85, 'Marko': 92, 'Petar': 78}

# 3. Paralelna transformacija
x = [1, 2, 3]
y = [4, 5, 6]
zbir = [a + b for a, b in zip(x, y)]
# [5, 7, 9]

# 4. Tri (ili više) liste
names = ['Ana', 'Marko']
ages = [25, 30]
cities = ['Beograd', 'Novi Sad']
combined = list(zip(names, ages, cities))
# [('Ana', 25, 'Beograd'), ('Marko', 30, 'Novi Sad')]

# 5. "Unzip" (Transponovanje)
paired = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*paired)
print(nums)    # (1, 2, 3)
print(letters) # ('a', 'b', 'c')
```

**Motorika**: `zip()` je **ključan** za sinhronizovanu iteraciju. Eliminiše potrebu za indeksiranjem (`for i in range(len(lista))`).

---

### 3. `max()` i `min()` sa `key` Parametrom - Agregacija

```python
# Sintaksa
maksimum = max(iterable, key=lambda x: izraz)
minimum = min(iterable, key=lambda x: izraz)

# Povratna vrednost: Element sa maksimalnom/minimalnom vrednošću
# Složenost: O(N)

# PRAVILO: key funkcija definiše PO ČEMU se poredi

# Primeri

# 1. Osnovno (bez key) - direktna vrednost
brojevi = [3, 1, 4, 1, 5, 9, 2]
print(max(brojevi))  # 9
print(min(brojevi))  # 1

# 2. Lista torki/lista - sortiranje po drugom elementu
studenti = [
    ('Ana', 85),
    ('Marko', 92),
    ('Petar', 78)
]
najbolji = max(studenti, key=lambda s: s[1])
print(najbolji)  # ('Marko', 92)

najslabiji = min(studenti, key=lambda s: s[1])
print(najslabiji)  # ('Petar', 78)

# 3. Lista rečnika - sortiranje po vrednosti ključa
ocene = [
    {'ime': 'Ana', 'ocena': 85},
    {'ime': 'Marko', 'ocena': 92},
    {'ime': 'Petar', 'ocena': 78}
]
najbolji_student = max(ocene, key=lambda d: d['ocena'])
print(najbolji_student)  # {'ime': 'Marko', 'ocena': 92}

# 4. Stringovi - najduži/najkraći
reči = ['pas', 'mačka', 'slon', 'miš']
najduža = max(reči, key=len)
print(najduža)  # 'mačka'

# 5. Custom logika - kompleksna key funkcija
def distance_from_zero(x):
    return abs(x)

brojevi = [-10, 5, -3, 8, -15]
najdalji = max(brojevi, key=distance_from_zero)
print(najdalji)  # -15 (najdalji od nule)
```

**Motorika**: `max()`/`min()` sa `key` je **moćniji** od običnog sortiranja jer:
- Ne sortira celu listu (efikasniji - O(N) umesto O(N log N))
- Direktno vraća traženi element
- Koristi istu lambda logiku kao `sort()`

---

## VII. LAMBDA FUNKCIJE - Anonimne, Inline Funkcije

```python
# Sintaksa
lambda parametri: izraz

# Ponašanje: Kreira anonimnu funkciju koja ODMAH vraća rezultat izraza
# Složenost: Zavisi od izraza

# Pravilo: SAMO JEDAN izraz (ne može više linija, ne može statement)

# Primeri

# 1. Osnovno
kvadrat = lambda x: x ** 2
print(kvadrat(5))  # 25

# Ekvivalentno sa def:
def kvadrat_def(x):
    return x ** 2

# 2. U sort() - sortiranje torki po drugom elementu
data = [(1, 'b'), (2, 'a'), (3, 'c')]
data.sort(key=lambda t: t[1])  # Sortira po slovu
print(data)  # [(2, 'a'), (1, 'b'), (3, 'c')]

# 3. U max()/min() - pronalaženje studenta sa najvišom ocenom
studenti = [
    {'ime': 'Ana', 'ocena': 85},
    {'ime': 'Marko', 'ocena': 92}
]
najbolji = max(studenti, key=lambda s: s['ocena'])

# 4. U map() (transformacija)
brojevi = [1, 2, 3, 4]
kvadrati = list(map(lambda x: x**2, brojevi))
# [1, 4, 9, 16]

# 5. U filter() (filtriranje)
parni = list(filter(lambda x: x % 2 == 0, brojevi))
# [2, 4]

# 6. Višeparametarska lambda
zbir = lambda x, y: x + y
print(zbir(3, 5))  # 8

# 7. Ternarni u lambda
apsolutna = lambda x: x if x >= 0 else -x
print(apsolutna(-5))  # 5
```

**Motorika**: Lambda je **inline funkcija** za jednostavne operacije. Koristi se kada:
- Funkcija je kratka (jedan izraz)
- Koristi se samo jednom (kao `key` parametar)
- Ne zahteva ime (throw-away funkcija)

#### Lambda vs List Comprehension

```python
brojevi = [1, 2, 3, 4, 5]

# Lambda + map() (funkcionalni stil)
kvadrati_map = list(map(lambda x: x**2, brojevi))

# List Comprehension (Pythonični stil) - PREFERIRANO!
kvadrati_lc = [x**2 for x in brojevi]

# Oba daju isti rezultat, ali LC je čitljiviji
```

**Pravilo**: Za transformaciju/filtriranje lista, **preferiraj List Comprehension**. Lambda koristi samo za `key` parametar u `sort()`, `max()`, `min()`.

---

## VIII. SET OPERACIJE - Matematički Skupovi

```python
# Kreiranje
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
prazan = set()  # Prazni set (ne {}, to je dict!)

# Karakteristike:
# - Samo jedinstveni elementi (automatski uklanja duplikate)
# - Nesortirano (nema garantovan redosled)
# - Brza provera pripadnosti O(1)
# - Elementi moraju biti hashable (imutabilni)

### Osnovne Operacije

```python
# 1. Dodavanje
s = {1, 2, 3}
s.add(4)  # {1, 2, 3, 4}
s.add(2)  # {1, 2, 3, 4} - duplikat ignorisan

# 2. Uklanjanje
s.remove(3)    # Briše 3, KeyError ako ne postoji
s.discard(10)  # Briše 10, NE baca error ako ne postoji
element = s.pop()  # Uklanja i vraća nasumičan element

# 3. Provera pripadnosti (O(1) - BRZO!)
if 2 in s:
    print("Postoji")
```

### Matematičke Set Operacije

```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# 1. UNIJA (|) - svi elementi iz oba seta
unija = s1 | s2
# {1, 2, 3, 4, 5, 6}
# Alternativa: s1.union(s2)

# 2. PRESEK (&) - zajednički elementi
presek = s1 & s2
# {3, 4}
# Alternativa: s1.intersection(s2)

# 3. RAZLIKA (-) - elementi u s1 koji NISU u s2
razlika = s1 - s2
# {1, 2}
# Alternativa: s1.difference(s2)

# 4. SIMETRIČNA RAZLIKA (^) - elementi koji su SAMO u jednom setu
sim_razlika = s1 ^ s2
# {1, 2, 5, 6}
# Alternativa: s1.symmetric_difference(s2)
```

**Motorika**: Setovi su **najbrži način** za:
- Uklanjanje duplikata: `unique = list(set(lista))`
- Provera pripadnosti: `if x in set_struktura` (O(1) vs O(N) za listu)
- Matematičke operacije (presek, unija)

### Praktični Primeri

```python
# Problem: Pronađi duplikate u listi
brojevi = [1, 2, 3, 2, 4, 3, 5]
svi = set()
duplikati = set()
for x in brojevi:
    if x in svi:
        duplikati.add(x)
    else:
        svi.add(x)
print(duplikati)  # {2, 3}

# Problem: Ukloni duplikate (zadržavajući tip list)
originalna = [1, 2, 2, 3, 3, 3, 4]
bez_duplikata = list(set(originalna))
# [1, 2, 3, 4] (NAPOMENA: redosled može biti drugačiji!)

# Problem: Pronađi zajedničke elemente dve liste
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
zajednicki = list(set(lista1) & set(lista2))
# [4, 5]
```

---

## IX. STRINGS - Metode za Obradu Teksta

### Osnovne Metode (Imutabilne - Vraćaju Novi String)

```python
tekst = "  Hello World  "

# 1. CASE Transformacije
print(tekst.upper())       # "  HELLO WORLD  "
print(tekst.lower())       # "  hello world  "
print(tekst.capitalize())  # "  hello world  " (samo prvi karakter)
print(tekst.title())       # "  Hello World  " (svaka reč)

# 2. Čišćenje Whitespace-a
print(tekst.strip())   # "Hello World" (briše sa obe strane)
print(tekst.lstrip())  # "Hello World  " (samo levo)
print(tekst.rstrip())  # "  Hello World" (samo desno)

# 3. Provere (Vraćaju bool)
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("   ".isspace())      # True

# 4. Zamena
print("Hello World".replace("World", "Python"))  # "Hello Python"

# 5. Deljenje (Split)
rečenica = "Ana,Marko,Petar"
imena = rečenica.split(",")  # ['Ana', 'Marko', 'Petar']

tekst = "Hello World from Python"
reči = tekst.split()  # Default delimiter: whitespace
# ['Hello', 'World', 'from', 'Python']

# 6. Spajanje (Join)
lista = ['Ana', 'Marko', 'Petar']
spojeno = ", ".join(lista)  # "Ana, Marko, Petar"

# 7. Pronalaženje
pozicija = "Hello World".find("World")  # 6 (indeks početka)
pozicija2 = "Hello World".find("Python")  # -1 (ne postoji)

# 8. Provera početka/kraja
print("test.py".endswith(".py"))    # True
print("test.py".startswith("test")) # True
```

**Motorika**: Svi string metodi vraćaju **NOVI string** (stringovi su imutabilni). Originalni string ostaje netaknut.

### f-Strings (Formatted String Literals)

```python
# Sintaksa (Python 3.6+)
f"tekst {varijabla} tekst"

# Primeri

# 1. Osnovno
ime = "Vladimir"
godine = 46
print(f"Ja sam {ime} i imam {godine} godina.")
# "Ja sam Vladimir i imam 46 godina."

# 2. Izrazi unutar {}
x = 10
print(f"Duplo od {x} je {x * 2}")
# "Duplo od 10 je 20"

# 3. Formatiranje brojeva
pi = 3.14159265
print(f"Pi je približno {pi:.2f}")  # "Pi je približno 3.14"

cena = 1234.5
print(f"Cena: {cena:,.2f} RSD")  # "Cena: 1,234.50 RSD"

# 4. Poravnanje
ime = "Ana"
print(f"|{ime:>10}|")  # "|       Ana|" (desno)
print(f"|{ime:<10}|")  # "|Ana       |" (levo)
print(f"|{ime:^10}|")  # "|   Ana    |" (centar)

# 5. Sa metodama
ime = "vladimir"
print(f"Zdravo, {ime.capitalize()}!")  # "Zdravo, Vladimir!"

# 6. Sa dictionary
student = {'ime': 'Ana', 'ocena': 85}
print(f"{student['ime']} ima ocenu {student['ocena']}")
# "Ana ima ocenu 85"
```

**Motorika**: f-strings su **najbrži i najčitljiviji** način za formatiranje stringova u Pythonu. Preferiraj ih umesto `%` ili `.format()`.

---

## X. RANGE - Generator Sekvenci

```python
# Sintaksa
range(stop)           # Od 0 do stop-1
range(start, stop)    # Od start do stop-1
range(start, stop, step)  # Od start do stop-1, korak step

# Karakteristike:
# - Vraća range objekat (lazy - ne kreira listu odmah)
# - Memorijski efikasan za velike opsege
# - Imutabilan

# Primeri

# 1. Osnovno (0 do n-1)
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4

# 2. Sa start i stop
for i in range(2, 7):
    print(i)
# 2, 3, 4, 5, 6

# 3. Sa step (korak)
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8

# 4. Negativan step (opadajuće)
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

# 5. Konvertovanje u listu (retko potrebno)
lista = list(range(5))  # [0, 1, 2, 3, 4]

# 6. U List Comprehension
kvadrati = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

**Motorika**: `range()` je **standard** za C-stil petlje. Ali, kada god je moguće, preferiraj direktnu iteraciju preko liste (`for x in lista`) ili `enumerate()`.

---

## XI. ANY i ALL - Logički Agregatori

```python
# Sintaksa
any(iterable)  # True ako JE BAR JEDAN element True
all(iterable)  # True ako SU SVI elementi True

# Ponašanje sa praznim iterable:
# any([]) → False
# all([]) → True (vakuumska istina)

# Primeri

# 1. any() - Provera da li postoji bar jedan True
brojevi = [1, 2, 3, 4, 5]
ima_paran = any(x % 2 == 0 for x in brojevi)
print(ima_paran)  # True (2 i 4 su parni)

# 2. all() - Provera da li su svi True
svi_pozitivni = all(x > 0 for x in brojevi)
print(svi_pozitivni)  # True

# 3. Sa listom boolean vrednosti
rezultati = [True, False, True]
print(any(rezultati))  # True (bar jedan je True)
print(all(rezultati))  # False (nisu svi True)

# 4. Provera da li string sadrži cifru
tekst = "abc123"
ima_cifru = any(c.isdigit() for c in tekst)
print(ima_cifru)  # True

# 5. Validacija - svi elementi ispunjavaju uslov
ocene = [85, 90, 78, 92]
svi_polozili = all(o >= 50 for o in ocene)
print(svi_polozili)  # True
```

**Motorika**: `any()` i `all()` su **ekstremno korisni** za validaciju i provere. Zamenjuju kompleksne petlje sa flagovima.

---

## XII. SORTED() - Ne-Destruktivno Sortiranje

```python
# Sintaksa
nova_lista = sorted(iterable, key=funkcija, reverse=False)

# Razlika list.sort() vs sorted():
# - list.sort() → sortira IN-PLACE, vraća None
# - sorted() → vraća NOVU sortiranu listu, originalna netaknuta

# Primeri

# 1. Osnovno
brojevi = [3, 1, 4, 1, 5]
sortirano = sorted(brojevi)
print(sortirano)  # [1, 1, 3, 4, 5]
print(brojevi)    # [3, 1, 4, 1, 5] - ORIGINALNA NETAKNUTA!

# 2. Opadajuće
opadajuce = sorted(brojevi, reverse=True)
# [5, 4, 3, 1, 1]

# 3. Sa key funkcijom (custom sortiranje)
reči = ['banana', 'pas', 'slon', 'mačka']
po_dužini = sorted(reči, key=len)
# ['pas', 'slon', 'mačka', 'banana']

# 4. Sortiranje torki
studenti = [
    ('Ana', 85),
    ('Marko', 92),
    ('Petar', 78)
]
po_oceni = sorted(studenti, key=lambda s: s[1], reverse=True)
# [('Marko', 92), ('Ana', 85), ('Petar', 78)]

# 5. Sortiranje rečnika (po vrednosti)
ocene = {'Ana': 85, 'Marko': 92, 'Petar': 78}
sortirano = sorted(ocene.items(), key=lambda item: item[1], reverse=True)
# [('Marko', 92), ('Ana', 85), ('Petar', 78)]

# 6. Sortiranje stringa (vraća listu karaktera)
s = "dcba"
sortirano = sorted(s)
# ['a', 'b', 'c', 'd']
# Za string: ''.join(sorted(s)) → "abcd"
```

**Motorika**: Koristi `sorted()` kada:
- Ne želiš da menjaš originalnu listu
- Sortirajuš strukturu koja nije lista (set, dict keys, string)

Koristi `.sort()` kada:
- Siguran si da želiš da menjaš listu in-place
- Efikasnost memorije je kritična (ne kreira kopiju)

---

## XIII. GENERATORS - Lazy Evaluation

```python
# Generator Expression (sintaksa slična LC, ali sa ())
gen = (x**2 for x in range(1000000))

# Karakteristike:
# - Kreira elemente "na zahtev" (lazy)
# - Memorijski efikasan (ne čuva sve elemente)
# - Može se iterirati samo jednom
# - Ne podržava indeksiranje

# Razlika sa List Comprehension:
lista = [x**2 for x in range(1000000)]  # Odmah kreira 1M elemenata
gen = (x**2 for x in range(1000000))    # Čeka iteraciju

# Primeri

# 1. Osnovna iteracija
gen = (x * 2 for x in range(5))
for vrednost in gen:
    print(vrednost)
# 0, 2, 4, 6, 8

# 2. Konverzija u listu (gubi lazy prednost)
gen = (x**2 for x in range(10))
lista = list(gen)  # [0, 1, 4, 9, 16, ...]

# 3. U sum(), max(), min() (efikasno!)
zbir = sum(x**2 for x in range(1000))  # Ne kreira listu!

# 4. Generator funkcija (sa yield)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for broj in fibonacci(10):
    print(broj)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

**Motorika**: Generatori su **ključni za memorijsku efikasnost** kada radiš sa velikim podacima. Ali za male liste, List Comprehension je jednostavniji.

---

## XIV. COLLECTIONS MODUL - Specijalizovane Strukture

### 1. Counter - Brojač Frekvencija

```python
from collections import Counter

# Automatski broji frekvencije
tekst = "hello world"
brojač = Counter(tekst)
print(brojač)
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Najčešći elementi
print(brojač.most_common(2))  # [('l', 3), ('o', 2)]

# Operacije
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'b', 'd'])
print(c1 + c2)  # Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
```

### 2. defaultdict - Rečnik sa Default Vrednostima

```python
from collections import defaultdict

# Klasični problem: brojač bez get()
counter = defaultdict(int)  # Default je 0
for slovo in "hello":
    counter[slovo] += 1
# Nema potrebe za: counter[slovo] = counter.get(slovo, 0) + 1

# Lista kao default
groups = defaultdict(list)
for ime, ocena in [('Ana', 85), ('Marko', 90), ('Ana', 92)]:
    groups[ime].append(ocena)
# {'Ana': [85, 92], 'Marko': [90]}
```

### 3. deque - Dvosmerna Reda (Queue)

```python
from collections import deque

# Efikasne operacije na OBA kraja (O(1))
q = deque([1, 2, 3])
q.append(4)      # Dodaj na desni kraj: [1, 2, 3, 4]
q.appendleft(0)  # Dodaj na levi kraj: [0, 1, 2, 3, 4]
q.pop()          # Ukloni sa desnog kraja: 4
q.popleft()      # Ukloni sa levog kraja: 0

# Poređenje sa listom:
# lista.pop(0) → O(N) SPORO!
# deque.popleft() → O(1) BRZO!
```

**Motorika**: `collections` modul pruža **specijalizovane strukture** koje rešavaju specifične probleme efikasnije od osnovnih tipova.

---

## XV. ERROR HANDLING - Try/Except Blokovi

```python
# Sintaksa
try:
    # Kod koji može baciti grešku
    rezultat = 10 / 0
except ZeroDivisionError:
    # Obrada greške
    print("Deljenje nulom!")
except ValueError as e:
    # Hvatanje greške sa detaljima
    print(f"Greška: {e}")
else:
    # Izvršava se ako NEMA greške
    print("Uspešno!")
finally:
    # Izvršava se UVEK (čišćenje resursa)
    print("Završeno.")

# Primeri

# 1. Bezbedna konverzija
def bezbedni_int(s):
    try:
        return int(s)
    except ValueError:
        return None

print(bezbedni_int("123"))   # 123
print(bezbedni_int("abc"))   # None

# 2. File operacije (sa finally)
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Fajl ne postoji")
finally:
    f.close()  # UVEK zatvori fajl

# 3. Bolje: with statement (automatski close)
try:
    with open("data.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Fajl ne postoji")
```

**Motorika**: `try/except` je **obavezan** za robusne aplikacije. Koristi ga za:
- User input validaciju
- File/network operacije
- External API pozive
- Konverzije tipova

---

## XVI. NAPREDNI PATTERNS - Idiomi

### 1. Swapping Vrednosti (Pythonic Way)

```python
# C-stil (sa temp varijablom)
temp = a
a = b
b = temp

# Python idiom (tuple unpacking)
a, b = b, a
```

### 2. Unpacking (Raspakivanje)

```python
# Lista/torka
x, y, z = [1, 2, 3]
# x=1, y=2, z=3

# Sa * operatorom (rest)
prvi, *ostali, poslednji = [1, 2, 3, 4, 5]
# prvi=1, ostali=[2, 3, 4], poslednji=5

# Funkcije (multiple return)
def min_max(lista):
    return min(lista), max(lista)

najmanji, najveći = min_max([1, 5, 3, 9, 2])
```

### 3. Conditional Expression in Assignment

```python
# Dobar pattern za default vrednosti
ime = input("Ime: ") or "Anonimus"
# Ako je input prazan string, koristi "Anonimus"

# Sa ternary
status = "aktivan" if korisnik.login_at else "neaktivan"
```

### 4. Chaining Comparisons

```python
# Python dozvoljava
if 0 < x < 10:
    print("Jedna cifra")

# Umesto
if x > 0 and x < 10:
    print("Jedna cifra")
```

---

## XVII. ZAKLJUČAK - Tvoja Mantra Motorike

```
1. LISTA → Mutabilna sekvenca, koristi append/pop/sort
2. DICT → Hash tabela, koristi get() i items()
3. SET → Jedinstveni elementi, matematičke operacije
4. LC → Transformacija/filtriranje lista
5. ENUMERATE → Indeks + vrednost u petlji
6. ZIP → Sinhronizacija više lista
7. LAMBDA → Inline funkcije za key parametar
8. ANY/ALL → Logička agregacija
9. TRY/EXCEPT → Robusnost
10. F-STRINGS → Formatiranje
```

---

**Finalna Napomena**: Ova dokumentacija je **referenca**, ne tutorial. Svaki koncept si već vežbao u drill-ovima. Sada imaš centralizovano mesto za osvežavanje memorije.

**Sledeći Korak**: Uvezi ovu dokumentaciju u NotebookML i kreiraj AI asistenta koji će ti postavljati kviz pitanja o ovim konceptima.

---

**Kraj Dokumentacije**  
**Datum poslednje izmene**: 25. oktobar 2025.