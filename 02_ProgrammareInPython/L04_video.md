# Videolezioni — L04: Variabili, istruzioni, espressioni, logica booleana

Sette video, **1 ora e 43 minuti in tutto**. Si guardano **prima** della lezione
in aula: `F04` ha due ore di parte blended, e sono queste.

I video stanno nella cartella **Videolezioni** su Google Drive, in
`L04_VariabiliEIstruzioni/`:

<https://drive.google.com/drive/folders/1V1L8G9y0Rp7lQDawD49cLpxYVbG995hD>

Si apre con l'**account campus**: è condivisa con i soli account d'Ateneo, e il
link è anche sulla pagina Moodle nella sezione di questa lezione.

| Video | Durata | Lucidi | Di cosa parla |
|:---|:---:|:---|:---|
| `L04_a_FileSorgente` | 26′36″ | `L04_a` | i tre modi di usare l'interprete, il file sorgente, commenti e indentazione, case sensitive e parole riservate, `print` e `input` |
| `L04_b_Variabili` | 13′29″ | `L04_b` | perché servono le variabili, nome e valore, le regole per i nomi, la dichiarazione |
| `L04_c_Istruzioni` | 30′08″ | `L04_c` | assegnamento, operatori aritmetici, stringhe, incremento, confronto, appartenenza, operatori logici, `print` e `input` |
| `L04_d_p1_Espressioni` | 3′49″ | `L04_d` | che cos'è un'espressione, e le parentesi |
| `L04_d_p2_PrecedenzaEProprieta` | 5′18″ | `L04_d` | la precedenza degli operatori |
| `L04_e_VariabiliAvanzate` | 13′21″ | `L04_e` | nome e oggetto, spazio dei nomi, identità e tipo, plasticità, la copia |
| `L04_f_p1_LogicaBooleana` | 10′42″ | `L04_f` | il tipo `bool` e le tavole di verità di `not`, `and`, `or` |

L'ordine è quello della tabella. `L04_d_p1` e `p2` sono corti e si guardano di
seguito.

## Come usarli assieme al resto del materiale

| Se vuoi… | Guarda | Leggi |
|:---|:---|:---|
| scrivere il tuo primo file `.py` | `L04_a` | lucidi `L04_a` |
| capire che cos'è una variabile | `L04_b` | lucidi `L04_b` |
| imparare gli operatori | `L04_c` | lucidi `L04_c` |
| sapere in che ordine si valuta un'espressione | `L04_d_p1`, `p2` | lucidi `L04_d` |
| capire che cosa succede con `b = a` | `L04_e` | lucidi `L04_e` |
| ragionare con `and`, `or`, `not` | `L04_f_p1` | lucidi `L04_f` |

---

## Dove i lucidi dicono più dei video

**Questa è la sezione da leggere.** I lucidi che hai sono stati rifatti; i video
no, e non lo saranno. Dove le due cose divergono **valgono i lucidi**.

### `L04_f` — logica booleana: il deck è nuovo

Il video copre le quattro tavole di verità. **Tutto il resto del deck non è nel
video**: il tipo `bool` come quarto tipo, lo XOR, la precedenza fra `not`, `and`
e `or`, le leggi di De Morgan, la valutazione pigra, e i due frame di traduzione
fra lingua ed espressione. È il caso opposto a tutti gli altri: qui il video
esisteva e i lucidi no, e sono stati scritti dopo.

**Due video sono stati ritirati**: la «spy story» in due parti, che poneva un
indovinello sull'`or` inclusivo. Nove minuti per un punto che la riga `V or V =
V` della tavola fa in una riga, e nessuna slide alle spalle. Se ti capita di
trovarli, non servono.

### `L04_c` e `L04_f` si sovrappongono sugli operatori logici

I quattro frame su `not`, `and` e `or` stanno **in coda a `L04_c`**, dentro la
tassonomia degli operatori, e il video `L04_c_Istruzioni` li mostra lì. `L04_f`
li ripresenta dall'inizio e li approfondisce. Non è una svista: il deck di
`L04_c` non si può tagliare senza farlo divergere dal suo video, e la
ripetizione è il prezzo. Se li hai già visti in `L04_c`, in `L04_f` trovi le
stesse tavole più tutto quello che segue.

### Le f-string non sono in nessun video

Gli ultimi due frame di `L04_c` insegnano le **f-string** —
`print(f"media: {media:.2f}")` — che il video non mostra. Sono ammesse
all'esame come la formattazione con `%`: entrambe stanno in
`riepilogo_funzioni_python.md`.

### La tabella delle parole riservate è cambiata

In `L04_a` l'elenco degli identificatori che non si possono usare come nomi era
quello di Python 2: conteneva `print` ed `exec`, che oggi sono funzioni e non
parole chiave, e non conteneva `True`, `False`, `None`, `nonlocal`, `async`,
`await`. **Nel video vedi la tabella vecchia.** Quella giusta è sui lucidi: 35
voci.

### Il frame sulla divisione non parla più di Python 2

In `L04_c` la slide che confrontava la divisione fra Python 2 e Python 3 è
diventata il confronto fra `/` e `//` **in Python 3**, che è l'informazione che
serve: `/` restituisce sempre un `float`, anche fra due interi. Il corso non
insegna Python 2.

### `eval` e la conversione esplicita

In coda a `L04_c` il video mostra `eval(input(...))` per leggere un numero. Il
frame c'è ancora, ma **ne è stato aggiunto uno dopo** sulla conversione
esplicita, `int(input(...))` e `float(input(...))`, che è la strada del corso:
`input()` restituisce sempre una stringa, e dire quale tipo ci si aspetta fa
emergere subito l'errore se l'utente scrive altro.

### Un esempio del video non girava

Nei lucidi di `L04_c` l'esercizio sulla divisione fra numeri **reali** era
scritto in Python 2 — `print "a = %f" % (a, b)` — e così com'era dava
`SyntaxError`. È stato riscritto ed eseguito: gli output sulle slide sono quelli
veri. Nel video vedi la versione vecchia.

---

## Un'avvertenza generale

I lucidi sono stati rifatti nel formato 16:10 e hanno **sezioni, titoli e
impaginazione diversi** da quelli che si vedono nei filmati. Il contenuto
segue, ma i numeri di slide no: se il video dice «slide 12», cercala per
titolo, non per numero.
