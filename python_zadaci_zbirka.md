# Python - Zbirka Zadataka za Vežbanje

> **Napomena:** Ova zbirka sadrži 73 zadatka organizovana po temama, sa primerima ulaza/izlaza i diskretnim hintovima koji usmeravaju razmišljanje bez otkrivanja rešenja.

---
## **Zadatak 1: Kvadriranje parnih brojeva**

Napiši funkciju `square_even_numbers` koja prihvata listu brojeva. Koristeći list comprehension, funkcija treba da isfiltrira samo parne brojeve iz ulazne liste i vrati novu listu koja sadrži njihove kvadrate.

* **Primer ulaza:** `[1, 2, 3, 4, 5, 6, 7]`
* **Očekivani izlaz:** `[4, 16, 36]`

---

## **Zadatak 2: Sortiranje jedinstvenih reči po dužini**

Napiši funkciju `sort_unique_by_length` koja prihvata listu reči. Funkcija treba prvo da ukloni sve duplikate, a zatim da sortira jedinstvene reči po njihovoj dužini, od najkraće do najduže.

* **Primer ulaza:** `['apple', 'banana', 'cucumber', 'apple', 'pear']`
* **Očekivani izlaz:** `['pear', 'apple', 'banana', 'cucumber']`

---

## **Zadatak 3: Inverzija brojeva u stringu**

Napiši funkciju `invert_and_keep_string` koja prihvata listu stringova, gde svaki string predstavlja ceo broj. Koristeći list comprehension, funkcija treba da promeni znak svakom broju (pozitivan postaje negativan i obrnuto) i vrati novu listu sa promenjenim vrednostima, koje takođe moraju biti tipa string.

* **Primer ulaza:** `["10", "-5", "2", "-1"]`
* **Očekivani izlaz:** `['-10', '5', '-2', '1']`

---

## **Zadatak 4: Pronalaženje najjeftinijeg proizvoda**

Napiši funkciju `find_cheapest_product` koja prihvata listu torki (tuples). Svaka torka se sastoji od naziva proizvoda (string) i njegove cene (broj). Koristeći `min()` funkciju i `lambda` izraz, pronađi i vrati kompletnu torku koja predstavlja najjeftiniji proizvod.

* **Primer ulaza:** `[('Laptop', 1200), ('Monitor', 300), ('Mouse', 15), ('Keyboard', 50)]`
* **Očekivani izlaz:** `('Mouse', 15)`

---

## **Zadatak 5: Mapiranje liste u rečnik sa indeksima**

Napiši funkciju `index_to_dictionary` koja prihvata listu stavki. Koristeći petlju i `enumerate`, kreiraj i vrati rečnik (dictionary) gde su ključevi indeksi elemenata iz ulazne liste, a vrednosti su sami elementi.

* **Primer ulaza:** `['milk', 'bread', 'eggs']`
* **Očekivani izlaz:** `{0: 'milk', 1: 'bread', 2: 'eggs'}`

---

## **Zadatak 6: Filtriranje ocena**

Napiši funkciju `filter_high_grades` koja prihvata dve liste iste dužine: listu sa imenima učenika i listu sa njihovim ocenama. Koristeći `zip` funkciju i list comprehension, spoji svakog učenika sa njegovom ocenom i vrati novu listu formatiranih stringova, ali samo za one učenike čija je ocena veća od 80.

* **Primer ulaza:** `names=['Pera', 'Mika', 'Laza', 'Ana']`, `grades=[95, 78, 88, 65]`
* **Očekivani izlaz:** `['Pera has 95', 'Laza has 88']`

---

## **Zadatak 7: Uslovna zamena vrednosti ("Fizz" zadatak)**

Napiši funkciju `fizz_swap` koja prihvata listu brojeva. Koristeći list comprehension i ternarni operator, funkcija treba da vrati novu listu u kojoj je svaki broj deljiv sa 3 zamenjen stringom `"Fizz"`. Ostali brojevi treba da ostanu nepromenjeni.

* **Primer ulaza:** `[1, 3, 5, 6, 8, 9, 10]`
* **Očekivani izlaz:** `[1, 'Fizz', 5, 'Fizz', 8, 'Fizz', 10]`

---

## **Zadatak 8: Povećanje cena za skuplje proizvode**

Napiši funkciju `price_markup` koja prihvata listu cena. Koristeći list comprehension, funkcija treba da filtrira samo one cene koje su veće od 100 i da na njih primeni povećanje od 10%. Funkcija treba da vrati novu listu koja sadrži samo preračunate, uvećane cene.

* **Primer ulaza:** `[50, 120, 99, 200, 10]`
* **Očekivani izlaz:** `[132.0, 220.0]`

---

## **Zadatak 9: Uslovno spajanje rečnika**

Napiši funkciju `conditional_merge` koja prihvata dva rečnika, `d1` i `d2`. Funkcija treba da kreira novi rečnik na sledeći način:
1. Prvo, iz rečnika `d1` filtriraj i zadrži samo one parove ključ-vrednost gde je vrednost veća od 50.
2. Zatim, spoji taj filtrirani rečnik sa celokupnim rečnikom `d2`.

Ako neki ključ postoji u oba rečnika (u filtriranom `d1` i u `d2`), vrednost iz `d2` ima prednost.

* **Ulaz 1:** `d1 = {'A': 90, 'B': 40, 'C': 70}`
* **Ulaz 2:** `d2 = {'B': 5, 'D': 100, 'A': 10}`
* **Očekivani izlaz:** `{'C': 70, 'B': 5, 'D': 100, 'A': 10}`

---

## **Zadatak 10: Agregacija (sabiranje) poena**

Napiši funkciju `aggregate_points` koja prihvata listu torki. Svaka torka sadrži ime studenta i broj poena koje je osvojio. Funkcija treba da prođe kroz listu i sabere sve poene za svakog studenta, vraćajući rečnik gde su ključevi imena studenata, a vrednosti ukupan zbir njihovih poena.

* **Primer ulaza:** `[('Pera', 10), ('Mika', 5), ('Pera', 20), ('Laza', 15)]`
* **Očekivani izlaz:** `{'Pera': 30, 'Mika': 5, 'Laza': 15}`

---

## **Zadatak 11: Kvadriranje vrednosti na parnim indeksima**

Napiši funkciju `square_at_even_indices` koja prihvata listu brojeva. Koristeći `enumerate` i list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih brojeva koji se u originalnoj listi nalaze na parnim indeksima (0, 2, 4, itd.).

* **Primer ulaza:** `[1, 2, 3, 4, 5, 6]`
* **Očekivani izlaz:** `[1, 9, 25]`

---

## **Zadatak 12: Sortiranje po ugnežđenim vrednostima**

Napiši funkciju `sort_by_nested_tuple` koja prima listu torki. Svaka torka sadrži ime osobe i drugu (ugnežđenu) torku sa godinama i visinom te osobe `('Ime', (godine, visina))`. Sortiraj listu po sledećim kriterijumima:
1. Primarno po godinama, rastuće.
2. Sekundarno po visini, opadajuće (ako su godine iste).

* **Primer ulaza:** `[('Ana', (25, 170)), ('Pera', (30, 180)), ('Mika', (25, 175))]`
* **Očekivani izlaz:** `[('Mika', (25, 175)), ('Ana', (25, 170)), ('Pera', (30, 180))]`

---

## **Zadatak 13: Zamena malih decimalnih brojeva**

Napiši funkciju `filter_small_floats` koja prihvata listu decimalnih brojeva. Koristeći list comprehension i ternarni operator, vrati novu listu gde je svaki broj veći od 10.0 zadržan, dok je svaki broj manji ili jednak 10.0 zamenjen sa `0.0`.

* **Primer ulaza:** `[15.5, 9.2, 11.0, 5.0, 10.0]`
* **Očekivani izlaz:** `[15.5, 0.0, 11.0, 0.0, 0.0]`

---

## **Zadatak 14: Filtriranje reči po dužini i početnom slovu**

Napiši funkciju `filter_by_length_and_start` koja prima listu reči. Koristeći list comprehension, vrati novu listu koja sadrži samo one reči koje istovremeno ispunjavaju oba uslova: duže su od 5 slova **I** počinju velikim slovom 'C'.

* **Primer ulaza:** `['apple', 'Cucumber', 'cat', 'Computer', 'caravan']`
* **Očekivani izlaz:** `['Cucumber', 'Computer', 'caravan']`

---

## **Zadatak 15: Inverzija vrednosti u rečniku**

Napiši funkciju `invert_dictionary_values` koja prihvata rečnik sa numeričkim vrednostima. Koristeći dictionary comprehension, kreiraj i vrati novi rečnik gde su ključevi isti kao u ulaznom rečniku, ali su sve vrednosti pomnožene sa -1.

* **Primer ulaza:** `{'prihod': 1000, 'trosak': 500, 'dobit': 500}`
* **Očekivani izlaz:** `{'prihod': -1000, 'trosak': -500, 'dobit': -500}`

---

## **Zadatak 16: Kreiranje rečnika sa cenom kao ključem**

Napiši funkciju `price_as_key_if_high` koja prima dve liste: listu imena i listu cena. Koristeći `zip` i dictionary comprehension, kreiraj rečnik gde je cena ključ, a ime vrednost, ali samo za one parove gde je cena veća od 100.

* **Ulaz (Imena):** `['A', 'B', 'C', 'D']`
* **Ulaz (Cene):** `[50, 120, 80, 250]`
* **Očekivani izlaz:** `{120: 'B', 250: 'D'}`

---

## **Zadatak 17: Sortiranje proizvoda po zalihama i ceni**

Napiši funkciju `sort_by_stock_and_price` koja prihvata listu torki. Svaka torka predstavlja proizvod sa formatom `(ime, cena, zaliha)`. Sortiraj listu po sledećim kriterijumima:
1. Primarno po broju zaliha, opadajuće.
2. Sekundarno po ceni, rastuće (ako su zalihe iste).

* **Primer ulaza:** `[('Laptop', 1200, 5), ('Monitor', 300, 10), ('Miš', 15, 5)]`
* **Očekivani izlaz:** `[('Monitor', 300, 10), ('Miš', 15, 5), ('Laptop', 1200, 5)]`

---

## **Zadatak 18: Filtriranje ocena po indeksu i vrednosti**

Napiši funkciju `filter_by_index_and_value` koja prihvata listu ocena. Koristeći `enumerate` i list comprehension, vrati novu listu koja sadrži samo one ocene koje zadovoljavaju oba uslova: nalaze se na indeksu deljivom sa 3 **I** njihova vrednost je veća od 70.

* **Primer ulaza:** `[80, 50, 60, 90, 70, 40, 85]`
* **Očekivani izlaz:** `[80, 90]`

---

## **Zadatak 19: Kvadriranje samo celih brojeva iz mešovite liste**

Napiši funkciju `square_only_integers` koja prihvata listu sa mešovitim tipovima podataka (brojevi, stringovi...). Koristeći list comprehension, funkcija treba da vrati novu listu koja sadrži kvadrate samo onih elemenata koji su celi brojevi (tip `int`).

* **Primer ulaza:** `[1, 5.5, 'a', 4, 9, 'b']`
* **Očekivani izlaz:** `[1, 16, 81]`

---

## **Zadatak 20: Kreiranje rečnika iz torki pod uslovom**

Napiši funkciju `dict_from_tuple_if_high` koja prima listu torki u formatu `(ime, bodovi)`. Koristeći dictionary comprehension, kreiraj i vrati rečnik, ali uključi samo one parove iz liste čija je vrednost bodova veća od 10.

* **Primer ulaza:** `[('A', 15), ('B', 5), ('C', 20), ('D', 8)]`
* **Očekivani izlaz:** `{'A': 15, 'C': 20}`

---

## **Zadatak 21: Presek tri liste**

Napiši funkciju `intersection_of_three` koja prihvata tri liste. Funkcija treba da pronađe i vrati skup (set) elemenata koji se nalaze u sve tri ulazne liste istovremeno.

* **Ulaz A:** `[1, 2, 3, 4]`
* **Ulaz B:** `[3, 4, 5, 6]`
* **Ulaz C:** `[4, 6, 7, 3]`
* **Očekivani izlaz:** `{3, 4}`

---

## **Zadatak 22: Sortiranje rečnika po vrednosti opadajuće**

Napiši funkciju `sort_dict_by_value_desc` koja prihvata rečnik (npr. ime: poeni). Funkcija treba da vrati listu torki `(ključ, vrednost)` sortiranu opadajuće prema vrednosti.

* **Primer ulaza:** `{'Pera': 30, 'Mika': 5, 'Laza': 15}`
* **Očekivani izlaz:** `[('Pera', 30), ('Laza', 15), ('Mika', 5)]`

---

## **Zadatak 23: Lista neparnih brojeva**

Napiši funkciju `odd_numbers_up_to_ten` koja ne prima argumente. Koristeći list comprehension i `range`, funkcija treba da kreira i vrati listu koja sadrži sve neparne brojeve od 1 do 10.

* **Očekivani izlaz:** `[1, 3, 5, 7, 9]`

---

## **Zadatak 24: Formatiranje numeričkih podataka iz liste stringova**

Napiši funkciju `format_numeric_data` koja prihvata listu stringova. Funkcija treba da vrati novu listu koja sadrži samo one elemente koji se mogu pretvoriti u broj. Ti elementi treba da budu pretvoreni u decimalni broj (float) i zaokruženi na dve decimale.

* **Primer ulaza:** `['10.5', 'error', '20.334', '15', 'fail']`
* **Očekivani izlaz:** `[10.5, 20.33, 15.0]`

---

## **Zadatak 25: Zbir kvadrata parova elemenata**

Napiši funkciju `sum_of_squares_pairs` koja prihvata dve liste brojeva jednakih dužina. Koristeći `zip` i list comprehension, funkcija treba da vrati novu listu gde je svaki element zbir kvadrata odgovarajućih elemenata iz ulaznih listi.

* **Ulaz A:** `[1, 2, 3]`
* **Ulaz B:** `[4, 5, 6]`
* **Očekivani izlaz:** `[17, 29, 45]` (Jer je 1²+4²=17, 2²+5²=29, 3²+6²=45)

---

## **Zadatak 26: Uslovno preimenovanje ključeva u rečniku**

Napiši funkciju `conditional_key_rename` koja prihvata rečnik (proizvod: cena). Kreiraj novi rečnik gde, ako je cena proizvoda veća od 100, ključu se dodaje prefiks `"SKU_"`. U suprotnom, ključ ostaje isti.

* **Primer ulaza:** `{'milk': 50, 'bread': 120, 'cheese': 80}`
* **Očekivani izlaz:** `{'milk': 50, 'SKU_bread': 120, 'cheese': 80}`

---

## **Zadatak 27: Sortiranje reči po dužini i abecedi**

Napiši funkciju `sort_by_length_then_alphabet_desc` koja prima listu stringova. Sortiraj listu po dva kriterijuma:
1. Primarno po dužini reči, opadajuće (od najduže ka najkraćoj).
2. Sekundarno po abecednom redu, takođe opadajuće (od Z ka A).

* **Primer ulaza:** `['apple', 'pie', 'banana', 'cat']`
* **Očekivani izlaz:** `['banana', 'apple', 'pie', 'cat']`

---


## 📝 Osnove i rad sa stringovima

### **Zadatak 28: Brojanje samoglasnika**
Napiši funkciju koja prihvata string i vraća ukupan broj samoglasnika (a, e, i, o, u) u njemu, ne praveći razliku između velikih i malih slova.

- **Primer ulaza:** `"Programiranje u Pythonu"`
- **Očekivani izlaz:** `7`
- **Hint:** *Možeš proći kroz string i proveravati da li se svaki karakter nalazi u setu samoglasnika. Ne zaboravi `lower()`.*

---

### **Zadatak 29: Provera palindroma**
Napiši funkciju koja proverava da li je data reč palindrom (čita se isto s leva na desno i s desna na levo).

- **Primer ulaza:** `"anavolimilovana"`
- **Očekivani izlaz:** `True`
- **Hint:** *String slicing `[::-1]` je veoma moćan alat za obrtanje.*

---

### **Zadatak 30: Obrtanje redosleda reči u rečenici**
Napiši funkciju koja prihvata rečenicu i vraća novu rečenicu sa obrnutim redosledom reči.

- **Primer ulaza:** `"Python je zaista moćan jezik"`
- **Očekivani izlaz:** `"jezik moćan zaista je Python"`
- **Hint:** *Razmisli o metodama `split()` i `join()` za stringove.*

---

### **Zadatak 31: Zamena karaktera u stringu**
Napiši funkciju koja prihvata tri argumenta: originalni string, karakter koji treba zameniti i karakter kojim se zamenjuje. Funkcija treba da vrati novi string sa izvršenom zamenom.

- **Primer ulaza:** `("banana", "a", "o")`
- **Očekivani izlaz:** `"bonono"`

---

### **Zadatak 32: Ekstrakcija brojeva iz stringa**
Napiši funkciju koja iz datog stringa izdvaja sve cifre i vraća ih kao listu celih brojeva.

- **Primer ulaza:** `"Artikl A123 košta 45.99 dinara"`
- **Očekivani izlaz:** `[1, 2, 3, 4, 5, 9, 9]`
- **Hint:** *Metoda `isdigit()` može biti korisna za proveru da li je karakter cifra.*

---

## 📋 Rad sa listama

### **Zadatak 33: Uklanjanje duplikata iz liste (bez `set`)**
Napiši funkciju koja uklanja sve duplikate iz liste, ali zadržava originalni redosled elemenata. Ne koristi `set` za rešavanje.

- **Primer ulaza:** `[1, 2, 5, 2, 3, 5, 1, 4]`
- **Očekivani izlaz:** `[1, 2, 5, 3, 4]`
- **Hint:** *Kreiraj praznu listu i dodaj elemente iz originalne samo ako se već ne nalaze u novoj listi.*

---

### **Zadatak 34: Spajanje i sortiranje dve liste**
Napiši funkciju koja spaja dve liste u jednu i zatim sortira tu novu listu u rastućem redosledu.

- **Primer ulaza:** `([3, 1, 5], [2, 4])`
- **Očekivani izlaz:** `[1, 2, 3, 4, 5]`

---

### **Zadatak 35: Rotacija liste ulevo**
Napiši funkciju koja rotira (pomera) elemente liste za `N` mesta ulevo.

- **Primer ulaza:** `([1, 2, 3, 4, 5, 6], 2)`
- **Očekivani izlaz:** `[3, 4, 5, 6, 1, 2]`
- **Hint:** *Slicing može da podeli listu na dva dela koja zatim možeš ponovo spojiti u drugačijem redosledu.*

---

### **Zadatak 36: Pronalaženje drugog najvećeg broja**
Napiši funkciju koja pronalazi i vraća drugi po veličini broj u listi brojeva.

- **Primer ulaza:** `[10, 45, 99, 4, 20]`
- **Očekivani izlaz:** `45`
- **Hint:** *Jednostavan način je da sortiraš listu. Pazi na slučajeve sa duplikatima ili ako lista ima manje od dva elementa.*

---

### **Zadatak 37: "Spljoštavanje" ugnežđene liste**
Napiši funkciju koja listu listi (ugnežđenu listu) pretvara u jednu jedinstvenu listu.

- **Primer ulaza:** `[[1, 2], [3, 4, 5], [6]]`
- **Očekivani izlaz:** `[1, 2, 3, 4, 5, 6]`
- **Hint:** *Možeš koristiti ugnežđenu petlju (nested loop) ili list comprehension.*

---

### **Zadatak 38: Provera da li je lista sortirana**
Napiši funkciju koja proverava da li je lista brojeva sortirana u rastućem redosledu i vraća `True` ili `False`.

- **Primer ulaza:** `[1, 3, 5, 8, 12]`
- **Očekivani izlaz:** `True`

---

### **Zadatak 39: Lista kvadrata neparnih brojeva (List Comprehension)**
Koristeći list comprehension, kreiraj listu koja sadrži kvadrate neparnih brojeva od 1 do 10.

- **Očekivani izlaz:** `[1, 9, 25, 49, 81]`

---

### **Zadatak 40: Filtriranje reči po dužini (List Comprehension)**
Data je lista reči. Koristeći list comprehension, vrati novu listu koja sadrži samo reči kraće od 5 karaktera.

- **Primer ulaza:** `['jabuka', 'auto', 'kuća', 'programiranje', 'most']`
- **Očekivani izlaz:** `['auto', 'kuća', 'most']`

---

### **Zadatak 41: Kumulativni zbir liste**
Napiši funkciju koja kao ulaz prima listu brojeva i vraća novu listu kumulativnih zbirova.

- **Primer ulaza:** `[1, 2, 3, 4]`
- **Očekivani izlaz:** `[1, 3, 6, 10]` (jer je 1, 1+2, 1+2+3, 1+2+3+4)
- **Hint:** *Trebaće ti promenljiva koja pamti tekući zbir dok prolaziš kroz listu.*

---

### **Zadatak 42: Premeštanje nula na kraj liste**
Napiši funkciju koja sve nule iz liste premešta na kraj, zadržavajući relativni redosled ostalih elemenata.

- **Primer ulaza:** `[0, 1, 9, 0, 3, 0, 12]`
- **Očekivani izlaz:** `[1, 9, 3, 12, 0, 0, 0]`
- **Hint:** *Najjednostavnije je da kreiraš novu listu dodajući sve elemente koji nisu nula, a zatim na kraj dodaš potreban broj nula.*

---

## 📚 Rad sa rečnicima (Dictionaries)

### **Zadatak 43: Inverzija rečnika**
Napiši funkciju koja zamenjuje mesta ključevima i vrednostima u rečniku. Pretpostavi da su sve vrednosti jedinstvene.

- **Primer ulaza:** `{'ime': 'Pera', 'grad': 'Beograd'}`
- **Očekivani izlaz:** `{'Pera': 'ime', 'Beograd': 'grad'}`

---

### **Zadatak 44: Brojanje frekvencije reči u tekstu**
Napiši funkciju koja prihvata tekst (string) i vraća rečnik gde su ključevi reči iz teksta, a vrednosti broj njihovih pojavljivanja.

- **Primer ulaza:** `"pas mačka pas ptica mačka pas"`
- **Očekivani izlaz:** `{'pas': 3, 'mačka': 2, 'ptica': 1}`
- **Hint:** *Rečnik je idealan za ovo. Metoda `dict.get(kljuc, 0)` može biti veoma korisna za elegantno brojanje.*

---

### **Zadatak 45: Pronalaženje ključa sa najvećom vrednošću**
Napiši funkciju koja vraća ključ koji ima najveću numeričku vrednost u rečniku.

- **Primer ulaza:** `{'fizika': 88, 'matematika': 95, 'hemija': 91}`
- **Očekivani izlaz:** `'matematika'`
- **Hint:** *Istraži kako se koristi `key` argument u `max()` funkciji.*

---

### **Zadatak 46: Rečnik kvadrata (Dictionary Comprehension)**
Koristeći dictionary comprehension, kreiraj rečnik gde su ključevi brojevi od 1 do 5, a vrednosti njihovi kvadrati.

- **Očekivani izlaz:** `{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}`

---

### **Zadatak 47: Filtriranje rečnika po vrednosti (Dictionary Comprehension)**
Dat je rečnik (proizvod: cena). Vrati novi rečnik koji sadrži samo proizvode čija je cena veća od 100.

- **Primer ulaza:** `{'Laptop': 1200, 'Miš': 50, 'Tastatura': 150}`
- **Očekivani izlaz:** `{'Laptop': 1200, 'Tastatura': 150}`

---

### **Zadatak 48: Grupisanje elemenata po nekoj osobini**
Data je lista reči. Grupiši ih u rečnik gde je ključ dužina reči, a vrednost lista svih reči te dužine.

- **Primer ulaza:** `['jedan', 'dva', 'tri', 'četiri', 'pet']`
- **Očekivani izlaz:** `{5: ['jedan', 'četiri'], 3: ['dva', 'tri', 'pet']}`
- **Hint:** *Prolazi kroz listu reči. Za svaku reč, proveri da li ključ (njena dužina) postoji u rečniku. Ako ne, kreiraj ga sa listom, a zatim dodaj reč.*

---

### **Zadatak 49: Ažuriranje vrednosti u rečniku**
Napiši funkciju koja prima rečnik i listu ključeva. Za svaki ključ iz liste, udvostručи njegovu vrednost u rečniku.

- **Primer ulaza:** `({'a': 1, 'b': 2, 'c': 3}, ['a', 'c'])`
- **Očekivani izlaz:** `{'a': 2, 'b': 2, 'c': 6}`

---

### **Zadatak 50: Rečnik parnih i neparnih brojeva**
Napiši funkciju koja razvrstava brojeve iz liste u rečnik sa dva ključa: `'parni'` i `'neparni'`.

- **Primer ulaza:** `[1, 2, 3, 4, 5, 6]`
- **Očekivani izlaz:** `{'parni': [2, 4, 6], 'neparni': [1, 3, 5]}`

---

## 🔢 Rad sa setovima i torkama (Sets & Tuples)

### **Zadatak 51: Unija i presek**
Napiši funkciju koja za dve liste vraća torku koja sadrži dva seta: prvi je unija, a drugi presek elemenata.

- **Primer ulaza:** `([1, 2, 3], [3, 4, 5])`
- **Očekivani izlaz:** `({1, 2, 3, 4, 5}, {3})`

---

### **Zadatak 52: Simetrična razlika**
Napiši funkciju koja vraća elemente koji se nalaze u jednoj ili drugoj listi, ali ne i u obe (simetrična razlika).

- **Primer ulaza:** `([1, 2, 3, 4], [3, 4, 5, 6])`
- **Očekivani izlaz:** `{1, 2, 5, 6}`
- **Hint:** *Setovi imaju ugrađen operator `^` ili metodu za ovo.*

---

### **Zadatak 53: Provera da li je skup podskup**
Napiši funkciju koja proverava da li je prvi set (kreiran od prve liste) podskup drugog seta (kreiranog od druge liste).

- **Primer ulaza:** `([1, 2], [1, 2, 3])`
- **Očekivani izlaz:** `True`

---

### **Zadatak 54: Sortiranje liste torki po drugom elementu**
Data je lista torki `(ime, godine)`. Sortiraj je po godinama u rastućem redosledu.

- **Primer ulaza:** `[('Pera', 30), ('Ana', 25), ('Mika', 35)]`
- **Očekivani izlaz:** `[('Ana', 25), ('Pera', 30), ('Mika', 35)]`
- **Hint:** *Koristi `sorted()` funkciju sa `lambda` izrazom kao ključem.*

---

### **Zadatak 55: Konverzija liste torki u rečnik**
Napiši funkciju koja pretvara listu torki (parova ključ-vrednost) u rečnik.

- **Primer ulaza:** `[('a', 1), ('b', 2), ('c', 3)]`
- **Očekivani izlaz:** `{'a': 1, 'b': 2, 'c': 3}`

---

## ⚙️ Funkcije, Lambda, Map, Filter

### **Zadatak 56: Faktorijel (rekurzivna funkcija)**
Napiši rekurzivnu funkciju koja izračunava faktorijel datog broja.

- **Primer ulaza:** `5`
- **Očekivani izlaz:** `120`
- **Hint:** *Svaka rekurzivna funkcija mora imati bazni slučaj (uslov za zaustavljanje). Ovde je to kada je broj 1.*

---

### **Zadatak 57: Funkcija sa promenljivim brojem argumenata (`*args`)**
Napiši funkciju `pomnozi_sve` koja prihvata proizvoljan broj numeričkih argumenata i vraća njihov proizvod.

- **Primer ulaza:** `pomnozi_sve(1, 2, 3, 4)`
- **Očekivani izlaz:** `24`

---

### **Zadatak 58: Funkcija sa ključnim argumentima (`**kwargs`)**
Napiši funkciju `kreiraj_profil` koja prihvata proizvoljan broj ključnih argumenata (npr. `ime="Pera"`, `godine=30`) i vraća rečnik sa tim podacima.

- **Primer ulaza:** `kreiraj_profil(ime="Ana", grad="Novi Sad", status="aktivan")`
- **Očekivani izlaz:** `{'ime': 'Ana', 'grad': 'Novi Sad', 'status': 'aktivan'}`

---

### **Zadatak 59: Korišćenje `map` i `lambda`**
Data je lista brojeva. Koristeći `map` i `lambda` funkciju, vrati novu listu gde je svaki broj uvećan za 10.

- **Primer ulaza:** `[1, 2, 3, 4]`
- **Očekivani izlaz:** `[11, 12, 13, 14]`

---

### **Zadatak 60: Korišćenje `filter` i `lambda`**
Data je lista brojeva. Koristeći `filter` i `lambda` funkciju, vrati novu listu koja sadrži samo parne brojeve.

- **Primer ulaza:** `[1, 2, 3, 4, 5, 6]`
- **Očekivani izlaz:** `[2, 4, 6]`

---

### **Zadatak 61: Sortiranje rečnika po vrednosti (lambda)**
Sortiraj rečnik po njegovim vrednostima u opadajućem redosledu, vraćajući listu torki.

- **Primer ulaza:** `{'a': 10, 'b': 30, 'c': 20}`
- **Očekivani izlaz:** `[('b', 30), ('c', 20), ('a', 10)]`

---

### **Zadatak 62: Funkcija kao argument**
Napiši funkciju `primeni_operaciju` koja prima listu i drugu funkciju kao argument. Funkcija `primeni_operaciju` treba da primeni prosleđenu funkciju na svaki element liste.

- **Primer poziva:** `primeni_operaciju([1, 2, 3], lambda x: x * x)`
- **Očekivani izlaz:** `[1, 4, 9]`

---

### **Zadatak 63: Generator Fibonačijevog niza**
Napiši generator funkciju (`yield`) koja generiše `n` brojeva Fibonačijevog niza.

- **Hint:** *Koristi `yield` umesto `return`. Trebaće ti dve promenljive za praćenje prethodna dva broja u nizu.*

---

### **Zadatak 64: Dekorator za merenje vremena izvršavanja**
Napiši dekorator koji meri i ispisuje vreme potrebno za izvršavanje funkcije koju dekoriše.

- **Hint:** *Dekorator je funkcija koja vraća drugu funkciju (wrapper). Koristi modul `time` da zabeleziš vreme pre i posle poziva originalne funkcije.*

---

## 📁 Rad sa fajlovima i obrada grešaka

### **Zadatak 65: Brojanje linija u fajlu**
Napiši funkciju koja prihvata putanju do fajla i vraća ukupan broj linija u njemu.

---

### **Zadatak 66: Čitanje fajla u listu**
Napiši funkciju koja čita tekstualni fajl i svaku liniju smešta kao poseban element u listu.

---

### **Zadatak 67: Pisanje liste u fajl**
Napiši funkciju koja prihvata listu stringova i upisuje svaki string u novu liniju u fajlu.

---

### **Zadatak 68: Pronalaženje najduže reči u fajlu**
Napiši funkciju koja čita tekstualni fajl i pronalazi najdužu reč u celom fajlu.

---

### **Zadatak 69: Dodavanje teksta na kraj fajla (Append)**
Napiši funkciju koja dodaje novi red teksta na kraj već postojećeg fajla, bez brisanja prethodnog sadržaja.

- **Hint:** *Prilikom otvaranja fajla, koristi mod `"a"`.*

---

### **Zadatak 70: Sigurno deljenje brojeva**
Napiši funkciju koja deli dva broja, ali koristi `try-except` blok da uhvati `ZeroDivisionError` i u tom slučaju vrati poruku: `"Greška: Deljenje nulom nije dozvoljeno."`

---

### **Zadatak 71: Konverzija u `int` sa obradom greške**
Napiši funkciju koja pokušava da konvertuje dati string u `int`. Ako je konverzija uspešna, vrati broj. Ako nije (npr. string je `"abc"`), uhvati `ValueError` i vrati `0`.

---

## 🎯 Osnove objektno-orijentisanog programiranja (OOP)

### **Zadatak 72: Klasa `Automobil`**
Kreiraj klasu `Automobil` sa atributima `marka`, `model` i `godiste`. Dodaj metodu `prikazi_info` koja ispisuje sve podatke o automobilu u formatiranom stringu.

---

### **Zadatak 73: Klasa `Krug`**
Kreiraj klasu `Krug` koja se inicijalizuje sa poluprecnikom (`r`). Dodaj metode `izracunaj_povrsinu` i `izracunaj_obim`.

---

### **Zadatak 74: Klasa `BankaRacun`**
Kreiraj klasu `BankaRacun` sa atributom `stanje`. Dodaj metode `uplata(iznos)` i `isplata(iznos)`. Metoda `isplata` ne sme dozvoliti da stanje ode ispod nule.

---

### **Zadatak 75: Nasleđivanje klasa**
Kreiraj baznu klasu `Zivotinja` sa metodom `oglasi_se`. Zatim kreiraj izvedene klase `Pas` i `Macka` koje nasleđuju `Zivotinja` i implementiraju (`override`) metodu `oglasi_se` tako da ispisuju "Av av" i "Mjau".

---

### **Zadatak 76: Statička metoda**
U klasu `Kalkulator` dodaj statičku metodu `saberi(a, b)` koja ne zahteva kreiranje instance klase da bi bila pozvana (`Kalkulator.saberi(5, 3)`).

- **Hint:** *Koristi dekorator `@staticmethod`.*

---

## 🧩 Algoritmi i rešavanje problema

### **Zadatak 77: FizzBuzz**
Napiši funkciju koja ispisuje brojeve od 1 do `N`. Ako je broj deljiv sa 3, umesto broja ispiši "Fizz". Ako je deljiv sa 5, ispiši "Buzz". Ako je deljiv i sa 3 i sa 5, ispiši "FizzBuzz".

- **Primer ulaza:** `15`
- **Hint:** *Redosled provera je bitan. Prvo proveri da li je broj deljiv sa oba (15), pa tek onda pojedinačno.*

---

### **Zadatak 78: Prosti brojevi**
Napiši funkciju koja proverava da li je dati broj prost (deljiv samo sa 1 i samim sobom).

- **Hint:** *Dovoljno je da proveravaš deljivost samo do kvadratnog korena datog broja.*

---

### **Zadatak 79: Generisanje prostih brojeva**
Napiši funkciju koja generiše i vraća listu svih prostih brojeva do datog broja `N`.

---

### **Zadatak 80: Binarna pretraga**
Implementiraj algoritam binarne pretrage koji pronalazi indeks elementa u **sortiranoj** listi.

- **Hint:** *Ovaj algoritam radi samo na **sortiranoj** listi. Potrebno je da pratiš levi, desni i srednji indeks.*

---

### **Zadatak 81: Anagrami**
Napiši funkciju koja proverava da li su dva data stringa anagrami (sastoje se od istih slova, bez obzira na redosled).

- **Primer ulaza:** `("listen", "silent")`
- **Očekivani izlaz:** `True`
- **Hint:** *Ako sortiraš karaktere u oba stringa, šta dobijaš ako su anagrami?*

---

### **Zadatak 82: Cezarova šifra**
Implementiraj jednostavnu Cezarovu šifru, gde se svako slovo u tekstu pomera za `N` mesta u abecedi.

- **Primer ulaza:** `("abc", 2)`
- **Očekivani izlaz:** `"cde"`

---

### **Zadatak 83: Pronalaženje nedostajućeg broja**
Data je lista od `N-1` jedinstvenih brojeva iz opsega od 1 do `N`. Pronaći broj koji nedostaje.

- **Primer ulaza:** `[1, 2, 4, 5, 6]`
- **Očekivani izlaz:** `3`
- **Hint:** *Izračunaj zbir brojeva koji bi trebalo da budu u listi (od 1 do N), a zatim od toga oduzmi zbir elemenata koji su stvarno u listi.*

---

### **Zadatak 84: Preplitanje dve liste**
Napiši funkciju koja spaja dve liste tako što naizmenično uzima elemente iz prve i druge liste.

- **Primer ulaza:** `(['a', 'b', 'c'], [1, 2, 3])`
- **Očekivani izlaz:** `['a', 1, 'b', 2, 'c', 3]`

---

## 🔬 Složeniji zadaci sa strukturama podataka

### **Zadatak 85: Matrično transponovanje**
Napiši funkciju koja transponuje matricu (zamenjuje redove i kolone). Matrica je predstavljena kao lista listi.

- **Primer ulaza:** `[[1, 2, 3], [4, 5, 6]]`
- **Očekivani izlaz:** `[[1, 4], [2, 5], [3, 6]]`
- **Hint:** *Pametan trik je da koristiš `zip(*matrica)`.*

---

### **Zadatak 86: Pronalaženje najčešćeg elementa**
Napiši funkciju koja pronalazi element koji se najčešće ponavlja u listi.

- **Primer ulaza:** `[1, 3, 3, 2, 1, 3, 4, 3]`
- **Očekivani izlaz:** `3`
- **Hint:** *Rečnik za brojanje frekvencija je dobar prvi korak. Možeš iskoristiti i `max()` sa `key` argumentom.*

---

### **Zadatak 87: Validacija zagrada**
Napiši funkciju koja proverava da li su u stringu sve zagrade `()`, `{}`, `[]` ispravno uparene i zatvorene.

- **Primer ulaza:** `"({[]})"` → `True`, `"([)]"` → `False`
- **Hint:** *Koristi stek (stack, možeš ga implementirati pomoću liste). Kada naiđeš na otvorenu zagradu, stavi je na stek. Kada naiđeš na zatvorenu, proveri da li odgovara poslednjoj otvorenoj.*

---

### **Zadatak 88: Duboko poređenje rečnika**
Napiši funkciju koja proverava da li su dva rečnika identična, uključujući i ugnežđene rečnike.

---

### **Zadatak 89: Rimska u arapske brojeve**
Napiši funkciju koja konvertuje broj zapisan rimskim ciframa u arapski (ceo broj).

- **Primer ulaza:** `"XXI"`
- **Očekivani izlaz:** `21`
- **Hint:** *Kreiraj rečnik za vrednosti rimskih cifara. Ako je vrednost trenutne cifre manja od sledeće (npr. 'I' pre 'V' u "IV"), oduzmi je. U suprotnom, dodaj je.*

---

### **Zadatak 90: "Ravno" predstavljanje rečnika**
Napiši funkciju koja "spljoštava" ugnežđeni rečnik.

- **Primer ulaza:** `{'a': 1, 'b': {'c': 2, 'd': 3}}`
- **Očekivani izlaz:** `{'a': 1, 'b.c': 2, 'b.d': 3}`
- **Hint:** *Ovo je dobar kandidat za rekurzivnu funkciju koja kao argumente prima rečnik i trenutnu putanju (prefiks).*

---

### **Zadatak 91: Pronalaženje parova sa datim zbirom**
Napiši efikasnu funkciju koja u listi brojeva pronalazi sve parove čiji je zbir jednak datom broju `S`.

- **Primer ulaza:** `([1, 2, 3, 4, 5], 6)`
- **Očekivani izlaz:** `[(1, 5), (2, 4)]`
- **Hint:** *Za efikasno rešenje, koristi set za proveru da li `S - trenutni_broj` već postoji.*

---

### **Zadatak 92: Množenje matrica**
Napiši funkciju za množenje dve matrice. (Ovo je teži zadatak za kraj).

---

### **Zadatak 93: Generisanje svih permutacija**
Napiši funkciju koja generiše sve moguće permutacije elemenata u listi.

- **Primer ulaza:** `[1, 2]`
- **Očekivani izlaz:** `[[1, 2], [2, 1]]`
- **Hint:** *Modul `itertools` ima ugrađenu funkciju za ovo. Pokušaj prvo da implementiraš samostalno koristeći rekurziju.*

---

### **Zadatak 94: Sortiranje stringa po brojevima unutar njega**
Data je rečenica gde svaka reč sadrži jedan broj. Sortiraj reči u rečenici na osnovu tog broja.

- **Primer ulaza:** `"je4st ovo2 pr1imer te3kst"`
- **Očekivani izlaz:** `"pr1imer ovo2 te3kst je4st"`
- **Hint:** *Podeli rečenicu u reči. Koristi `sorted()` sa `lambda` funkcijom koja će iz svake reči izvući broj za sortiranje.*

---

### **Zadatak 95: Kaprekarova konstanta**
Napiši funkciju koja demonstrira Kaprekarovu rutinu za četvorocifren broj, koja uvek konvergira ka broju 6174.

---

### **Zadatak 96: Run-Length Encoding (RLE)**
Napiši funkciju koja kompresuje string koristeći RLE algoritam.

- **Primer ulaza:** `"AAABBCDDD"`
- **Očekivani izlaz:** `"3A2B1C3D"`
- **Hint:** *Prolazi kroz string i drži brojač za uzastopne iste karaktere. Kada se karakter promeni, dodaj brojač i prethodni karakter u rezultat.*

---

### **Zadatak 97: Dekompresija Run-Length Encoding**
Napiši funkciju koja dekompresuje string kompresovan RLE algoritmom.

- **Primer ulaza:** `"3A2B1C3D"`
- **Očekivani izlaz:** `"AAABBCDDD"`

---

### **Zadatak 98: Sudoku validator**
Napiši funkciju koja proverava da li je data 9x9 Sudoku tabla validna.

- **Hint:** *Napiši tri odvojene provere: za redove, za kolone i za 3x3 blokove. Korišćenje setova može da uprosti proveru duplikata.*

---

### **Zadatak 99: Pascalov trougao**
Napiši funkciju koja generiše prvih `N` redova Pascalovog trougla.

- **Hint:** *Svaki element u novom redu (osim ivica) je zbir dva elementa iznad njega u prethodnom redu.*

---

### **Zadatak 100: Pronalaženje ostrva**
Data je 2D matrica (mreža) koja se sastoji od 1 (kopno) i 0 (voda). Napiši funkciju koja broji ukupan broj "ostrva" (grupa povezanih jedinica).

- **Hint:** *Ovo je problem pretrage. Prolazi kroz matricu. Kada nađeš '1', pokreni pretragu (npr. rekurzivni DFS) koja će sve povezane '1' "potopiti" (pretvoriti u '0') i uvećaj brojač ostrva za jedan.*

---

## 📊 Napomena o rešavanju zadataka

Ova zbirka je dizajnirana za postepeno napredovanje od osnovnih ka složenijim konceptima. Preporučuje se:

1. **Rešavanje zadataka redosledom** - Svaka sekcija gradi na znanju iz prethodne
2. **Korišćenje hintova samo kad zapneš** - Pokušaj prvo samostalno
3. **Refaktorisanje rešenja** - Nakon što zadatak radi, razmisli kako bi mogao biti bolji
4. **Pisanje testova** - Za svaki zadatak napiši bar 2-3 test primera

---

*Srećno sa vežbanjem! 🚀*