# Autovalutazione — funzioni e file

**Lezioni coperte:** `L08` — funzioni, parametri, moduli; `L09` — file

**Quando farla.** Da solo, **prima** della sessione `A04`. In aula la commentiamo insieme: chi arriva avendola fatta sa già su che cosa chiedere.

**Come funziona.** Due parti.

- **Otto domande a risposta multipla.** Sotto ciascuna trovi la risposta giusta **e il motivo per cui le altre sono sbagliate**: quelle spiegazioni sono la parte che insegna, quindi leggile anche quando hai indovinato.
- **Cinque programmi da scrivere.** Aprili nell'editor, uno per file, e **mandali in esecuzione**: è scrivendo il codice che scopri se hai capito davvero. I primi quattro hanno un **caso piccolo**, che puoi controllare a mano mentre lo scrivi, e un **controllo**, più grande, che dice se il programma regge. Il quinto è fatto come un tema d'esame.

**Non è un voto.** Serve a scoprire che cosa non sai prima che te lo chieda qualcun altro. Se sbagli, segna il numero e portalo in aula.

**I file dei programmi sono già pronti** in `~/InfoCourse/02_ProgrammareInPython/data/`, con gli altri file del corso: cominciano tutti con `A04_`, e dopo un `git pull` li trovi lì. Prima di scrivere il caricamento **apri il file e guardalo**: è la prima cosa da fare con un file che non conosci. Nessun programma usa `input()`.

---

# Parte 1 — Domande

## 1 — Stampare o restituire

Che cosa succede?

```python
def somma(valori):
    totale = 0
    for v in valori:
        totale = totale + v
    print(totale)


risultato = somma([3, 4, 5])
print(risultato + 1)
```

- **A** stampa `12` e poi `13`
- **B** stampa `13`
- **C** stampa `12`, poi si ferma con un errore
- **D** si ferma con un errore senza stampare niente

<details>
<summary>Mostra la risposta</summary>

**C**: stampa `12`, poi si ferma con `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. Il `print` dentro la funzione stampa 12 mentre la funzione lavora; ma la funzione non ha `return`, quindi restituisce `None`, e `None + 1` non si può fare.

- *A* — sarebbe vero con `return totale` al posto di `print(totale)`. Stampare e restituire sono due cose diverse: la prima mostra un valore a chi guarda lo schermo, la seconda lo consegna a chi ha chiamato la funzione;
- *B* — il 12 si vede comunque, perché il `print` dentro la funzione viene eseguito;
- *D* — l'errore arriva alla seconda riga del programma principale, quando la funzione ha già finito e ha già stampato.

</details>

---

## 2 — Per posizione e per nome

Con la funzione `def intervallo(minimo, massimo, passo=1):`, quale di queste chiamate **non** funziona?

- **A** `intervallo(1, 10)`
- **B** `intervallo(1, 10, passo=2)`
- **C** `intervallo(massimo=10, minimo=1)`
- **D** `intervallo(minimo=1, 10)`

<details>
<summary>Mostra la risposta</summary>

**D**, `intervallo(minimo=1, 10)`: `SyntaxError: positional argument follows keyword argument`. Dopo un argomento passato per nome, Python non sa più a quale parametro dare un argomento senza nome. Si scrivono **prima quelli per posizione, poi quelli per nome**.

- *A* — `passo` ha un valore di default, 1, e si può non darlo;
- *B* — prima due per posizione, poi uno per nome: l'ordine giusto;
- *C* — tutti per nome, e allora l'ordine non conta.

È un errore di **sintassi**: Python lo trova prima di eseguire qualunque riga del file.

</details>

---

## 3 — Una variabile dentro e una fuori

Che cosa stampa?

```python
soglia = 0


def gelo(temperature):
    soglia = -5
    conta = 0
    for t in temperature:
        if t < soglia:
            conta = conta + 1
    return conta


print(gelo([-6, -2, 1, -8]), soglia)
```

- **A** `2 0`
- **B** `2 -5`
- **C** `3 0`
- **D** un errore

<details>
<summary>Mostra la risposta</summary>

**A**: `2 0`. Dentro la funzione `soglia = -5` crea una variabile **locale**, che vale solo lì: i valori sotto -5 sono -6 e -8, quindi 2. La `soglia` di fuori non è stata toccata, e vale ancora 0.

- *B* — assegnare dentro una funzione non cambia la variabile di fuori con lo stesso nome: ne crea una nuova;
- *C* — sarebbe la risposta con la soglia a 0: -6, -2 e -8. Ma dentro la funzione vale la `soglia` locale;
- *D* — avere due variabili con lo stesso nome, una dentro e una fuori, è lecito. È solo difficile da leggere: per questo conviene dare alla soglia un parametro, `def gelo(temperature, soglia=-5)`.

</details>

---

## 4 — La lista che entra in una funzione

Che cosa stampa?

```python
def segnaMancante(misure):
    misure.append(None)
    return len(misure)


oggi = [3, -1]
n = segnaMancante(oggi)
print(n, oggi)
```

- **A** `3 [3, -1]`
- **B** `3 [3, -1, None]`
- **C** `2 [3, -1]`
- **D** un errore

<details>
<summary>Mostra la risposta</summary>

**B**: `3 [3, -1, None]`. Il parametro `misure` non è una copia di `oggi`: è **un altro nome per la stessa lista**. `append` la modifica, e la modifica si vede anche da fuori.

- *A* — sarebbe vero se la funzione ricevesse una copia. Con i numeri e le stringhe non si nota, perché non si possono modificare; con le liste e i dizionari sì;
- *C* — `len` viene calcolato dopo l'`append`, quindi conta anche il `None`;
- *D* — `None` è un valore come gli altri, e si può mettere in una lista.

Se la lista di chi chiama non deve cambiare, la funzione ne costruisce una nuova, come in `L08_esercizi`, esercizio 9.

</details>

---

## 5 — Un percorso relativo

Lo script `conta.py` sta nella cartella `~/esercizi`, e il file da leggere sta in `~/esercizi/data/meteo.csv`. Lo script apre il file con `open("data/meteo.csv")`. Lanciato dalla home, con `python esercizi/conta.py`, si ferma con `FileNotFoundError: [Errno 2] No such file or directory: 'data/meteo.csv'`. Perché?

- **A** un percorso relativo parte dalla cartella da cui si lancia lo script
- **B** un percorso relativo parte sempre dalla home
- **C** bisognava scrivere `"./data/meteo.csv"`
- **D** manca `encoding="utf-8"`

<details>
<summary>Mostra la risposta</summary>

**A**: un percorso relativo parte **dalla cartella da cui si lancia lo script**, non da quella dove lo script sta. Lanciato dalla home, Python cerca `~/data/meteo.csv`, che non c'è. Da `~/esercizi`, con `python conta.py`, lo stesso script funziona.

- *B* — parte dalla cartella corrente, che qui è la home per caso;
- *C* — `.` è proprio la cartella corrente: `./data/meteo.csv` e `data/meteo.csv` sono lo stesso percorso, e danno lo stesso errore;
- *D* — un encoding sbagliato dà altri errori, o caratteri sbagliati, ma solo **dopo** aver trovato il file.

Per un percorso che funzioni da dovunque: `pl.Path(__file__).parent / "data" / "meteo.csv"`, che parte dalla cartella dello script. È in aula e in `focus_PythonEOS.md`.

</details>

---

## 6 — La lettera sbagliata

`note.txt` contiene due righe. Il programma vorrebbe leggerle:

```python
with open("note.txt", "w", encoding="utf-8") as f:
    righe = f.readlines()
```

e si ferma con `io.UnsupportedOperation: not readable`. Che cosa contiene `note.txt` **dopo** l'errore?

- **A** le due righe, come prima
- **B** niente: il file è vuoto
- **C** solo la prima riga
- **D** il file non esiste più

<details>
<summary>Mostra la risposta</summary>

**B**: niente. `"w"` svuota il file **appena lo apre**, prima di qualunque lettura o scrittura: l'errore arriva dopo, quando `readlines` prova a leggere un file aperto solo per scrivere. Le due righe sono già perse.

- *A* — sarebbe vero se l'errore arrivasse prima dell'apertura; arriva dopo;
- *C* — `"w"` non tiene niente: il file riparte da zero;
- *D* — il file c'è, è solo vuoto. `"w"` crea il file se non c'è, e lo svuota se c'è.

Su un file di dati che non si può rifare, la regola è: **si apre in `"r"`, e si scrive su un file nuovo**.

</details>

---

## 7 — Dove sta la testina

`dati.csv` ha tre righe: `giorno;minima`, `1;-4`, `2;-5`. Che cosa stampa?

```python
with open("dati.csv", encoding="utf-8") as f:
    intestazione = f.readline()
    righe = f.readlines()
    resto = f.read()
print(len(righe), repr(resto))
```

- **A** `2 ''`
- **B** `3 ''`
- **C** `2 'giorno;minima\n1;-4\n2;-5\n'`
- **D** un errore

<details>
<summary>Mostra la risposta</summary>

**A**: `2 ''`. Ogni lettura parte da dove si è fermata la precedente: `readline` prende l'intestazione, `readlines` le due righe che restano, e dopo la testina è in fondo al file. `read` non trova più niente e restituisce la stringa vuota.

- *B* — l'intestazione l'ha già presa `readline`: `readlines` legge **quello che resta**, non tutto il file;
- *C* — il file non ricomincia da capo da solo. Per rileggerlo serve `f.seek(0)`, o un altro `open`;
- *D* — leggere alla fine del file non è un errore: si ottiene una stringa vuota, o una lista vuota.

</details>

---

## 8 — Un carattere sbagliato

Un file CSV salvato in UTF-8 ha l'intestazione `Data,Max Umidità`. Un programma la legge e stampa `Data,Max UmiditÃ `, senza nessun errore. Con quale `encoding` è stato aperto?

- **A** `"utf-8"`
- **B** `"latin-1"`
- **C** `"ascii"`
- **D** senza `encoding`, su Linux

<details>
<summary>Mostra la risposta</summary>

**B**: `"latin-1"`. In UTF-8 la `à` è scritta con **due byte**; `latin-1` legge ogni byte come un carattere a sé, e di quei due fa `Ã` e un carattere che sembra uno spazio, ma non è `" "`. Non dà mai errore, perché per `latin-1` ogni byte è un carattere valido: per questo lo sbaglio passa inosservato.

- *A* — è la codifica giusta, e legge `Umidità`;
- *C* — ASCII non ha la `à`, e si ferma con `UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 15`;
- *D* — sulla VM il default è UTF-8, e il file si legge bene. Su Windows il default è un altro, e sbaglia come `latin-1`: per questo l'`encoding` si scrive sempre.

</details>

---

# Parte 2 — Programmi

Ogni programma va scritto in un suo file, per esempio `a04_p1.py`, ed eseguito con `python3 a04_p1.py`. **Il calcolo va nelle funzioni**, e le funzioni **restituiscono** il risultato: i `print` stanno nel programma principale. Niente `break`.

Il percorso dei file si costruisce con `pathlib`, come in `L09_esercizi`, e funziona da qualunque cartella lanci lo script:

```python
import pathlib as pl

dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
```

## Programma 1 — Funzioni su una lista

Scrivi due funzioni:

- `statistiche(valori)`, che restituisce la tupla `(minima, massima, media)`, calcolate con un ciclo;
- `giorniSotto(valori, soglia=0)`, che restituisce quanti valori sono **sotto** la soglia.

```python
temperature = [2, -3, -1, 5, -4, 0, 1]
```

**Caso piccolo:** minima **-4**, massima **5**, media **0.0**; **3** giorni sotto zero, e **2** sotto -2.

**Controllo:** con un anno di temperature finte,

```python
temperature = []
for giorno in range(365):
    temperature.append((giorno * 7) % 23 - 8)
```

il programma deve stampare minima **-8**, massima **14**, media **3.02** (con `round(media, 2)`), **127** giorni sotto zero e **95** sotto -2.

<details>
<summary>Mostra la soluzione</summary>

```python
def statistiche(valori):
    minima = valori[0]
    massima = valori[0]
    somma = 0
    for v in valori:
        if v < minima:
            minima = v
        if v > massima:
            massima = v
        somma = somma + v
    return minima, massima, somma / len(valori)


def giorniSotto(valori, soglia=0):
    giorni = 0
    for v in valori:
        if v < soglia:
            giorni = giorni + 1
    return giorni


temperature = [2, -3, -1, 5, -4, 0, 1]
minima, massima, media = statistiche(temperature)
print(minima, massima, round(media, 2), giorniSotto(temperature), giorniSotto(temperature, -2))
```

Tre punti dove si sbaglia:

- **restituire tre valori**: `return minima, massima, somma / len(valori)` restituisce una tupla, e `minima, massima, media = statistiche(...)` la spacchetta. Tre `print` dentro la funzione al posto del `return` stampano gli stessi numeri, ma la funzione restituisce `None`, e la riga di chi la chiama dà `TypeError`;
- **minimo e massimo partono dal primo valore**, non da 0: sulla lista del controllo il massimo partirebbe giusto, ma su una settimana tutta sotto zero `massima = 0` darebbe una temperatura che non c'è;
- **la soglia di default** si usa scrivendo `giorniSotto(temperature)`, senza il secondo argomento; `giorniSotto(temperature, -2)` la sostituisce. Sotto -2 vuol dire `< -2`: il -2 non conta.

</details>

---

## Programma 2 — Un CSV con commenti e buchi

Il file `A04_stazioni.csv` è fatto così:

```
# rete meteo urbana: le minime di una settimana
# un campo vuoto vuol dire che quel giorno la stazione non ha misurato
stazione;lun;mar;mer;gio;ven;sab;dom
Brera;-1;-3;;0;2;1;-2
Lambrate;-2;-4;-5;-1;;0;-3
Juvara;0;-2;-3;1;3;;
Parco Nord;-3;-5;-6;-2;-1;-2;-4
```

Le righe che cominciano con `#` sono commenti; poi c'è un'intestazione; poi una riga per stazione, con le minime dei sette giorni separate da `;`. **Un campo vuoto vuol dire che quel giorno la stazione non ha misurato.**

Scrivi:

- `caricaMinime(nomeFile)`, che restituisce un dizionario che a ogni stazione associa la lista delle sue sette minime, intere, con `None` dove il campo è vuoto;
- `mediaPresenti(valori)`, la media dei soli valori che non sono `None`.

Poi stampa quante stazioni ci sono, quante misure mancano in tutto, e la stazione con la media più bassa.

**Caso piccolo:** **4** stazioni, **4** misure mancanti; la più fredda è **Parco Nord**, con media **-3.29**. Brera ha media **-0.5**: sei misure, non sette.

**Controllo:** con `A04_stazioniMese.csv`, quaranta stazioni per trenta giorni, il programma deve stampare **40** stazioni, **93** misure mancanti, e la più fredda **S00**, con media **-1.89**.

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl

dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"


def caricaMinime(nomeFile):
    minime = {}
    with open(nomeFile, encoding="utf-8") as f:
        intestazione = False
        for riga in f:
            if riga.startswith("#") or riga.strip() == "":
                pass
            elif not intestazione:
                intestazione = True
            else:
                campi = riga.strip().split(";")
                valori = []
                for campo in campi[1:]:
                    if campo == "":
                        valori.append(None)
                    else:
                        valori.append(int(campo))
                minime[campi[0]] = valori
    return minime


def mediaPresenti(valori):
    somma = 0
    presenti = 0
    for v in valori:
        if v is not None:
            somma = somma + v
            presenti = presenti + 1
    return somma / presenti


minime = caricaMinime(dati / "A04_stazioni.csv")
mancanti = 0
piuFredda = None
for stazione in minime:
    mancanti = mancanti + minime[stazione].count(None)
    if piuFredda is None or mediaPresenti(minime[stazione]) < mediaPresenti(minime[piuFredda]):
        piuFredda = stazione
print(len(minime), mancanti, piuFredda, round(mediaPresenti(minime[piuFredda]), 2))
```

Tre punti dove si sbaglia:

- **l'intestazione non è sempre la prima riga**: qui ci sono due commenti prima. La soluzione salta i commenti e tratta come intestazione la **prima riga che non è un commento**, con una variabile che se lo ricorda. Un `readline` prima del ciclo prenderebbe un commento, e `int("lun")` si fermerebbe con `ValueError`;
- **il campo vuoto**: `int("")` dà `ValueError`. Il campo vuoto va riconosciuto prima di convertire, e diventa `None`;
- **la media dei presenti**: dividere per 7 invece che per le misure presenti, o mettere 0 al posto dei buchi, abbassa la media senza nessun errore. Per Brera darebbe -0.43 invece di -0.5: un giorno senza misura **non è un giorno a zero gradi**.

</details>

---

## Programma 3 — Una classifica impaginata

Il file `A04_classifica.txt` è fatto così:

```
POS ATLETA                    SOCIETA               TEMPO
  1 BIANCHI  ANNA MARIA       Nuoto Club Bicocca    1'05"32
  2 ROSSI  GIULIA             Acquatica Milano      1'06"08
  3 VERDI  CHIARA             Nuoto Club Bicocca    1'07"91
  4 NERI  SOFIA ELENA         Polisportiva Lambro   1'10"45
    GALLI  MARTA              Acquatica Milano      Squalif.
```

Un file **a colonne fisse**: la posizione occupa i caratteri da 0 a 3, l'atleta da 4 a 29, la società da 30 a 51, il tempo dal 52 in poi. Un'atleta squalificata non ha posizione, e al posto del tempo c'è `Squalif.`.

Scrivi:

- `centesimi(tempo)`, che da `1'05"32` restituisce 6532, e `None` per `Squalif.`;
- `leggiClassifica(nomeFile)`, che restituisce una lista di tuple `(posizione, atleta, societa, centesimi)`, con `None` dove la posizione manca.

Poi stampa quante atlete ci sono, quante sono squalificate, il distacco in centesimi fra l'ultima classificata e la prima, e quante atlete ha ogni società.

**Caso piccolo:** **5** atlete, **1** squalificata, distacco **513** centesimi; **2** atlete per Nuoto Club Bicocca e Acquatica Milano, **1** per Polisportiva Lambro.

**Controllo:** con `A04_classificaLunga.txt`, quaranta atlete, il programma deve stampare **40** atleti, **4** squalificati, distacco **1443** centesimi, e **14**, **13** e **13** atleti per le tre società.

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl

dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"


def centesimi(tempo):
    if tempo == "Squalif.":
        return None
    minuti, resto = tempo.split("'")
    secondi, cent = resto.split('"')
    return (int(minuti) * 60 + int(secondi)) * 100 + int(cent)


def leggiClassifica(nomeFile):
    classifica = []
    with open(nomeFile, encoding="utf-8") as f:
        f.readline()
        for riga in f:
            posizione = riga[:4].strip()
            if posizione == "":
                posizione = None
            else:
                posizione = int(posizione)
            atleta = riga[4:30].strip()
            societa = riga[30:52].strip()
            tempo = centesimi(riga[52:].strip())
            classifica.append((posizione, atleta, societa, tempo))
    return classifica


classifica = leggiClassifica(dati / "A04_classifica.txt")
squalificate = 0
validi = []
perSocieta = {}
for posizione, atleta, societa, tempo in classifica:
    if tempo is None:
        squalificate = squalificate + 1
    else:
        validi.append(tempo)
    if societa in perSocieta:
        perSocieta[societa] = perSocieta[societa] + 1
    else:
        perSocieta[societa] = 1
print(len(classifica), squalificate, validi[-1] - validi[0], perSocieta)
```

Tre punti dove si sbaglia:

- **`split()` non funziona**: `BIANCHI  ANNA MARIA` è tre parole, `ROSSI  GIULIA` due, e anche le società hanno più parole. Il numero di pezzi cambia da una riga all'altra; la posizione dei caratteri no. Si usa lo **slicing**, e poi `strip()` per togliere gli spazi di riempimento;
- **il tempo ha due separatori**, l'apostrofo e le virgolette: due `split`, uno dopo l'altro. Il `"` dentro una stringa si scrive fra apici, `'"'`;
- **il distacco si calcola sui soli tempi validi**: con la squalificata in fondo, `classifica[-1]` ha tempo `None`, e `None - 6532` dà `TypeError`. Mettere `-1` o `0` al posto di `None` non dà errore, e dà un distacco sbagliato.

</details>

---

## Programma 4 — Un catalogo su più righe

Il file `A04_catalogo.txt` comincia così:

```
codice: B01
titolo: Il nome della rosa
autore: Umberto Eco
anno: 1980

codice: B02
titolo: La donna della domenica
autore: Carlo Fruttero
autore: Franco Lucentini
anno: 1972

...
```

Ogni libro occupa più righe, nella forma `etichetta: valore`, e i libri sono separati da una riga vuota. Un libro può avere **più righe `autore`**. **Dopo l'ultimo libro non c'è una riga vuota.**

Scrivi `caricaCatalogo(nomeFile)`, che restituisce un dizionario che a ogni codice associa un dizionario con il `titolo`, la **lista** degli `autori` e l'`anno`, intero. Poi stampa quanti libri ci sono, i codici dei libri con più di un autore, e i titoli di Carlo Fruttero.

**Caso piccolo:** **5** libri, i libri con più autori sono **`['B02', 'B04']`**, e Carlo Fruttero ha scritto **`['La donna della domenica', 'A che punto è la notte']`**. Il numero di libri si controlla nel terminale, con `grep -c "^codice" A04_catalogo.txt`, dalla cartella `data`.

**Controllo:** con `A04_catalogoLungo.txt` il programma deve stampare **60** libri, e **15** con più di un autore.

<details>
<summary>Mostra la soluzione</summary>

```python
import pathlib as pl

dati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"


def caricaCatalogo(nomeFile):
    catalogo = {}
    libro = None
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            pezzi = riga.split(":", 1)
            etichetta = pezzi[0].strip()
            valore = ""
            if len(pezzi) == 2:
                valore = pezzi[1].strip()
            if etichetta == "codice":
                libro = {"titolo": None, "autori": [], "anno": None}
                catalogo[valore] = libro
            elif etichetta == "titolo":
                libro["titolo"] = valore
            elif etichetta == "autore":
                libro["autori"].append(valore)
            elif etichetta == "anno":
                libro["anno"] = int(valore)
    return catalogo


catalogo = caricaCatalogo(dati / "A04_catalogo.txt")
print(len(catalogo))
piuAutori = []
for codice in catalogo:
    if len(catalogo[codice]["autori"]) > 1:
        piuAutori.append(codice)
print(piuAutori)
titoli = []
for codice in catalogo:
    if "Carlo Fruttero" in catalogo[codice]["autori"]:
        titoli.append(catalogo[codice]["titolo"])
print(titoli)
```

Tre punti dove si sbaglia:

- **salvare il libro alla riga vuota**: è naturale, perché la riga vuota chiude il libro. Ma dopo l'ultimo non ce n'è una, e l'ultimo libro non viene mai salvato: il programma conta **4** libri invece di 5, e **59** invece di 60 nel controllo, senza nessun errore. La soluzione mette il libro nel dizionario **appena comincia**, alla riga `codice`, e lo riempie dopo: `libro` e `catalogo[valore]` sono lo stesso dizionario;
- **l'autore che si ripete**: con `libro["autore"] = valore` il secondo autore sostituisce il primo, e di Fruttero e Lucentini resta solo Lucentini. Un campo che si ripete diventa una **lista**, che nasce vuota a ogni libro;
- **`split(":", 1)` e non `split(":")`**: il secondo argomento dice di spezzare **una volta sola**, al primo `:`, e lascia intero un valore che ne contiene altri. Con `split(":")` un titolo come `Python: il corso` darebbe tre pezzi. La riga vuota fra due libri dà un solo pezzo, per questo il valore si legge solo se i pezzi sono due.

</details>

---

## Programma 5 — Le letture dei sensori, come all'esame

Questo programma è fatto **come un tema d'esame**: le funzioni sono già dichiarate e numerate, il commento sopra ciascuna dice che cosa deve fare, e il corpo principale in fondo è già scritto. Copia il file, completa le funzioni, e lancialo. Finché le funzioni sono vuote si ferma all'`Es. 4)` con un `TypeError`: è normale.

```python
# -*- coding: utf-8 -*-
# Programma 5 - Le letture dei sensori, come all'esame

import pathlib as pl

nomeEsercizio = "Sensori"

lLetture = [("2026-01-12 06:00", "Brera", -1.5), ("2026-01-12 06:00", "Lambrate", -3.0),
            ("2026-01-12 12:00", "Brera", 4.0), ("2026-01-12 12:00", "Lambrate", 2.5),
            ("2026-01-12 18:00", "Brera", 1.0), ("2026-01-12 18:00", "Lambrate", -0.5),
            ("2026-01-13 06:00", "Brera", -2.5), ("2026-01-13 06:00", "Lambrate", -4.5),
            ("2026-01-13 12:00", "Brera", 3.5), ("2026-01-13 12:00", "Lambrate", 3.0)]

"""
Ogni lettura è una tupla (istante, stazione, temperatura): l'istante è una stringa "AAAA-MM-GG HH:MM", la stazione una stringa, la temperatura un float.

Implementate le seguenti funzioni; il commento sopra ciascuna dice che cosa fare. Il corpo principale, in fondo, mostra come vengono chiamate.
"""

"""
1. La funzione `ora(sIstante_IN)` accetta un istante e restituisce l'ora come intero.
Ad esempio da "2026-01-12 18:00" si ottiene 18
"""
def ora(sIstante_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
2. La funzione `mediaPerStazione(lLetture_IN)` accetta una lista di letture e restituisce un dizionario che a ogni stazione associa la media delle sue temperature.
Ad esempio con le sole due letture delle 6:00 del 12 gennaio si ottiene {'Brera': -1.5, 'Lambrate': -3.0}
"""
def mediaPerStazione(lLetture_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
3. La funzione `mediaPerOra(lLetture_IN)` accetta una lista di letture e restituisce un dizionario che a ogni ora del giorno, un intero, associa la media delle temperature lette a quell'ora, in tutte le stazioni e tutti i giorni. Usa la funzione `ora`.
Ad esempio con le sole due letture delle 6:00 del 12 gennaio si ottiene {6: -2.25}
"""
def mediaPerOra(lLetture_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
4. La funzione `caricaLetture(fName_IN)` accetta il percorso di un file, `A04_letture.csv`, e restituisce la lista delle letture che contiene, nella stessa forma di lLetture.
Il file ha una o più righe di commento che cominciano con #, un'intestazione, e poi una lettura per riga, con i campi separati da ; e la temperatura con la virgola decimale:
    # letture dei sensori della rete urbana
    istante;stazione;temperatura
    2026-01-12 06:00;Brera;-1,5
"""
def caricaLetture(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


##########################################################
# Corpo principale: già scritto
##########################################################

print(f"Esercizio {nomeEsercizio}.")
print("\nEs. 1)\n")
print(ora("2026-01-12 18:00"))
print(ora("2026-01-13 06:00"))
print("\nEs. 2)\n")
print(mediaPerStazione(lLetture))
print("\nEs. 3)\n")
print(mediaPerOra(lLetture))
print("\nEs. 4)\n")
fName = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data" / "A04_letture.csv"
lDalFile = caricaLetture(fName)
print(len(lDalFile))
print(lDalFile[0])
print(lDalFile == lLetture)
```

Quando le funzioni sono giuste, il programma stampa:

```
Esercizio Sensori.

Es. 1)

18
6

Es. 2)

{'Brera': 0.9, 'Lambrate': -0.5}

Es. 3)

{6: -2.875, 12: 3.25, 18: 0.25}

Es. 4)

10
('2026-01-12 06:00', 'Brera', -1.5)
True
```

L'ultimo `True` è il controllo: le letture caricate dal file sono **uguali** a quelle di `lLetture`.

<details>
<summary>Mostra la soluzione</summary>

```python
def ora(sIstante_IN):
    sOra = sIstante_IN.split(" ")[1]
    return int(sOra.split(":")[0])


def mediaPerStazione(lLetture_IN):
    dSomme = {}
    dConteggi = {}
    for sIstante, sStazione, fTemperatura in lLetture_IN:
        if sStazione in dSomme:
            dSomme[sStazione] = dSomme[sStazione] + fTemperatura
            dConteggi[sStazione] = dConteggi[sStazione] + 1
        else:
            dSomme[sStazione] = fTemperatura
            dConteggi[sStazione] = 1
    dMedie = {}
    for sStazione in dSomme:
        dMedie[sStazione] = dSomme[sStazione] / dConteggi[sStazione]
    return dMedie


def mediaPerOra(lLetture_IN):
    dTemperature = {}
    for sIstante, sStazione, fTemperatura in lLetture_IN:
        iOra = ora(sIstante)
        if iOra in dTemperature:
            dTemperature[iOra].append(fTemperatura)
        else:
            dTemperature[iOra] = [fTemperatura]
    dMedie = {}
    for iOra in dTemperature:
        dMedie[iOra] = sum(dTemperature[iOra]) / len(dTemperature[iOra])
    return dMedie


def caricaLetture(fName_IN):
    lLetture = []
    with open(fName_IN, encoding="utf-8") as f:
        bIntestazione = True
        for sRiga in f:
            if not sRiga.startswith("#"):
                if bIntestazione:
                    bIntestazione = False
                else:
                    lCampi = sRiga.strip().split(";")
                    fTemperatura = float(lCampi[2].replace(",", "."))
                    lLetture.append((lCampi[0], lCampi[1], fTemperatura))
    return lLetture
```

Quattro punti dove si sbaglia:

- **Es. 1, i due separatori**: l'ora sta dopo lo spazio e prima dei due punti, quindi due `split`. Restituire `"18"`, la stringa, invece di 18 fa stampare lo stesso numero, ma poi `mediaPerOra` userebbe stringhe come chiavi;
- **Es. 2, media e non somma**: servono due dizionari, le somme e i conteggi, oppure un dizionario di liste come nell'Es. 3. Dividere per il numero di letture **di tutte le stazioni** dà 0.45 e -0.25 al posto di 0.9 e -0.5;
- **Es. 3, usare la funzione dell'Es. 1**: è il motivo per cui `ora` esiste. Ricopiare dentro `mediaPerOra` i due `split` funziona, ma un errore andrebbe corretto in due posti;
- **Es. 4, la virgola decimale e le righe prima dei dati**: `float("-1,5")` dà `ValueError`, quindi prima `replace(",", ".")`. E prima dei dati ci sono **due** commenti e un'intestazione: un solo `readline` lascerebbe passare l'intestazione, e `float("temperatura")` si fermerebbe. Il `True` finale dice che i tipi sono giusti: con la temperatura lasciata stringa, le liste sarebbero diverse.

</details>

---

## Che cosa portare in aula

Segna i numeri che hai sbagliato, e i programmi che non danno il controllo. Se sono raggruppati, dicono qualcosa:

| se hai sbagliato | rivedi |
|:---|:---|
| 1, programma 1 | `return` contro `print`, e restituire più valori con una tupla — `L08_a`, `L08_b`; `L08_esercizi` 1, 4 e 10 |
| 2, 3, 4 | come entrano i dati in una funzione: posizione e nome, variabili locali, la lista che non è una copia — `L08_a` *Visibilità*, `L08_b`; `L08_esercizi` 2, 3 e 9 |
| 5, 8 | dove sta il file e come è scritto: percorsi relativi, `pathlib`, `encoding` — `L09_a` *Apertura*; `focus_PythonEOS.md` |
| 6, 7 | le modalità e la testina — `L09_a` *Il nastro*; `L09_esercizi` 2, 3 e 8 |
| programmi 2, 3, 4 | caricare un file di forma diversa: commenti e campi vuoti, colonne fisse, record su più righe — `L09_esercizi` 11–14; `focus_FileSemistrutturati.md` |
| programma 5 | la forma del compito: funzioni con la firma data, una che usa l'altra, il caricamento alla fine — `L09_challenge`, la parte prima |
