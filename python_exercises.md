# Python Vežbe - Zbirka Zadataka

## Napomena
Ova zbirka sadrži 27 zadataka za vežbanje Python koncepata poput list comprehension, dictionary comprehension, sortiranja, filtriranja i rada sa kolekcijama podataka.

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

## Dodatne Napomene

Ovi zadaci pokrivaju sledeće Python koncepte:
- List comprehension
- Dictionary comprehension
- Funkcije `zip()`, `enumerate()`, `min()`, `max()`, `sorted()`
- Lambda funkcije
- Ternarni operator
- Rad sa skupovima (sets)
- Filtriranje i transformacija podataka
- Sortiranje po višestrukim kriterijumima

Srećno sa vežbanjem!