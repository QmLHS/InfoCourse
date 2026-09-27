# Esercizi — algoritmi, su carta

**Lezione coperta:** `L03` — algoritmi, linguaggi e programmazione

**Non serve il calcolatore.** Servono carta e penna. Qui non si scrive codice:
si scrivono **passi numerati in italiano**, e si eseguono a mano. È
l'esercizio che rende possibile tutto il resto del corso, ed è anche l'unico
che si può fare in treno.

**I dati sono veri.** Sono le temperature registrate a Milano nel gennaio 2011,
dal file che useremo tutto l'anno. Le massime dal 9 al 15:

| 9 gen | 10 | 11 | 12 | 13 | 14 | 15 |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 5 | 6 | 8 | 9 | 10 | 3 | 3 |

e le minime dal 1° al 6:

| 1 gen | 2 | 3 | 4 | 5 | 6 |
|:--:|:--:|:--:|:--:|:--:|:--:|
| −4 | −5 | −3 | −1 | −2 | −3 |

**Come si lavora.** Gli esercizi salgono di difficoltà in tre gradini: prima
**seguire** un algoritmo già scritto, poi **trovare** l'errore in uno che quasi
funziona, infine **scriverne** uno tu. Le soluzioni sono sotto ogni esercizio:
aprile dopo aver provato, perché la difficoltà qui non è capire la risposta, è
arrivarci.

---

# Primo gradino — seguire

## Esercizio 1 — La somma (difficoltà: •)

Esegui questo algoritmo sulle **massime** (5, 6, 8, 9, 10, 3, 3):

1. `totale` vale 0
2. prendi il primo valore dell'elenco
3. aggiungi il valore che hai in mano a `totale`
4. se ci sono ancora valori, prendi il successivo e torna al passo 3
5. scrivi `totale`

Rispondi a due domande: **quanto vale `totale`** alla fine, e **quante volte**
viene eseguito il passo 3.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

`totale` vale **44**, e il passo 3 viene eseguito **7 volte**, una per valore.

Se hai seguito i passi scrivendo il valore di `totale` dopo ognuno — 0, 5, 11,
19, 28, 38, 41, 44 — hai fatto la cosa che conviene fare sempre: tenere
traccia di come cambia ciò che cambia.

</details>

---

## Esercizio 2 — Contare con una condizione (difficoltà: •)

Sempre sulle massime:

1. `quanti` vale 0
2. prendi il primo valore
3. se il valore è **maggiore di 5**, aumenta `quanti` di 1
4. se ci sono ancora valori, prendi il successivo e torna al passo 3
5. scrivi `quanti`

Quanto vale `quanti`? E quante volte viene eseguito il **confronto** del passo 3?

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

`quanti` vale **4**: superano il 5 i giorni con 6, 8, 9 e 10.

Il confronto viene eseguito **7 volte**, una per valore — anche quando la
risposta è no. È una distinzione che tornerà: *quante volte guardo* e *quante
volte agisco* sono due conteggi diversi.

</details>

---

## Esercizio 3 — Il più grande (difficoltà: •)

1. `massimo` vale il **primo** valore dell'elenco
2. prendi il valore successivo
3. se il valore che hai in mano è maggiore di `massimo`, allora `massimo` prende quel valore
4. se ci sono ancora valori, prendi il successivo e torna al passo 3
5. scrivi `massimo`

Sulle massime: quanto vale `massimo` alla fine, e **quante volte** viene
eseguito il passo 3 — cioè quante volte `massimo` cambia davvero?

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

`massimo` vale **10**, e cambia **4 volte**: 5 diventa 6, poi 8, poi 9, poi 10.
Gli ultimi due giorni, a 3 gradi, non lo cambiano.

Nota il passo 1: `massimo` parte dal **primo valore dell'elenco**, non da zero.
Il perché è l'esercizio 6.

</details>

---

# Secondo gradino — trovare l'errore

Ogni algoritmo di questa sezione **quasi** funziona. Per ciascuno: eseguilo sui
dati indicati, scrivi cosa produce, e di' **quale passo cambieresti e come**.

## Esercizio 4 — La media che non torna (difficoltà: ••)

Sulle **otto** caselle dal 9 al 16 gennaio, dove il 16 è vuoto — quindi
5, 6, 8, 9, 10, 3, 3 e una casella senza misura:

1. `totale` vale 0, `quante` vale 8
2. prendi la prima casella
3. se la casella contiene una misura, aggiungi la misura a `totale`
4. se ci sono ancora caselle, prendi la successiva e torna al passo 3
5. scrivi `totale` diviso `quante`

Cosa produce? E cosa dovrebbe produrre?

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Produce **44 / 8 = 5,5**. Dovrebbe produrre **44 / 7 = 6,29**.

L'algoritmo è attento a non sommare le caselle vuote, ma poi divide per
**quante caselle ci sono** invece che per **quanti valori ha sommato**.

Il passo da cambiare è il **primo**: `quante` non deve valere 8 in partenza,
deve valere 0 e crescere di 1 ogni volta che il passo 3 somma qualcosa.

È l'errore più insidioso della sezione perché il risultato è **plausibile**:
5,5 gradi a gennaio non fa sospettare niente.

</details>

---

## Esercizio 5 — Il massimo che parte male (difficoltà: ••)

Sulle **minime** (−4, −5, −3, −1, −2, −3):

1. `massimo` vale 0
2. prendi il primo valore
3. se il valore è maggiore di `massimo`, allora `massimo` prende quel valore
4. se ci sono ancora valori, prendi il successivo e torna al passo 3
5. scrivi `massimo`

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Produce **0**, che non è nessuno dei valori dell'elenco. La risposta giusta è
**−1**, il 4 gennaio.

`massimo` parte da 0, e nessuna temperatura negativa riesce a superarlo: la
condizione del passo 3 è sempre falsa e il valore iniziale sopravvive fino in
fondo.

Il passo da cambiare è il **primo**: `massimo` deve partire dal **primo valore
dell'elenco**, come nell'esercizio 3. Chi sceglie «parto da un numero molto
piccolo» risolve il caso di oggi e ne prepara un altro per il giorno in cui i
dati saranno più piccoli di quel numero.

</details>

---

## Esercizio 6 — L'azzeramento di troppo (difficoltà: ••)

Sulle massime:

1. prendi il primo valore
2. `totale` vale 0
3. aggiungi il valore a `totale`
4. se ci sono ancora valori, prendi il successivo e torna al passo 2
5. scrivi `totale`

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Produce **3**, cioè l'ultimo valore, e non 44.

Il passo 2 sta **dentro** il giro: `totale` viene azzerato prima di ogni
somma, quindi alla fine contiene solo l'ultimo valore aggiunto.

Non c'è un passo da riscrivere, c'è un passo da **spostare**: l'azzeramento va
prima del passo 1, cioè prima che il giro cominci. Confronta con l'esercizio 1,
dove l'ordine è giusto.

</details>

---

## Esercizio 7 — Un valore di troppo, o uno di meno (difficoltà: ••)

Vogliamo contare i giorni in cui la massima è stata **almeno 3 gradi**. Sulle
massime:

1. `quanti` vale 0
2. prendi il primo valore
3. se il valore è **maggiore di 3**, aumenta `quanti` di 1
4. se ci sono ancora valori, prendi il successivo e torna al passo 3
5. scrivi `quanti`

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Produce **5**, ma la risposta giusta è **7**: tutti e sette i giorni hanno
almeno 3 gradi, compresi i due giorni a 3 esatti.

«Almeno 3» significa «maggiore **o uguale** a 3», e il passo 3 dice solo
«maggiore». I due giorni a 3 gradi cadono esattamente sul confine e vengono
esclusi.

È un errore che non si vede mai sui dati di mezzo e si vede sempre sui casi al
bordo — ed è il motivo per cui, quando si prova un algoritmo, conviene
scegliere apposta un dato che stia **esattamente** sulla soglia.

</details>

---

## Esercizio 8 — Il caso che non c'è (difficoltà: ••)

L'algoritmo della media, questa volta scritto bene:

1. `totale` vale 0, `quanti` vale 0
2. prendi la prima casella
3. se la casella contiene una misura: aggiungi la misura a `totale` e aumenta `quanti` di 1
4. se ci sono ancora caselle, prendi la successiva e torna al passo 3
5. scrivi `totale` diviso `quanti`

Eseguilo su una settimana in cui **il sensore è rimasto spento**: sette caselle,
tutte vuote. Cosa succede?

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

Al passo 5 si divide 0 per **0**, che non è un numero.

L'algoritmo non è sbagliato: è **incompleto**. Non dice cosa fare quando non
c'è nessuna misura, e quel caso non è impossibile — un sensore guasto, un file
troncato, un mese non ancora cominciato.

La correzione è un passo in più prima del 5: *se `quanti` vale 0, scrivi «non
ci sono misure» e fermati*. Qualunque cosa si decida va bene, purché sia
**deciso**: il problema non è la risposta, è il silenzio.

</details>

---

# Terzo gradino — scrivere

Qui non c'è un algoritmo da seguire: c'è un problema in italiano, e devi
produrre tu i passi numerati. Scrivi anche, in testa, **cosa serve in ingresso**
e **cosa si ottiene alla fine**.

## Esercizio 9 — Sopra la media (difficoltà: •••)

Data una serie di temperature, scrivi l'algoritmo che dice **quanti giorni**
hanno avuto una massima superiore alla media del periodo.

Provalo sulle massime e verifica il risultato a mano.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

**Ingresso:** un elenco di temperature. **Uscita:** un numero.

1. calcola la media dell'elenco (è l'algoritmo dell'esercizio 8)
2. `quanti` vale 0
3. prendi il primo valore
4. se il valore è maggiore della media, aumenta `quanti` di 1
5. se ci sono ancora valori, prendi il successivo e torna al passo 4
6. scrivi `quanti`

Sulle massime la media è 6,29 e la risposta è **3**: i giorni da 8, 9 e 10
gradi.

La cosa da notare, e che quasi tutti scoprono sbagliando: **l'elenco va
percorso due volte**. La prima per sapere la media, la seconda per contare —
perché al primo giro la media non esiste ancora, e confrontare un valore con
una media che sta ancora crescendo non significa niente.

</details>

---

## Esercizio 10 — È già ordinato? (difficoltà: •••)

Dato un elenco di numeri, scrivi l'algoritmo che risponde **sì** o **no** alla
domanda: i valori sono in ordine crescente?

Non devi ordinarli. Devi solo dire se lo sono già.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

**Ingresso:** un elenco di numeri. **Uscita:** sì oppure no.

1. prendi il primo valore e chiamalo `precedente`
2. prendi il valore successivo e chiamalo `corrente`
3. se `corrente` è minore di `precedente`, scrivi «no» e **fermati**
4. `precedente` prende il valore di `corrente`
5. se ci sono ancora valori, prendi il successivo come `corrente` e torna al passo 3
6. scrivi «sì»

Sulle massime la risposta è **no**, e l'algoritmo se ne accorge al sesto
valore: dopo il 10 arriva il 3.

Due cose meritano attenzione. La prima è il passo 3: si può **uscire prima**
della fine, appena la risposta è certa — non serve guardare il resto. La
seconda è il passo 6: il «sì» si scrive solo se il giro è finito senza mai
fermarsi, cioè *dopo* aver guardato tutti. Chi mette il «sì» dentro il giro lo
scrive a ogni coppia in ordine, e risponde sette volte a una domanda sola.

</details>

---

## Esercizio 11 — Togliere i buchi (difficoltà: •••)

Data una serie di **caselle** in cui alcune contengono una misura e altre sono
vuote, scrivi l'algoritmo che produce un **nuovo elenco** con le sole misure
presenti, nello stesso ordine.

È il passo che, nell'attività di gruppo, il programma principale si è tenuto
per sé.

### Soluzione

<details>
<summary>Mostra la soluzione</summary>

**Ingresso:** una serie di caselle. **Uscita:** un elenco di numeri.

1. `risultato` è un elenco vuoto
2. prendi la prima casella
3. se la casella contiene una misura, aggiungi quella misura in fondo a `risultato`
4. se ci sono ancora caselle, prendi la successiva e torna al passo 3
5. scrivi `risultato`

Sulle otto caselle dal 9 al 16 gennaio il risultato ha **7** valori.

La differenza rispetto a tutti gli algoritmi precedenti è cosa si accumula: là
era un numero che cresceva, qui è un **elenco** che si allunga. È la stessa
idea — si parte da niente e si aggiunge un pezzo alla volta — applicata a una
cosa diversa da un numero.

</details>
