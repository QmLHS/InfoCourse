# Esercizi — file

**Lezione coperta:** `L09` — aprire e chiudere un file, `with`; le modalità `"r"`, `"w"`, `"a"`; il nastro e la testina; `read`, `readline`, `readlines`, `tell`; `strip` e `split`; scrivere un file; caricare file di forma diversa

Funzioni, cicli e strutture dati hanno le loro schede, e qui si danno per saputi. Il nuovo è **portare i dati da un file dentro una struttura di Python**: una lista, un dizionario, una lista di tuple. Ogni file ha la sua forma, e la forma decide il codice.

**Come si lavora.** Tre gradini, come per le schede precedenti: prima **seguire** il codice e dire che cosa stampa, poi **trovare** l'errore, infine **scrivere**. Le soluzioni sono sotto ogni esercizio: aprile dopo aver provato.

**I primi due gradini lavorano su un file piccolo, che create voi.** Salvate questo script come `creaMeteo.py` nella vostra cartella `~/esercizi` e lanciatelo da lì: scrive `meteo.txt` accanto a sé.

```python
with open("meteo.txt", "w", encoding="utf-8") as f:
    f.write("giorno;minima\n1;-4\n2;-5\n3;-3\n")
```

Il file ha quattro righe: un'intestazione e tre giorni, con il punto e virgola come separatore. **Ogni riga finisce con `\n`**, anche l'ultima.

**Il terzo gradino lavora sui file del corso**, che stanno in `~/InfoCourse/02_ProgrammareInPython/data/`. Il percorso si costruisce con `pathlib`, come in aula, e funziona da qualunque cartella lanciate lo script:

```python
import pathlib as pl

dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
```

**Ogni caricamento finisce con un conto**: quante righe, quanti record. Il conto si confronta con un numero ottenuto per un'altra strada, `wc -l` o `grep -c` di `L02`. Se i due numeri non tornano, il caricamento ha perso qualcosa, anche senza errori.

---

## Gradino 1 — seguire il codice

## Esercizio 1 — Tre modi di leggere (difficoltà: •)

Che cosa stampa il programma? `repr` mostra le stringhe con le virgolette e con `\n` scritto per esteso, così si vede dove finisce ogni riga.

```python
with open("meteo.txt", encoding="utf-8") as f:
    print(repr(f.readline()))
    print(repr(f.read()))

with open("meteo.txt", encoding="utf-8") as f:
    print(f.readlines())
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
'giorno;minima\n'
'1;-4\n2;-5\n3;-3\n'
['giorno;minima\n', '1;-4\n', '2;-5\n', '3;-3\n']
```

**`readline` legge una riga, `\n` compreso. `read` legge tutto quello che resta**, in una stringa sola: qui le tre righe dei dati, perché l'intestazione l'ha già presa `readline`. **`readlines` legge tutto quello che resta e lo spezza in una lista di righe**, ciascuna con il suo `\n`.

Il secondo `with` riapre il file, e la lettura riparte dall'inizio: per questo `readlines` trova anche l'intestazione.

Il `\n` in fondo a ogni riga è il motivo per cui `print(riga)` in un ciclo lascia una riga vuota fra una riga e l'altra: un a capo è nella riga, l'altro lo aggiunge `print`. Si toglie con `print(riga, end="")`, oppure con `riga.strip()`.

</details>

---

## Esercizio 2 — Dove sta la testina (difficoltà: •)

`tell()` dice in che posizione è la testina, contando i caratteri dall'inizio del file. Che cosa stampa il programma?

```python
with open("meteo.txt", encoding="utf-8") as f:
    print(f.tell())
    f.readline()
    print(f.tell())
    riga = f.readline()
    print(repr(riga), f.tell())
    resto = f.read()
    print(repr(resto), f.tell())
    print(repr(f.read()))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
0
14
'1;-4\n' 19
'2;-5\n3;-3\n' 29
''
```

**Ogni lettura parte da dove si è fermata la precedente**, e sposta la testina in avanti: è il nastro di `L09_a`. All'apertura la testina è a 0. `giorno;minima\n` è lungo 14 caratteri, contando `\n` come uno: dopo il primo `readline` la testina è a 14. Il secondo `readline` legge `1;-4\n`, cinque caratteri, e la testina arriva a 19.

Il primo `readline` legge l'intestazione e la butta: il risultato non va in nessuna variabile. È il modo più semplice di **saltare una riga**.

**Alla fine del file `read` restituisce la stringa vuota**, senza errori. La testina è in fondo, a 29, e non c'è più niente da leggere.

</details>

---

## Esercizio 3 — Scrivere e aggiungere (difficoltà: •)

Che cosa stampa l'ultima riga?

```python
with open("prova.txt", "w", encoding="utf-8") as f:
    f.write("uno\n")
with open("prova.txt", "w", encoding="utf-8") as f:
    f.write("due\n")
with open("prova.txt", "a", encoding="utf-8") as f:
    f.write("tre\n")
with open("prova.txt", "a", encoding="utf-8") as f:
    f.write("quattro")

with open("prova.txt", encoding="utf-8") as f:
    print(repr(f.read()))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
'due\ntre\nquattro'
```

**`"w"` svuota il file appena lo apre**: il secondo `open` in `"w"` cancella `uno`, prima ancora di scrivere `due`. **`"a"` mette la testina in fondo**, e quello che si scrive si aggiunge a quello che c'è.

**`write` scrive esattamente la stringa che riceve**, e non aggiunge l'a capo come fa `print`. `quattro` non ha `\n`, quindi il file non finisce con un a capo: un'altra riga aggiunta dopo finirebbe attaccata, `quattrocinque`.

</details>

---

## Esercizio 4 — I pezzi di una riga (difficoltà: •)

Che cosa stampa il programma?

```python
riga = "2;-5\n"
campi = riga.split(";")
print(campi)
campi = riga.strip().split(";")
print(campi)
print(campi[1] < "-4", int(campi[1]) < -4)
print(campi[0] + campi[1], int(campi[0]) + int(campi[1]))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
['2', '-5\n']
['2', '-5']
False True
2-5 -3
```

**`split` lascia l'a capo attaccato all'ultimo pezzo**: per questo prima si toglie con `strip()`, e poi si spezza. È l'ordine giusto quasi sempre.

**I pezzi sono stringhe, anche quando sembrano numeri.** `"-5" < "-4"` confronta i caratteri uno per uno, come nel dizionario: il segno meno è uguale, e `"5"` viene dopo `"4"`, quindi è `False`. Fra numeri, -5 è minore di -4. E `+` fra stringhe le attacca: `"2" + "-5"` è `"2-5"`.

Un campo numerico si converte con `int` o `float` **subito**, quando si legge la riga: dopo, nel resto del programma, nessuno si ricorda più che era una stringa.

</details>

---

## Gradino 2 — trovare l'errore

## Esercizio 5 — Il file già chiuso (difficoltà: ••)

Il programma dovrebbe stampare la prima riga dei dati. Che cosa succede?

```python
with open("meteo.txt", encoding="utf-8") as f:
    righe = f.readlines()
print(f.readline())
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
ValueError: I/O operation on closed file.
```

**Il `with` chiude il file quando il suo blocco finisce**, cioè alla prima riga non indentata. `f` esiste ancora, ma è un file chiuso, e non si può leggere.

Le righe però sono già state lette, e stanno in `righe`: la prima riga dei dati è `righe[1]`, perché `righe[0]` è l'intestazione. Tutto quello che serve dal file si legge **dentro** il `with`, e si mette in una variabile; fuori si lavora sulla variabile.

</details>

---

## Esercizio 6 — Sommare le minime (difficoltà: ••)

Il programma dovrebbe sommare le minime dei tre giorni. Che cosa succede, e come si corregge?

```python
totale = 0
with open("meteo.txt", encoding="utf-8") as f:
    f.readline()
    for riga in f:
        campi = riga.strip().split(";")
        totale = totale + campi[1]
print(totale)
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

**`campi[1]` è la stringa `"-4"`**, come nell'esercizio 4, e Python non somma un intero e una stringa. Si converte al momento della lettura:

```python
        totale = totale + int(campi[1])
```

Stampa `-12`.

Questa volta l'errore c'è, ed è chiaro. Con `totale = ""` all'inizio non ci sarebbe stato: `+` avrebbe attaccato le stringhe, e il programma avrebbe stampato `-4-5-3` senza lamentarsi.

</details>

---

## Esercizio 7 — Una riga di troppo (difficoltà: ••)

Il programma dovrebbe mettere le minime in una lista di interi. Che cosa succede?

```python
minime = []
with open("meteo.txt", encoding="utf-8") as f:
    for riga in f:
        campi = riga.strip().split(";")
        minime.append(int(campi[1]))
print(minime)
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
ValueError: invalid literal for int() with base 10: 'minima'
```

**La prima riga è l'intestazione**, e il suo secondo campo è la parola `minima`, che non è un numero. Il ciclo la tratta come le altre perché nessuno gli ha detto di saltarla.

Si salta con un `readline` prima del ciclo, come nell'esercizio 2:

```python
with open("meteo.txt", encoding="utf-8") as f:
    f.readline()
    for riga in f:
        ...
```

Stampa `[-4, -5, -3]`. Il `for` riparte da dove si è fermata la testina, cioè dalla seconda riga.

Prima di scrivere il caricamento si guarda **com'è fatto il file**: c'è un'intestazione? Ci sono righe vuote, o commenti? Con `head` di `L02` si vede in un attimo.

</details>

---

## Esercizio 8 — La seconda lettura (difficoltà: ••)

Il programma legge le righe, ne stampa il numero, e poi vuole i dati senza l'intestazione. Perché `dati` è vuota?

```python
with open("meteo.txt", encoding="utf-8") as f:
    righe = f.readlines()
    print(len(righe))
    dati = f.readlines()
    print(len(dati))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
4
0
```

**Dopo il primo `readlines` la testina è in fondo al file**, e il secondo non trova più niente: restituisce una lista vuota, senza errori. Il file non si rilegge da solo.

Non serve rileggerlo: le righe sono già in `righe`, e i dati senza intestazione sono `righe[1:]`, lo slicing di `L07`. Se proprio si vuole rileggere, `f.seek(0)` riporta la testina all'inizio.

</details>

---

## Gradino 3 — scrivere e caricare

Gli esercizi 9 e 10 scrivono un file e lo rileggono. Dall'11 al 14 si caricano quattro file veri, ciascuno con una forma diversa: un CSV con le sue trappole, un TSV, un file a record su più righe, un file impaginato a colonne fisse. Sono le forme viste in aula, e il codice si scrive **guardando il file**, prima di tutto.

La soluzione sotto ogni esercizio è **una** delle possibili.

## Esercizio 9 — Scrivere un CSV (difficoltà: •••)

Scrivi in `minime.csv` le minime di `L08_esercizi.md`, una riga per giorno, con un'intestazione:

```
giorno;minima
1;-4
2;-5
...
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
minime = [-4, -5, -3, -1, -2, -3, 0]

with open("minime.csv", "w", encoding="utf-8") as f:
    f.write("giorno;minima\n")
    giorno = 1
    for t in minime:
        f.write(f"{giorno};{t}\n")
        giorno = giorno + 1
```

`wc -l minime.csv` dice `8`: l'intestazione e sette giorni.

**`write` vuole una stringa.** `f.write(t)` darebbe `TypeError: write() argument must be str, not int`: il numero si mette dentro una f-string, che costruisce la riga intera, separatore e a capo compresi. **L'a capo va scritto**: senza `\n` le sette righe finirebbero tutte attaccate su una.

</details>

---

## Esercizio 10 — Rileggerlo (difficoltà: •••)

Scrivi la funzione `leggiMinime(nomeFile)`, che legge `minime.csv` e restituisce la lista delle minime come interi. Poi calcola l'escursione e i giorni di gelo con le funzioni del modulo `temperature.py` dell'esercizio 12 di `L08_esercizi.md`, che sta nella stessa cartella.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
import temperature as tm


def leggiMinime(nomeFile):
    minime = []
    with open(nomeFile, encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.strip().split(";")
            minime.append(int(campi[1]))
    return minime


minime = leggiMinime("minime.csv")
print(len(minime))
print("escursione:", tm.escursione(minime))
print("giorni di gelo:", tm.giorniSotto(minime))
```

Stampa:

```
7
escursione: 5
giorni di gelo: 6
```

**Il conto torna**: 7 minime, le 8 righe di `wc -l` meno l'intestazione. E i risultati sono quelli di `L08_esercizi`, dove la lista era scritta a mano: il file ha fatto andata e ritorno senza perdere niente.

**Leggere e calcolare stanno in due posti diversi.** `leggiMinime` sa com'è fatto il file e restituisce una lista; le funzioni di `temperature.py` lavorano su una lista e non sanno da dove arrivi. Se domani il file cambia forma, si cambia solo `leggiMinime`.

</details>

---

## Esercizio 11 — Un CSV con le trappole (difficoltà: •••)

`data/telefonate.csv` contiene le telefonate di un mese fra i clienti di un operatore telefonico. Ecco le prime righe:

```
Cod_Chiamante;Cod_Destinatario;Cod_Cella_Chiamante;Cod_Cella_Destinatario;Inizio;Fine
# 22;11;17;16;1:0:1;1:0:4
15;20;14;11;1:1:34;1:1:33
25;49;5;3;1:2:30;1:2:31
```

Separatore `;`, codifica ASCII, a capo di Windows (`\r\n`). La prima riga è l'intestazione; **le righe che cominciano con `#` sono da scartare**. `Inizio` e `Fine` sono `giorno:ora:minuto`.

1. Scrivi `leggiTelefonate(nomeFile)`, che restituisce una lista di tuple `(chiamante, destinatario, giorno)`, tutti interi; il giorno è quello di inizio della chiamata.
2. Scrivi `chiamatePerCliente(telefonate)`, che restituisce un dizionario che a ogni cliente associa il numero di chiamate fatte, e trova il cliente che ne ha fatte di più.
3. Scrivi `chiamatePerGiorno(telefonate)`, che restituisce un dizionario che a ogni giorno associa il numero di chiamate. Quanti giorni ha il mese?

Il conto: quante righe ha il file, e quante sono quelle da scartare? `wc -l` e `grep -c "^#"` lo dicono.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl


def leggiTelefonate(nomeFile):
    telefonate = []
    with open(nomeFile, encoding="utf-8") as f:
        f.readline()
        for riga in f:
            if not riga.startswith("#"):
                campi = riga.strip().split(";")
                giorno = int(campi[4].split(":")[0])
                telefonate.append((int(campi[0]), int(campi[1]), giorno))
    return telefonate


def chiamatePerCliente(telefonate):
    conteggio = {}
    for chiamante, destinatario, giorno in telefonate:
        if chiamante in conteggio:
            conteggio[chiamante] = conteggio[chiamante] + 1
        else:
            conteggio[chiamante] = 1
    return conteggio


def chiamatePerGiorno(telefonate):
    conteggio = {}
    for chiamante, destinatario, giorno in telefonate:
        if giorno in conteggio:
            conteggio[giorno] = conteggio[giorno] + 1
        else:
            conteggio[giorno] = 1
    return conteggio


dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
telefonate = leggiTelefonate(dati / "telefonate.csv")
print(len(telefonate))

perCliente = chiamatePerCliente(telefonate)
piuAttivo = None
for cliente in perCliente:
    if piuAttivo is None or perCliente[cliente] > perCliente[piuAttivo]:
        piuAttivo = cliente
print(len(perCliente), "clienti; il", piuAttivo, "ha fatto", perCliente[piuAttivo], "chiamate")

perGiorno = chiamatePerGiorno(telefonate)
print(len(perGiorno), "giorni")
```

Stampa:

```
590
50 clienti; il 10 ha fatto 19 chiamate
30 giorni
```

**Il conto**: il file ha 701 righe, e `grep -c "^#"` ne trova 110 da scartare. 701 meno l'intestazione meno 110 fa 590, le telefonate caricate.

**Due separatori, due `split`**: il primo spezza la riga sui `;`, il secondo spezza `1:1:34` sui `:`, e del risultato serve solo il pezzo 0. È lo stesso schema del tempo `4'49"74` del nuoto, in aula.

**Gli a capo `\r\n` qui non si vedono**: aprendo un file in modalità testo Python li trasforma in `\n`, e `strip()` toglie comunque tutti e due. Diventano un problema con un `split` senza `strip`: l'ultimo campo, `Fine`, porterebbe con sé l'a capo.

**Un dizionario che conta** è lo schema del conteggio delle lettere in `L07_esercizi`: se la chiave c'è si aumenta, altrimenti si crea a 1. Le due funzioni di conteggio sono quasi identiche; cambia solo **quale elemento della tupla** fa da chiave.

</details>

---

## Esercizio 12 — Perché esiste il TSV (difficoltà: •••)

`data/itemsFOD.tsv` è il catalogo di un supermercato online:

```
ID	DESCRIPTION	UNIT_SALE_PRICE
0	Esselunga, Cornetti gusto formaggio 100 g	0.59
1	Esselunga, crema vaniglia conf. 4x125 g	1.59
```

Separatore il **tab**, `"\t"`; codifica UTF-8; un'intestazione.

1. Prova prima `split(",")` sulla riga del prodotto 0: quanti pezzi escono, e perché?
2. Scrivi `leggiProdotti(nomeFile)`, che restituisce un dizionario che a ogni ID associa la tupla `(descrizione, prezzo)`, con l'ID intero e il prezzo `float`.
3. Trova il prodotto più caro, e conta quanti prodotti costano meno di un euro.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Con la virgola come separatore i pezzi sono **due**, `['0\tEsselunga', ' Cornetti gusto formaggio 100 g\t0.59']`: la virgola sta **dentro** la descrizione, e il tab non la spezza. Su tutto il file `split(",")` dà uno, due o tre pezzi, a seconda di quante virgole ha la descrizione. Il tab nelle descrizioni non compare mai: per questo il file usa lui.

```python
import pathlib as pl


def leggiProdotti(nomeFile):
    prodotti = {}
    with open(nomeFile, encoding="utf-8") as f:
        f.readline()
        for riga in f:
            campi = riga.strip().split("\t")
            prodotti[int(campi[0])] = (campi[1], float(campi[2]))
    return prodotti


dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
prodotti = leggiProdotti(dati / "itemsFOD.tsv")
print(len(prodotti))

piuCaro = None
economici = 0
for codice in prodotti:
    descrizione, prezzo = prodotti[codice]
    if piuCaro is None or prezzo > prodotti[piuCaro][1]:
        piuCaro = codice
    if prezzo < 1:
        economici = economici + 1
print(prodotti[piuCaro])
print(economici)
```

Stampa:

```
120
('Oral-B, Precision Clean testina ricambio per spazzolino elettrico 2 pezzi', 8.85)
6
```

**Il conto**: `wc -l` dice 121, cioè l'intestazione e 120 prodotti.

**Il separatore si sceglie fra i caratteri che nei dati non compaiono mai.** La virgola nei testi è ovunque; il punto e virgola un po' meno; il tab quasi mai. Un CSV con le virgole nei campi esiste, ma ha bisogno delle virgolette attorno al campo, e `split` da solo non basta più.

**Dal dizionario esce una tupla**, e si spacchetta: `descrizione, prezzo = prodotti[codice]`, come in `L07`.

</details>

---

## Esercizio 13 — Record su più righe (difficoltà: •••)

`data/pubmedCoronavirus.txt` è il file di PubMed visto in aula: ogni pubblicazione comincia con una riga `PMID`, ha i suoi campi uno per riga, e finisce con una riga vuota. Le etichette occupano i primi 4 caratteri, il valore comincia dal settimo:

```
PMID- 32060789
DP  - 2020 Feb 14
TI  - The First Disease X is Caused by a Highly Transmissible Acute Respiratory
      Syndrome Coronavirus.
PL  - China
AID - 10.1007/s12250-020-00206-5 [doi]
AID - 10.1007/s12250-020-00206-5 [pii]
```

In aula la struttura associava a ogni PMID data, titolo, luogo e DOI. Qui ne serve un'altra:

1. Scrivi `leggiPubblicazioni(nomeFile)`, che restituisce un dizionario che a ogni PMID associa un dizionario con l'**anno** (intero, i primi 4 caratteri di `DP`), il **luogo** (`PL`) e la **lista di tutti gli identificativi** `AID`, che possono essere zero, uno o più.
2. Scrivi `contaPerAnno(pubblicazioni)`, che restituisce un dizionario che a ogni anno associa il numero di pubblicazioni, e trova l'anno con più pubblicazioni.
3. Quante pubblicazioni non hanno nessun identificativo?

Il conto: `grep -c "^PMID"` dice quante pubblicazioni ci sono. **Il tuo dizionario deve averne altrettante.**

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl


def leggiPubblicazioni(nomeFile):
    pubblicazioni = {}
    pub = None
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            etichetta = riga[:4].strip()
            valore = riga[6:].strip()
            if etichetta == "PMID":
                pub = {"anno": None, "luogo": None, "identificativi": []}
                pubblicazioni[valore] = pub
            elif etichetta == "DP":
                pub["anno"] = int(valore[:4])
            elif etichetta == "PL":
                pub["luogo"] = valore
            elif etichetta == "AID":
                pub["identificativi"].append(valore)
    return pubblicazioni


def contaPerAnno(pubblicazioni):
    conteggio = {}
    for pmid in pubblicazioni:
        anno = pubblicazioni[pmid]["anno"]
        if anno in conteggio:
            conteggio[anno] = conteggio[anno] + 1
        else:
            conteggio[anno] = 1
    return conteggio


dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
pubblicazioni = leggiPubblicazioni(dati / "pubmedCoronavirus.txt")
print(len(pubblicazioni))

perAnno = contaPerAnno(pubblicazioni)
anno = None
for a in perAnno:
    if anno is None or perAnno[a] > perAnno[anno]:
        anno = a
print(anno, perAnno[anno])

senza = 0
for pmid in pubblicazioni:
    if len(pubblicazioni[pmid]["identificativi"]) == 0:
        senza = senza + 1
print(senza)
```

Stampa:

```
14817
2015 781
2432
```

**Il conto torna**: 14 817, come `grep -c "^PMID"`. **La pubblicazione entra nel dizionario appena comincia**, alla riga `PMID`, e si riempie dopo: `pub` e `pubblicazioni[valore]` sono lo stesso dizionario. Se invece la si salva alla riga vuota, come nella prima versione vista in aula, l'ultima si perde, perché il file non finisce con una riga vuota: il dizionario ne ha 14 816, **e il 1949 sparisce da `perAnno`**, perché quella pubblicazione è l'unica di quell'anno.

**Un campo che si ripete diventa una lista**: `"identificativi"` nasce vuota a ogni `PMID`, e ogni riga `AID` le aggiunge un elemento. Le pubblicazioni senza identificativi restano con la lista vuota, ed è così che si contano.

**Le righe che non servono non si nominano.** Il seguito del titolo, le righe senza etichetta, `TI` e la riga vuota non entrano in nessun ramo, e il ciclo passa oltre.

Il 2015 supera di poco il 2004, che ne ha 779: sono gli anni della MERS e della SARS. Il 2020 ne ha 346 perché il file si ferma a febbraio.

</details>

---

## Esercizio 14 — Colonne fisse, un'altra struttura (difficoltà: •••)

`data/gareNuoto.txt` è il file delle gare di nuoto visto in aula: un file impaginato per la stampa, dove l'intestazione dice di che gara sono le righe sotto, e ogni campo sta sempre negli stessi caratteri:

```
        400 stile libero  femminile  -  Categoria  Master 25      Tempo Base :  4'23"38
----------------------------------------------------------------------------------------------
       1   GUARESCHI  MARTINA             1990   Coopernuoto                 4'33"59  962,68
```

Il nome dell'atleta sta nei caratteri da 10 a 41, l'anno di nascita da 42 a 47, il tempo da 76 a 84.

In aula la struttura era per **gara**. Qui serve per **atleta**:

1. Scrivi `leggiAtleti(nomeFile)`, che restituisce un dizionario che a ogni atleta, identificato dalla tupla `(nome, anno di nascita)`, associa la lista delle sue prestazioni `(specialità, tempo)`. La specialità è la parte dell'intestazione prima del trattino, per esempio `400 stile libero femminile`; il tempo resta il testo, `4'33"59`.
2. Quanti atleti ci sono, e quanti hanno nuotato due gare?
3. Chi è l'atleta più anziano, e che gare ha fatto?

Il conto: le prestazioni in tutto il dizionario devono essere 872, quelle contate in aula con la struttura per gara.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl


def leggiAtleti(nomeFile):
    atleti = {}
    specialita = None
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            if "Categoria" in riga:
                specialita = " ".join(riga.split("-")[0].split())
            elif riga.strip() != "" and not riga.startswith("-"):
                atleta = (riga[10:42].strip(), int(riga[42:48]))
                if atleta not in atleti:
                    atleti[atleta] = []
                atleti[atleta].append((specialita, riga[76:85].strip()))
    return atleti


dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
atleti = leggiAtleti(dati / "gareNuoto.txt")
print(len(atleti))

prestazioni = 0
dueGare = 0
piuAnziano = None
for atleta in atleti:
    prestazioni = prestazioni + len(atleti[atleta])
    if len(atleti[atleta]) == 2:
        dueGare = dueGare + 1
    if piuAnziano is None or atleta[1] < piuAnziano[1]:
        piuAnziano = atleta
print(prestazioni, dueGare)
print(piuAnziano, atleti[piuAnziano])
```

Stampa:

```
474
872 398
('FORLANI  GEROLAMO', 1935) [('400 stile libero maschile', '7\'30"56'), ('100 misti maschile', '2\'05"07')]
```

**Il conto torna**: 872 prestazioni, come con la struttura per gara. **Lo stesso file, due strutture**: per gara si risponde a «chi ha vinto i 400 stile?», per atleta a «che gare ha fatto Forlani?». Quale costruire dipende dalla domanda.

**La chiave è una tupla, nome e anno**: due atleti con lo stesso nome finirebbero altrimenti nella stessa lista. In questo file non succede, ma il codice non può saperlo. Una tupla può fare da chiave perché non si modifica; una lista no.

**La specialità sopravvive da una riga all'altra**, come la gara in aula: l'intestazione la cambia, le righe di classifica la usano. Qui si tiene solo la parte prima del trattino, così la stessa specialità di categorie diverse ha lo stesso nome.

Il tempo è rimasto testo, con l'apostrofo e le virgolette: Python lo stampa con `\'` per non confonderlo con l'apostrofo che chiude la stringa. Per confrontare due tempi andrebbe convertito in centesimi, come in aula.

</details>
