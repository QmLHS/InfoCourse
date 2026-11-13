# Autovalutazione — le strutture dati

**Lezione coperta:** `L07` — strutture dati complesse e iteratori

**Quando farla.** Da solo, **prima** della sessione `A03`. In aula la commentiamo insieme: chi arriva avendola fatta sa già su che cosa chiedere.

**Come funziona.** Due parti.

- **Otto domande a risposta multipla.** Sotto ciascuna trovi la risposta giusta **e il motivo per cui le altre sono sbagliate**: quelle spiegazioni sono la parte che insegna, quindi leggile anche quando hai indovinato.
- **Cinque programmi da scrivere.** Aprili nell'editor, uno per file, e **mandali in esecuzione**: è scrivendo il codice che scopri se hai capito davvero. I primi quattro hanno un **caso piccolo**, che puoi controllare a mano mentre lo scrivi, e un **controllo**: un risultato che a mano non si ottiene, e che il tuo programma deve stampare uguale. Il quinto è fatto come un tema d'esame, e ogni domanda dice che cosa deve stampare. La soluzione è sotto «Mostra la soluzione»: aprila **dopo**.

**Non è un voto.** Serve a scoprire che cosa non sai prima che te lo chieda qualcun altro. Se sbagli, segna il numero e portalo in aula.

Nessun programma usa `input()`: i dati sono scritti nelle prime righe, e per provare un altro caso basta cambiarli.

---

# Parte 1 — Domande

## 1 — Un indice e uno slicing

Che cosa stampa?

```python
regione = 'Lombardia'
print(regione[-1], regione[2:5])
```

<details>
<summary>Mostra la risposta</summary>

**`a mba`**: `regione[-1]` è l'ultimo carattere, e `regione[2:5]` prende le posizioni 2, 3 e 4.

- *`a omb`* — le posizioni partono da 0: la `L` è in posizione 0, la `o` in posizione 1, la `m` in posizione 2;
- *`a mbar`* — lo slicing si ferma **prima** del secondo numero: `[2:5]` dà 5 − 2 = 3 caratteri;
- *errore* — gli indici negativi sono permessi, e contano dalla fine: `-1` è l'ultimo, `-2` il penultimo.

</details>

---

## 2 — A che livello

Le minime di tre giorni, mese per mese:

```python
minime = {'gen': [-2, 1, -4], 'feb': [3, 0, 5]}
```

Quale espressione dà `0`, la minima del secondo giorno di febbraio?

- **A** `minime['feb'][1]`
- **B** `minime[1]['feb']`
- **C** `minime['feb', 1]`
- **D** `minime['feb'][2]`

<details>
<summary>Mostra la risposta</summary>

**A**: prima la chiave del dizionario, `'feb'`, che dà la lista `[3, 0, 5]`; poi l'indice della lista, `1`, che dà `0`.

- *B* — l'ordine è rovesciato: `minime[1]` cerca la **chiave** `1`, che non c'è, e dà `KeyError: 1`;
- *C* — `minime['feb', 1]` cerca una sola chiave, la tupla `('feb', 1)`, e dà `KeyError`;
- *D* — `[2]` è il **terzo** giorno, e dà `5`.

Ogni parentesi quadra scende di un livello, e a ogni livello si usa quello che **quel** livello capisce: chiavi per il dizionario, posizioni per la lista. Quando non sei sicuro, stampa un livello alla volta: `print(minime['feb'])`.

</details>

---

## 3 — Una stringa che non cambia

Che cosa stampa?

```python
parola = 'pane'
parola.replace('p', 'c')
print(parola)
```

<details>
<summary>Mostra la risposta</summary>

**`pane`**: `replace` **non modifica** la stringa, ne restituisce una nuova, e qui nessuno la conserva.

- *`cane`* — sarebbe la risposta con `parola = parola.replace('p', 'c')`, che dà un nome alla stringa nuova;
- *un errore* — `replace` funziona: è assegnare a una posizione, `parola[0] = 'c'`, che dà `TypeError`;
- *`None`* — `replace` restituisce la stringa nuova, non `None`. È `sort`, sulle liste, che modifica e restituisce `None`.

Le stringhe non si modificano: ogni metodo delle stringhe dà una stringa nuova.

</details>

---

## 4 — Due righe, una lista

Che cosa stampa?

```python
base = [0, 0]
tabella = [base, base]
tabella[0][0] = 5
print(tabella)
```

<details>
<summary>Mostra la risposta</summary>

**`[[5, 0], [5, 0]]`**: le due righe di `tabella` sono **la stessa lista**, `base`, scritta due volte.

- *`[[5, 0], [0, 0]]`* — sarebbe così se le righe fossero due liste diverse, per esempio `tabella = [[0, 0], [0, 0]]` o `tabella = [list(base), list(base)]`;
- *un errore* — una lista può contenere liste, anche la stessa due volte.

Mettere una lista in un'altra non la copia: si mette **un riferimento** alla stessa lista. Si vede anche dopo: `print(base)` stampa `[5, 0]`.

</details>

---

## 5 — Aggiungere una stringa a una lista

Che cosa stampa?

```python
lettere = ['x']
lettere += 'yz'
print(lettere)
```

<details>
<summary>Mostra la risposta</summary>

**`['x', 'y', 'z']`**: su una lista, `+=` si comporta come `extend`, e aggiunge **uno per uno** gli elementi di quello che riceve. Una stringa è una sequenza di caratteri, quindi entrano `'y'` e `'z'`.

- *`['x', 'yz']`* — sarebbe la risposta con `lettere.append('yz')`, che aggiunge un elemento solo;
- *`'xyz'`* — `lettere` resta una lista: `+=` la modifica, non la trasforma;
- *un errore* — `+=` accetta qualunque sequenza. Dà errore invece `lettere = lettere + 'yz'`, perché `+` vuole una lista da tutti e due i lati: `TypeError: can only concatenate list (not "str") to list`.

</details>

---

## 6 — Che cosa visita il `for`

Che cosa succede?

```python
giorni = {'gen': 31, 'feb': 28, 'mar': 31}
totale = 0
for mese in giorni:
    totale = totale + mese
print(totale)
```

<details>
<summary>Mostra la risposta</summary>

**Un errore**, `TypeError: unsupported operand type(s) for +: 'int' and 'str'`.

- *`90`* — sarebbe la risposta se il `for` desse i valori. Su un dizionario, invece, il `for` dà **le chiavi**: al primo giro `mese` vale `'gen'`, e `0 + 'gen'` non si può calcolare;
- *`'genfebmar'`* — `totale` parte da `0`, che è un intero: sommare una stringa a un intero è un errore, non una concatenazione.

Per sommare i giorni: `totale = totale + giorni[mese]`, oppure `for numGiorni in giorni.values():`. Prima di scrivere il corpo di un `for`, chiediti **che cosa contiene la variabile a ogni giro**: se non lo sai, stampala.

</details>

---

## 7 — Togliere mentre si scorre

Il programma dovrebbe togliere i voti insufficienti. Che cosa stampa?

```python
voti = [18, 17, 16, 25, 15]
for voto in voti:
    if voto < 18:
        voti.remove(voto)
print(voti)
```

<details>
<summary>Mostra la risposta</summary>

**`[18, 16, 25]`**: il `16` sopravvive.

- *`[18, 25]`* — sarebbe la risposta attesa, ma il `for` avanza di **una posizione** a ogni giro. Quando toglie il `17`, in posizione 1, il `16` scivola in posizione 1, e il giro dopo il `for` guarda la posizione 2, dove adesso c'è il `25`. Il `16` non viene mai controllato;
- *un errore* — su una lista Python non se ne accorge, e non dà nessun errore. Sul dizionario, invece, sì: `RuntimeError`.

Non si toglie da quello che si sta scorrendo: si costruisce una lista nuova con quello che si vuole tenere.

```python
sufficienti = []
for voto in voti:
    if voto >= 18:
        sufficienti.append(voto)
```

</details>

---

## 8 — La prima volta

Il programma dovrebbe contare quante volte compare ogni parola. Che cosa succede?

```python
conteggio = {}
for parola in ['oggi', 'piove', 'oggi']:
    conteggio[parola] = conteggio[parola] + 1
print(conteggio)
```

<details>
<summary>Mostra la risposta</summary>

**Un errore**, `KeyError: 'oggi'`, al primo giro.

- *`{'oggi': 2, 'piove': 1}`* — sarebbe la risposta giusta, ma per calcolare `conteggio[parola] + 1` Python deve prima **leggere** `conteggio['oggi']`, e la chiave non c'è ancora;
- *`{'oggi': 1, 'piove': 1}`* — Python non parte da zero da solo: una chiave che manca è un errore, non un valore vuoto.

Due correzioni, equivalenti. La prima volta si crea la chiave: `if parola not in conteggio: conteggio[parola] = 0`, prima dell'incremento. Oppure si legge con un valore di riserva: `conteggio[parola] = conteggio.get(parola, 0) + 1`.

</details>

---

# Parte 2 — Programmi

Ogni programma va scritto in un suo file, per esempio `a03_p1.py`, ed eseguito con `python3 a03_p1.py`. Usa quello che hai visto: le strutture, i loro metodi, `for` e `while`. Niente `break`: un ciclo finisce quando la sua condizione diventa falsa.

## Programma 1 — Sotto zero

Data una lista di temperature, stampa la **media**, **quanti giorni** sono stati sopra la media e la **serie più lunga** di giorni consecutivi **sotto zero**.

```python
temperature = [3, -1, -2, 4, -3, -5, -1, 2]
```

**Caso piccolo:** con la lista sopra la media è **-0.375** (con `round(media, 2)` il programma stampa `-0.38`), i giorni sopra la media sono **3** (il 3, il 4 e il 2) e la serie più lunga sotto zero è di **3** giorni (-3, -5, -1).

**Controllo:** costruisci un anno di temperature, finte, con queste righe:

```python
temperature = []
for giorno in range(365):
    temperature.append((giorno * giorno) % 29 - 9)
```

Il programma deve stampare media **5.03** (arrotondata con `round(media, 2)`), **177** giorni sopra la media e una serie più lunga di **5** giorni.

<details>
<summary>Mostra la soluzione</summary>

```python
temperature = []
for giorno in range(365):
    temperature.append((giorno * giorno) % 29 - 9)

somma = 0
for temperatura in temperature:
    somma = somma + temperatura
media = somma / len(temperature)

sopra = 0
for temperatura in temperature:
    if temperatura > media:
        sopra = sopra + 1

# serie: quanti giorni sotto zero di fila fino a oggi; piuLunga: la serie piu' lunga vista finora
serie = 0
piuLunga = 0
for temperatura in temperature:
    if temperatura < 0:
        serie = serie + 1
        if serie > piuLunga:
            piuLunga = serie
    else:
        serie = 0
print("media:", round(media, 2), "sopra la media:", sopra, "serie piu' lunga:", piuLunga)
```

Tre punti dove si sbaglia:

- **due giri, non uno**: i giorni sopra la media si contano solo dopo aver calcolato la media, quindi servono due `for`. Contare nello stesso giro della somma vuol dire confrontare con una media che non c'è ancora;
- **la serie riparte**: senza `serie = 0` nell'`else`, `serie` conta tutti i giorni sotto zero dell'anno, e il programma stampa `138`;
- **sotto zero vuol dire `< 0`**: con `<= 0` anche i giorni a zero allungano la serie, e il programma stampa `7`.

</details>

---

## Programma 2 — Le parole di un articolo

Data una frase, stampa **quante parole** contiene, la loro **lunghezza media**, **quante** sono più lunghe di 10 caratteri e **quante volte** compare la parola `di`. La punteggiatura non fa parte della parola: `sociali.` è lunga 7, non 8.

```python
frase = "La media di sei voti di matematica, arrotondata all'intero, va sul libretto."
```

**Caso piccolo:** con la frase sopra il programma stampa **12** parole, lunghezza media **5.17**, **1** parola più lunga di 10 caratteri (`arrotondata`) e `di` **2** volte.

**Controllo:** con l'articolo 3 della Costituzione

```python
frase = "Tutti i cittadini hanno pari dignità sociale e sono eguali davanti alla legge, senza distinzione di sesso, di razza, di lingua, di religione, di opinioni politiche, di condizioni personali e sociali. È compito della Repubblica rimuovere gli ostacoli di ordine economico e sociale, che, limitando di fatto la libertà e l'eguaglianza dei cittadini, impediscono il pieno sviluppo della persona umana e l'effettiva partecipazione di tutti i lavoratori all'organizzazione politica, economica e sociale del Paese."
```

deve stampare **74** parole, lunghezza media **5.7**, **6** parole più lunghe di 10 caratteri e `di` **9** volte.

<details>
<summary>Mostra la soluzione</summary>

```python
frase = "Tutti i cittadini hanno pari dignità sociale e sono eguali davanti alla legge, senza distinzione di sesso, di razza, di lingua, di religione, di opinioni politiche, di condizioni personali e sociali. È compito della Repubblica rimuovere gli ostacoli di ordine economico e sociale, che, limitando di fatto la libertà e l'eguaglianza dei cittadini, impediscono il pieno sviluppo della persona umana e l'effettiva partecipazione di tutti i lavoratori all'organizzazione politica, economica e sociale del Paese."

parole = frase.split()
lettere = 0
lunghe = 0
volteDi = 0
for parola in parole:
    pulita = parola.strip('.,')
    lettere = lettere + len(pulita)
    if len(pulita) > 10:
        lunghe = lunghe + 1
    if pulita == 'di':
        volteDi = volteDi + 1
print("parole:", len(parole), "lunghezza media:", round(lettere / len(parole), 2))
print("piu' lunghe di 10:", lunghe, "di:", volteDi)
```

Tre punti dove si sbaglia:

- **`frase.count('di')` non conta le parole**: conta i pezzi di testo, anche dentro le altre parole. Nella frase piccola dà `3`, perché c'è `di` anche in `media`; nell'articolo dà `16`;
- **le virgolette**: la frase contiene apostrofi, `all'intero`, quindi va scritta fra virgolette **doppie**. Fra virgolette semplici l'apostrofo chiude la stringa, e Python dà `SyntaxError`;
- **la punteggiatura**: senza `strip('.,')`, `matematica,` è lunga 11 e diventa una parola lunga, e la media sale.

</details>

---

## Programma 3 — Il dizionario inverso

**Prima parte.** Un dizionario dà la città di ogni prefisso telefonico. Costruisci il dizionario **inverso**, che dà il prefisso di ogni città, e stampa il prefisso di Torino.

```python
prefissi = {'02': 'Milano', '06': 'Roma', '011': 'Torino', '010': 'Genova', '051': 'Bologna'}
```

Deve stampare **`011`**.

**Seconda parte.** Un dizionario dà, per ogni matricola, il corso a cui lo studente si è iscritto. Costruisci il dizionario che dà, per ogni corso, **la lista** delle matricole iscritte. Stampa, per ogni corso, quanti iscritti ha e qual è la prima matricola della lista.

```python
iscrizioni = {'m1': 'Analisi', 'm2': 'Statistica', 'm3': 'Analisi'}
```

**Caso piccolo:** il dizionario costruito è `{'Analisi': ['m1', 'm3'], 'Statistica': ['m2']}`: Analisi ha **2** iscritti, il primo è `m1`; Statistica ne ha **1**, `m2`.

**Controllo:** costruisci duecento iscrizioni con queste righe:

```python
corsiOfferti = ['Analisi', 'Informatica', 'Statistica', 'Demografia', 'Algebra']
iscrizioni = {}
for numero in range(1, 201):
    iscrizioni['m' + str(1000 + numero)] = corsiOfferti[(numero * 3 + numero // 7) % 5]
```

Deve stampare Demografia **40** iscritti (il primo `m1001`), Informatica **39** (`m1002`), Algebra **40** (`m1003`), Statistica **41** (`m1004`), Analisi **40** (`m1005`).

<details>
<summary>Mostra la soluzione</summary>

```python
prefissi = {'02': 'Milano', '06': 'Roma', '011': 'Torino', '010': 'Genova', '051': 'Bologna'}

# prima parte: ogni valore diventa una chiave, e la sua chiave il valore
perCitta = {}
for prefisso, citta in prefissi.items():
    perCitta[citta] = prefisso
print("Torino:", perCitta['Torino'])

corsiOfferti = ['Analisi', 'Informatica', 'Statistica', 'Demografia', 'Algebra']
iscrizioni = {}
for numero in range(1, 201):
    iscrizioni['m' + str(1000 + numero)] = corsiOfferti[(numero * 3 + numero // 7) % 5]

# seconda parte: i corsi si ripetono, quindi a ogni corso va una lista di matricole
perCorso = {}
for matricola, corso in iscrizioni.items():
    if corso not in perCorso:
        perCorso[corso] = []
    perCorso[corso].append(matricola)

for corso, matricole in perCorso.items():
    print(corso, len(matricole), "iscritti, il primo:", matricole[0])
```

Tre punti dove si sbaglia:

- **l'inverso semplice sulla seconda parte**: con `perCorso[corso] = matricola`, come nella prima, ogni matricola **sovrascrive** quella prima, e per ogni corso resta solo l'ultima: Demografia `m1200`, senza nessun errore. Quando i valori si ripetono, l'inverso ha bisogno di una lista;
- **la lista va creata la prima volta, e solo la prima**: senza l'`if`, `perCorso[corso].append(...)` dà `KeyError`; con `perCorso[corso] = []` fuori dall'`if`, la lista riparte vuota a ogni matricola e ognuna contiene un solo iscritto;
- **perché conviene**: per sapere chi è iscritto a Statistica, senza l'inverso bisogna scorrere tutte le duecento iscrizioni; con l'inverso basta `perCorso['Statistica']`. Se le domande sono tante, l'inverso si costruisce una volta e si usa ogni volta.

</details>

---

## Programma 4 — La tabella con l'intestazione

Le presenze in biblioteca, sede per sede e giorno per giorno. La **prima riga** è l'intestazione, con i nomi delle colonne. Dato il nome di un giorno, stampa il **totale delle presenze** di quel giorno, trovando la colonna dall'intestazione. Poi stampa il **totale della settimana** di ogni sede.

```python
tabella = [['sede', 'lun', 'mar', 'mer'],
           ['Centrale', 12, 15, 9],
           ['Bicocca', 20, 18, 25]]
giorno = 'mar'
```

**Caso piccolo:** il martedì è la colonna 2, e il totale è **33**. Le sedi: Centrale **36**, Bicocca **63**.

**Controllo:** costruisci quaranta sedi con queste righe:

```python
tabella = [['sede', 'lun', 'mar', 'mer', 'gio', 'ven']]
for numero in range(1, 41):
    riga = ['sede' + str(numero)]
    for numGiorno in range(5):
        riga.append((numero * 13 + numGiorno * 7) % 50)
    tabella.append(riga)
giorno = 'mer'
```

Deve stampare **970** presenze il mercoledì, e fra le quaranta righe dei totali `sede17` **175**.

<details>
<summary>Mostra la soluzione</summary>

```python
tabella = [['sede', 'lun', 'mar', 'mer', 'gio', 'ven']]
for numero in range(1, 41):
    riga = ['sede' + str(numero)]
    for numGiorno in range(5):
        riga.append((numero * 13 + numGiorno * 7) % 50)
    tabella.append(riga)
giorno = 'mer'

intestazione = tabella[0]
colonna = intestazione.index(giorno)

# le righe dei dati partono dalla seconda: la prima e' l'intestazione
totaleGiorno = 0
for riga in tabella[1:]:
    totaleGiorno = totaleGiorno + riga[colonna]
print(giorno, totaleGiorno)

for riga in tabella[1:]:
    totaleSede = 0
    for presenze in riga[1:]:
        totaleSede = totaleSede + presenze
    print(riga[0], totaleSede)
```

Tre punti dove si sbaglia:

- **l'intestazione non è un dato**: con `for riga in tabella:` il primo giro somma `0 + 'mer'`, e dà `TypeError`. Allo stesso modo, nei totali delle sedi la colonna 0 è il nome: si parte da `riga[1:]`;
- **la colonna si trova, non si conta a mano**: `intestazione.index(giorno)` dà 3 per `'mer'`, perché in posizione 0 c'è `'sede'`. Contando i giorni da 0 si scrive 2 e si somma il martedì; contandoli da 1 si scrive 3 per caso giusto, ma con un'altra intestazione no;
- **`totaleSede = 0` dentro il ciclo delle righe**: fuori, il totale non riparte, e ogni sede somma anche le precedenti.

È la forma dei temi d'esame: una lista di liste con l'intestazione in testa, e le colonne indicate per nome.

</details>

---

## Programma 5 — La biblioteca, come all'esame

Questo programma è fatto come un tema d'esame: la struttura dati è data, e le domande si risolvono una dopo l'altra, nello stesso file.

```python
libri = {
    'B01': {'titolo': 'Il nome della rosa', 'autore': 'Eco', 'anno': 1980, 'prestiti': ['m1003', 'm1017', 'm1003', 'm1042']},
    'B02': {'titolo': 'Le città invisibili', 'autore': 'Calvino', 'anno': 1972, 'prestiti': ['m1008', 'm1003']},
    'B03': {'titolo': 'Il sistema periodico', 'autore': 'Levi', 'anno': 1975, 'prestiti': []},
    'B04': {'titolo': 'Il barone rampante', 'autore': 'Calvino', 'anno': 1957, 'prestiti': ['m1017', 'm1025', 'm1008']},
    'B05': {'titolo': 'Lessico famigliare', 'autore': 'Ginzburg', 'anno': 1963, 'prestiti': ['m1042']},
    'B06': {'titolo': "Se una notte d'inverno un viaggiatore", 'autore': 'Calvino', 'anno': 1979, 'prestiti': ['m1003', 'm1025']},
    'B07': {'titolo': 'Il giorno della civetta', 'autore': 'Sciascia', 'anno': 1961, 'prestiti': ['m1017']},
    'B08': {'titolo': 'La storia', 'autore': 'Morante', 'anno': 1974, 'prestiti': ['m1008', 'm1042', 'm1025']},
}
```

La chiave è il codice del libro. Il valore è un dizionario con quattro campi: `titolo` e `autore` sono stringhe, `anno` è un intero, `prestiti` è la lista delle matricole che hanno preso il libro, nell'ordine dei prestiti; una matricola può comparire più volte.

1. Stampa quanti libri ci sono. *Deve stampare **8**.*
2. Stampa la lista dei titoli di Calvino. *Deve stampare i **3** titoli di `B02`, `B04` e `B06`.*
3. Stampa quanti prestiti ci sono stati in tutto. *Deve stampare **16**.*
4. Stampa la lista dei codici dei libri che la matricola `m1003` ha preso almeno una volta, e quante volte, in tutto, ha preso un libro. *Deve stampare **`['B01', 'B02', 'B06']`** e **4**.*
5. La matricola `m1050` prende *Il sistema periodico*. Registra il prestito e stampa la lista dei prestiti del libro. *Deve stampare **`['m1050']`**.*

<details>
<summary>Mostra la soluzione</summary>

```python
# 1
print(len(libri))

# 2
titoliCalvino = []
for codice, libro in libri.items():
    if libro['autore'] == 'Calvino':
        titoliCalvino.append(libro['titolo'])
print(titoliCalvino)

# 3
totalePrestiti = 0
for codice in libri:
    totalePrestiti = totalePrestiti + len(libri[codice]['prestiti'])
print(totalePrestiti)

# 4
lettore = 'm1003'
presi = []
volte = 0
for codice in libri:
    prestiti = libri[codice]['prestiti']
    if lettore in prestiti:
        presi.append(codice)
    volte = volte + prestiti.count(lettore)
print(presi, volte)

# 5
libri['B03']['prestiti'].append('m1050')
print(libri['B03']['prestiti'])
```

Quattro punti dove si sbaglia:

- **domanda 3, contare i prestiti e non i libri**: `len(libri[codice])` è sempre 4, il numero dei campi, e il programma stampa `32`. Il livello giusto è un passo più sotto, `libri[codice]['prestiti']`;
- **domanda 4, `in` contro `count`**: `in` dice **se** la matricola c'è, ed è quello che serve per la lista dei codici; per sapere **quante volte** serve `count`, perché `m1003` ha preso `B01` due volte. Con un contatore che cresce di uno a ogni `in` vero, il programma stampa `3`;
- **domanda 5, aggiungere e non sostituire**: `libri['B03']['prestiti'] = 'm1050'` sostituisce la lista con una stringa, e il prossimo `append` dà `AttributeError`. A un libro che ha già dei prestiti, li cancellerebbe;
- **domanda 5, il codice e non il titolo**: la domanda dà il titolo, ma la chiave è il codice. Il codice si trova guardando la struttura, o con un `for` che confronta i titoli: `libri['Il sistema periodico']` dà `KeyError`.

</details>

---

## Che cosa portare in aula

Segna i numeri che hai sbagliato, e i programmi che non danno il controllo. Se sono raggruppati, dicono qualcosa:

| se hai sbagliato | rivedi |
|:---|:---|
| 1, programma 2 | indici, slicing e metodi delle stringhe — `L07_b`; `L07_esercizi` 1 e 6 |
| 2, 6, programmi 4 e 5 | la forma di una struttura annidata, e che cosa visita il `for` — `L07_e`, `L07_f`, `L07_g`; `L07_esercizi` 9 e 10 |
| 3, 4, 5 | che cosa si modifica e che cosa no, e quando due nomi indicano la stessa lista — `L07_b`, `L07_d`; `L07_esercizi` 3, 4 e 6 |
| 7, programma 1 | scorrere una lista: togliere, contare, ricordare una serie — `L07_f`; `L07_esercizi` 8 e 11 |
| 8, programma 3 | costruire un dizionario: la prima volta di una chiave, il dizionario di liste, l'inverso — `L07_e`; `L07_riepilogo`, *Dizionari* |
