# Esercizi — funzioni

**Lezione coperta:** `L08` — definire e chiamare una funzione; parametri per posizione e per nome, valori di default; `return`; visibilità delle variabili; composizione; moduli

Cicli e strutture dati hanno le loro schede, `L06_esercizi.md` e `L07_esercizi.md`, e qui si danno per saputi: il nuovo è **dare un nome a un pezzo di programma**, passargli i dati e farsi restituire il risultato.

**Come si lavora.** Tre gradini, come per le schede precedenti: prima **seguire** il codice e dire che cosa stampa, poi **trovare** l'errore, infine **scrivere**. Le soluzioni sono sotto ogni esercizio: aprile dopo aver provato.

**Il primo gradino si fa con carta e penna**, poi si controlla nell'interprete. Con le funzioni le domande da farsi sono due: **che valore ha ogni parametro**, in questa chiamata? E **che cosa restituisce** la funzione, cioè che cosa c'è dopo `return`?

**Le temperature sono vere**: le minime di Milano dal 1° al 7 gennaio 2011, dal file `MeteoMilano2011.csv` che leggerete con `L09`. Qui sono scritte a mano in una lista:

```python
minime = [-4, -5, -3, -1, -2, -3, 0]
```

---

## Gradino 1 — seguire il codice

## Esercizio 1 — `print` o `return` (difficoltà: •)

Che cosa stampa il programma?

```python
def doppioStampa(n):
    print(n * 2)


def doppioRestituisce(n):
    return n * 2


a = doppioStampa(3)
b = doppioRestituisce(3)
print(a)
print(b)
print(doppioRestituisce(doppioRestituisce(3)))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
6
None
6
12
```

Il primo `6` lo stampa `doppioStampa`, **mentre viene chiamata**: è il `print` dentro la funzione. `doppioRestituisce(3)` invece non stampa niente, restituisce 6 e lo mette in `b`.

**Una funzione senza `return` restituisce `None`**: `a` vale `None`, e `print(a)` lo mostra. Il 6 di `doppioStampa` è comparso sullo schermo, ma non è finito da nessuna parte: non si può sommare, confrontare, passare a un'altra funzione.

L'ultima riga funziona solo con la versione che restituisce: `doppioRestituisce(3)` vale 6, e il 6 diventa il parametro della chiamata esterna, che restituisce 12. **Se il risultato serve ancora, ci vuole `return`**; `print` serve solo a chi guarda lo schermo.

</details>

---

## Esercizio 2 — Parametri per posizione e per nome (difficoltà: •)

Che cosa stampa ciascuna chiamata?

```python
def intervallo(minimo, massimo, passo=1):
    return list(range(minimo, massimo, passo))


print(intervallo(0, 5))
print(intervallo(0, 10, 3))
print(intervallo(massimo=4, minimo=1))
print(intervallo(5, 0, -2))
print(intervallo(0, 10, passo=5))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
[0, 1, 2, 3, 4]
[0, 3, 6, 9]
[1, 2, 3]
[5, 3, 1]
[0, 5]
```

**Per posizione**, gli argomenti vanno ai parametri nell'ordine in cui sono scritti: in `intervallo(0, 10, 3)`, `minimo` è 0, `massimo` è 10, `passo` è 3.

**`passo=1` è un valore di default**: se la chiamata non lo dà, come nella prima, vale 1. Se lo dà, come nella seconda, il default non conta.

**Per nome**, l'ordine non conta più: `intervallo(massimo=4, minimo=1)` assegna ciascun valore al parametro con quel nome. Nell'ultima riga i due modi si mescolano: prima quelli per posizione, poi quelli per nome, mai il contrario.

Il resto è `range` di `L07`: il secondo estremo è escluso, e con un passo negativo si conta all'indietro.

</details>

---

## Esercizio 3 — Dentro e fuori (difficoltà: •)

Che cosa stampa il programma?

```python
x = 10


def f(y):
    x = y + 1
    print("dentro:", x)
    return x * 2


def g():
    print("g vede:", x)


z = f(x)
print("fuori:", x)
print("z:", z)
g()
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
dentro: 11
fuori: 10
z: 22
g vede: 10
```

**`x = y + 1` dentro `f` crea una variabile nuova**, locale, che si chiama `x` come quella di fuori ma è un'altra: nasce con la chiamata e sparisce quando la funzione finisce. La `x` di fuori resta 10.

La chiamata `f(x)` passa il **valore** di `x`, cioè 10, al parametro `y`: `y` vale 10, la `x` locale 11, e la funzione restituisce 22.

**`g` invece la `x` di fuori la vede**: non le assegna niente, quindi `x` non è locale, e Python la cerca fuori dalla funzione. Leggere una variabile di fuori si può; assegnarle dentro una funzione crea una variabile nuova.

</details>

---

## Esercizio 4 — Dove si ferma la funzione (difficoltà: •)

Che cosa stampa il programma?

```python
def segno(t):
    if t < 0:
        return "sotto zero"
    if t > 0:
        return "sopra zero"
    print("controllo finito")


print(segno(-3))
print(segno(4))
print(segno(0))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
sotto zero
sopra zero
controllo finito
None
```

**`return` chiude la funzione**: con -3 il primo `if` restituisce, e il resto della funzione non viene eseguito. Per questo `controllo finito` compare una volta sola.

Con 0 nessuno dei due `if` è vero: la funzione arriva in fondo, stampa `controllo finito` e finisce **senza `return`**. Restituisce quindi `None`, ed è `None` che stampa il `print` della chiamata.

Una funzione che deve sempre restituire qualcosa ha bisogno di un `return` **su ogni strada**. Qui ne manca uno per lo zero: alla fine della funzione, `return "zero"`.

</details>

---

## Esercizio 5 — Una funzione dentro l'altra (difficoltà: •)

Che cosa stampa il programma, e in che ordine?

```python
def piuUno(n):
    print("piuUno di", n)
    return n + 1


def doppio(n):
    print("doppio di", n)
    return n * 2


print(doppio(piuUno(3)))
print(piuUno(doppio(3)))
print(doppio(piuUno(1)) + piuUno(doppio(1)))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
piuUno di 3
doppio di 4
8
doppio di 3
piuUno di 6
7
piuUno di 1
doppio di 2
doppio di 1
piuUno di 2
7
```

**Prima si calcola l'argomento, poi si chiama la funzione**: in `doppio(piuUno(3))` Python deve sapere quanto vale `piuUno(3)` prima di poter chiamare `doppio`. Quindi la funzione scritta più dentro viene eseguita per prima, anche se si legge per seconda.

L'ordine conta: `doppio(piuUno(3))` fa 8, `piuUno(doppio(3))` fa 7.

Nell'ultima riga le due chiamate composte si eseguono **da sinistra a destra**, ciascuna dall'interno verso l'esterno: prima tutta quella a sinistra del `+`, che vale 4, poi tutta quella a destra, che vale 3.

</details>

---

## Gradino 2 — trovare l'errore

## Esercizio 6 — La media di un giorno solo (difficoltà: ••)

La funzione dovrebbe restituire la media delle minime della settimana, ma stampa `-0.5714285714285714`. Dov'è l'errore?

```python
def media(lista):
    somma = 0
    for valore in lista:
        somma = somma + valore
        return somma / len(lista)


minime = [-4, -5, -3, -1, -2, -3, 0]
print(media(minime))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

**Il `return` è dentro il ciclo**: è indentato come la somma. Al primo giro `somma` vale -4, e la funzione restituisce subito -4 / 7, cioè -0,57: gli altri sei giorni non vengono mai sommati.

Il `return` va allineato al `for`, così viene eseguito una volta sola, **dopo** il ciclo:

```python
def media(lista):
    somma = 0
    for valore in lista:
        somma = somma + valore
    return somma / len(lista)
```

Stampa `-2.5714285714285716`, la media vera.

Nessun errore, e un numero plausibile: è il tipo di sbaglio che si trova solo controllando il risultato a mano su un caso piccolo. Una media che dipende solo dal primo valore cambia se si cambia il primo valore, e resta uguale se si cambiano gli altri.

</details>

---

## Esercizio 7 — La scala sbagliata (difficoltà: ••)

La funzione converte una temperatura in gradi Fahrenheit se la scala è `"F"`, e la lascia com'è altrimenti. Il programma dovrebbe stampare -4 gradi convertiti, cioè 24.8. Stampa invece `F`, senza errori. Perché?

```python
def converti(gradi, scala):
    if scala == "F":
        return gradi * 9 / 5 + 32
    return gradi


print(converti("F", -4))
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

**Gli argomenti sono nell'ordine sbagliato**: per posizione, `gradi` riceve `"F"` e `scala` riceve -4. La scala non è `"F"`, quindi la funzione restituisce `gradi` così com'è: la stringa `"F"`.

Due correzioni, ugualmente giuste:

```python
print(converti(-4, "F"))
print(converti(scala="F", gradi=-4))
```

Stampano tutte e due `24.8`. La seconda chiama **per nome**, e lì l'ordine non conta: con una funzione che ha più parametri, i nomi rendono la chiamata leggibile e impossibile da scambiare.

Sarebbe stato meglio un errore. Il ramo del `return gradi` accetta qualunque scala, anche -4, e lascia passare tutto: lo scambio arriva in fondo senza che nessuno se ne accorga.

</details>

---

## Esercizio 8 — Il risultato che non c'è (difficoltà: ••)

Il programma dovrebbe stampare quanti giorni di gelo ci sono stati nella settimana. Che cosa succede?

```python
def contaGelo(lista):
    giorni = 0
    for t in lista:
        if t < 0:
            giorni = giorni + 1
    return giorni


minime = [-4, -5, -3, -1, -2, -3, 0]
contaGelo(minime)
print(giorni)
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
NameError: name 'giorni' is not defined
```

**`giorni` è una variabile locale di `contaGelo`**: esiste solo mentre la funzione lavora, e fuori non c'è. Quello che esce dalla funzione è il **valore** dopo `return`, non la variabile.

E quel valore, qui, va perso: la riga `contaGelo(minime)` chiama la funzione, che restituisce 6, ma nessuno lo raccoglie. Va messo in una variabile del programma, che può avere anche un altro nome:

```python
gelo = contaGelo(minime)
print(gelo)
```

Stampa `6`: lo zero di domenica non è sotto zero.

</details>

---

## Esercizio 9 — La lista che cambia (difficoltà: ••)

La funzione dovrebbe restituire le temperature in gradi Fahrenheit, lasciando com'era la lista in gradi Celsius. Che cosa stampa il programma, e perché?

```python
def inFahrenheit(lista):
    i = 0
    while i < len(lista):
        lista[i] = lista[i] * 9 / 5 + 32
        i = i + 1
    return lista


minime = [-4, -5, -3, -1, -2, -3, 0]
fahrenheit = inFahrenheit(minime)
print(fahrenheit)
print(minime)
```

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```
[24.8, 23.0, 26.6, 30.2, 28.4, 26.6, 32.0]
[24.8, 23.0, 26.6, 30.2, 28.4, 26.6, 32.0]
```

**Le minime in gradi Celsius sono perse.** Il parametro `lista` non è una copia: è un altro nome per **la stessa lista** di `minime`, come nella copia di `L07_d`. `lista[i] = ...` cambia quella lista, e `return lista` restituisce ancora lei: `fahrenheit` e `minime` sono due nomi per una lista sola.

Per lasciare intatta la lista ricevuta, la funzione ne costruisce una **nuova**:

```python
def inFahrenheit(lista):
    nuova = []
    for t in lista:
        nuova.append(t * 9 / 5 + 32)
    return nuova
```

Ora la seconda riga stampa `[-4, -5, -3, -1, -2, -3, 0]`.

Con un numero lo sbaglio non si può fare: `x = x + 1` dentro una funzione crea una variabile locale, come nell'esercizio 3. Con una lista sì, perché `lista[i] = ...` non crea un nome nuovo, **cambia** la lista che c'è.

</details>

---

## Gradino 3 — scrivere

La soluzione sotto ogni esercizio è **una** delle possibili. Ogni esercizio usa le funzioni del precedente: tienile tutte nello stesso file, fino al 12.

## Esercizio 10 — Dallo script alle funzioni (difficoltà: •••)

Nell'esercizio 11 di `L07_esercizi.md` un programma stampava la minima, la massima e la media di una settimana di temperature, con un ciclo solo.

Riscrivilo come tre funzioni, `minima(lista)`, `massima(lista)` e `media(lista)`, ciascuna con il suo ciclo, e usale sulle `minime` di questa scheda. Ogni funzione **restituisce** il risultato; i `print` stanno fuori.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
def minima(lista):
    piuBassa = lista[0]
    for t in lista:
        if t < piuBassa:
            piuBassa = t
    return piuBassa


def massima(lista):
    piuAlta = lista[0]
    for t in lista:
        if t > piuAlta:
            piuAlta = t
    return piuAlta


def media(lista):
    somma = 0
    for t in lista:
        somma = somma + t
    return somma / len(lista)


minime = [-4, -5, -3, -1, -2, -3, 0]
print("minima:", minima(minime))
print("massima:", massima(minime))
print("media:", media(minime))
```

Stampa:

```
minima: -5
massima: 0
media: -2.5714285714285716
```

**Il calcolo resta quello dello script**: cambia solo da dove arrivano i dati, il parametro `lista` invece di una variabile scritta in cima, e dove va il risultato, il `return` invece del `print`.

Il ciclo unico di `L07` è diventato tre cicli, e la lista si scorre tre volte. È il prezzo di avere tre pezzi che si possono usare **anche da soli**: per sapere la minima di un'altra settimana basta `minima(altraSettimana)`, senza ricopiare niente.

**Il massimo parte da `lista[0]`, non da 0**, come in `L07`. Su questa settimana partire da 0 darebbe il risultato giusto per caso, perché la massima è proprio 0; su una settimana tutta sotto zero darebbe 0, una temperatura che non c'è mai stata.

</details>

---

## Esercizio 11 — Funzioni che usano funzioni (difficoltà: •••)

Aggiungi due funzioni:

- `escursione(lista)`, la differenza fra la temperatura più alta e la più bassa, **costruita con `minima` e `massima`** dell'esercizio 10, senza un ciclo nuovo;
- `giorniSotto(lista, soglia=0)`, quanti valori sono sotto la soglia. È `contaGelo` dell'esercizio 8, con la soglia come parametro: senza soglia conta i giorni di gelo.

Prova `giorniSotto` sulle `minime` con la soglia di default e con soglia -3.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
def escursione(lista):
    return massima(lista) - minima(lista)


def giorniSotto(lista, soglia=0):
    giorni = 0
    for t in lista:
        if t < soglia:
            giorni = giorni + 1
    return giorni


print("escursione:", escursione(minime))
print("giorni di gelo:", giorniSotto(minime))
print("giorni sotto -3:", giorniSotto(minime, -3))
```

Stampa:

```
escursione: 5
giorni di gelo: 6
giorni sotto -3: 2
```

**`escursione` è una riga**: il lavoro lo fanno `massima` e `minima`, già scritte e già controllate. È la composizione di `L08_b`, e il motivo per cui conviene spezzare un programma in funzioni piccole.

**Il valore di default rende la funzione più generale senza complicare la chiamata più comune**: `giorniSotto(minime)` fa quello che faceva `contaGelo`, e chi ha bisogno di un'altra soglia la scrive. Sotto -3 ci sono due giorni, -4 e -5: -3 non è *sotto* -3.

</details>

---

## Esercizio 12 — Un modulo vostro (difficoltà: •••)

Sposta le cinque funzioni degli esercizi 10 e 11 in un file `temperature.py`, nella vostra cartella `~/esercizi`, e scrivi accanto un secondo script, `analisi.py`, che le importi e stampi l'escursione e i giorni di gelo delle `minime`.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

`temperature.py` contiene **solo le definizioni**: `minima`, `massima`, `media`, `escursione`, `giorniSotto`, copiate dagli esercizi 10 e 11, senza la lista `minime` e senza `print`.

`analisi.py`:

```python
import temperature as tm

minime = [-4, -5, -3, -1, -2, -3, 0]
print("escursione:", tm.escursione(minime))
print("giorni di gelo:", tm.giorniSotto(minime))
print("giorni sotto -3:", tm.giorniSotto(minime, soglia=-3))
```

Da `~/esercizi`, `python analisi.py` stampa:

```
escursione: 5
giorni di gelo: 6
giorni sotto -3: 2
```

**Il nome del modulo è il nome del file senza `.py`**, e Python lo cerca anzitutto nella cartella dello script che lo importa: per questo i due file stanno insieme. `as tm` dà al modulo un nome corto, e ogni funzione si chiama con il prefisso, `tm.escursione`, come `math.sqrt`.

**Attenzione ai `print` di prova.** Quando Python importa un modulo, ne esegue tutte le righe: un `print(minima([3, 1, 2]))` lasciato in fondo a `temperature.py` per controllare la funzione esce ogni volta che `analisi.py` lo importa, prima di tutto il resto. Le prove si fanno in uno script a parte, oppure si tolgono prima di usare il modulo.

**Non chiamare il file come un modulo che esiste già**: un `numpy.py` nella vostra cartella viene importato **al posto** di numpy, e il dado del gioco dell'oca, `np.random.randint(1, 7)`, smette di funzionare: `AttributeError: module 'numpy' has no attribute 'random'`.

</details>

---

## Esercizio 13 — Cambiare base (difficoltà: •••, la più difficile della scheda)

In `L02` abbiamo visto che il calcolatore rappresenta i numeri **in base 2**. Per scrivere un numero in un'altra base lo si divide per la base, si tiene il resto, e si ripete sul quoziente finché non arriva a 0: i resti sono le cifre, **dall'ultima alla prima**. 13 in base 2: 13 // 2 = 6 resto 1, 6 // 2 = 3 resto 0, 3 // 2 = 1 resto 1, 1 // 2 = 0 resto 1, e 13 si scrive `1101`. In base 16 le cifre sono sedici, e dopo il 9 si usano le lettere: `A` vale 10, `F` vale 15.

Scrivi le funzioni per farlo, in un file `basi.py`, una alla volta e ciascuna usando le precedenti:

1. `cifra(n)`, il carattere che rappresenta una cifra da 0 a 15: da `"0"` a `"9"`, poi da `"A"` a `"F"`. E `valore(carattere)`, il contrario: `valore("F")` è 15;
2. `inBase(n, base=2)`, la stringa che rappresenta l'intero `n` nella base data: `inBase(13)` è `"1101"`, `inBase(255, 16)` è `"FF"`. Con un `while`, dividendo e tenendo i resti;
3. `daBase(testo, base=2)`, il contrario: `daBase("1101")` è 13;
4. `verifica()`, che controlla le due funzioni **l'una con l'altra**: per ogni `n` da 0 a 999, e per le basi 2, 8 e 16, `daBase(inBase(n, base), base)` deve ridare `n`. Stampa i casi sbagliati e restituisce quanti sono;
5. `converti(testo, da, a)`, da una base a un'altra, **senza un ciclo**: `converti("FF", 16, 2)` è `"11111111"`.

Un suggerimento per il punto 3: leggendo `"1101"` da sinistra, ogni cifra nuova moltiplica per la base quello che si è letto finora. Dopo `"1"` si ha 1, dopo `"11"` si ha 1 × 2 + 1 = 3, dopo `"110"` 3 × 2 + 0 = 6.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

```python
CIFRE = "0123456789ABCDEF"


def cifra(n):
    return CIFRE[n]


def valore(carattere):
    i = 0
    while CIFRE[i] != carattere:
        i = i + 1
    return i


def inBase(n, base=2):
    testo = ""
    while n > 0:
        testo = cifra(n % base) + testo
        n = n // base
    if testo == "":
        testo = "0"
    return testo


def daBase(testo, base=2):
    n = 0
    for carattere in testo:
        n = n * base + valore(carattere)
    return n


def verifica():
    errori = 0
    for base in [2, 8, 16]:
        for n in range(1000):
            if daBase(inBase(n, base), base) != n:
                print("sbagliato:", n, "in base", base)
                errori = errori + 1
    return errori


def converti(testo, da, a):
    return inBase(daBase(testo, da), a)


print(inBase(13))
print(inBase(255, 16))
print(inBase(0))
print(daBase("1101"))
print(converti("FF", 16, 2))
print("errori:", verifica())
```

Stampa:

```
1101
FF
0
13
11111111
errori: 0
```

**`CIFRE` è una stringa usata come tabella**: la cifra di valore `n` sta all'indice `n`, quindi `cifra` è un indice e `valore` è la ricerca del contrario. Il nome tutto maiuscolo è una convenzione per dire «questo non cambia mai»; le funzioni lo leggono senza assegnarlo, come la `x` di `g` nell'esercizio 3.

**I resti escono al contrario.** Per 13 i resti, nell'ordine in cui escono, sono `1011`, ma 13 in base 2 è `1101`. Per questo la cifra nuova si mette **davanti**, `cifra(n % base) + testo`, e non in coda. Una mia prima versione la metteva in coda, e `verifica()` ha trovato 2782 casi sbagliati su 3000: gli altri 218 sono quasi tutti numeri che si leggono uguali nei due versi, come `101`.

**Lo zero è un caso a parte.** Con `n = 0` il `while` non fa nemmeno un giro, e `testo` resta vuoto: senza l'`if` dopo il ciclo, `inBase(0)` sarebbe `""`. E `verifica()` **non se ne accorge**, perché `daBase("")` vale 0, che è proprio `n`. Un controllo automatico trova molti errori, non tutti: i casi limite, lo zero, la lista vuota, si provano anche a mano.

**`converti` è una riga** perché il lavoro c'è già: da una base qualsiasi si passa all'intero, e dall'intero all'altra base. È lo stesso principio dell'esercizio 11, portato più in là.

Python queste conversioni le sa fare: `bin(13)` dà `'0b1101'`, `hex(255)` dà `'0xff'` e `int("1101", 2)` dà 13. Usali per **controllare** le tue funzioni, non al loro posto.

</details>
