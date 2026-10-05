# Videolezioni — L05: Selezione

Cinque video, **37 minuti in tutto**. Si guardano **prima** della lezione in
aula, dopo quelli di `L04`: la selezione usa gli operatori di confronto e la
logica booleana che `L04_c` e `L04_f` introducono.

I video stanno nella cartella **Videolezioni** su Google Drive, in
`L05_Selezione/`:

<https://drive.google.com/drive/folders/1V1L8G9y0Rp7lQDawD49cLpxYVbG995hD>

Si apre con l'**account campus**: è condivisa con i soli account d'Ateneo, e il
link è anche sulla pagina Moodle nella sezione di questa lezione.

| Video | Durata | Lucidi | Di cosa parla |
|:---|:---:|:---|:---|
| `L05_p1_Motivazione` | 6′30″ | *Intro* | perché servono le strutture di controllo: sequenza, selezione, iterazione |
| `L05_p2_Sequenza` | 4′17″ | *Sequenza* | l'ordine delle istruzioni, e lo scambio di due variabili |
| `L05_p3_IfElsePass` | 11′11″ | *if*, *if-else*, *pass* | `if`, `if ... else`, e l'istruzione `pass` |
| `L05_p4_CondizioniAnnidate` | 8′55″ | *Annidate* | una condizione dentro un'altra, e l'indentazione che decide il ramo |
| `L05_p5_SelezioneConcatenata` | 7′06″ | *if-elif* | `if ... elif ... else`, e il confronto con l'annidamento |

L'ordine è quello della tabella.

> **Attenzione: il deck non segue l'ordine dei video.** Due differenze, e sono
> nel deck da sempre, non introdotte ora.
>
> `if ... elif ... else` viene **prima** delle condizioni annidate, mentre `p4`
> e `p5` le presentano al contrario. E l'istruzione `pass`, che `p3` tratta
> subito dopo `if-else`, sui lucidi è **l'ultima sezione**, dopo gli esercizi.
>
> Il contenuto è lo stesso. Se studi sul deck, vai nell'ordine delle slide; se
> segui i video, cerca le sezioni per nome.

## Come usarli assieme al resto del materiale

| Se vuoi… | Guarda | Leggi |
|:---|:---|:---|
| capire che cosa sono le strutture di controllo | `p1` | lucidi, sezione *Intro* |
| capire l'indentazione come blocco | `p2`, `p4` | lucidi, *Sequenza* e *Annidate* |
| scrivere il tuo primo `if` | `p3` | lucidi, *if* e *if-else* |
| scegliere fra più alternative | `p5` | lucidi, *if-elif* |
| vedere un programma che si corregge | — | lucidi, sezione *Radici* |
| esercitarti | — | `L04_esercizi.md`, parte sulla selezione |

---

## Dove i lucidi dicono più dei video

**Questa è la sezione da leggere.** I lucidi sono stati rifatti e **tre errori
del deck vecchio sono stati corretti**: nei video quegli errori ci sono ancora.
Dove le due cose divergono **valgono i lucidi**.

### Il codice del valore assoluto non girava

Sul frame del primo `if`, l'esempio che calcola il valore assoluto leggeva così:

```python
a = input("Inserire un numero intero a: ")
if a < 0:
```

`input()` restituisce **sempre una stringa**, e confrontare una stringa con
`0` in Python 3 dà

```
TypeError: '<' not supported between instances of 'str' and 'int'
```

Il programma del video, battuto così com'è, **non parte**. Sui lucidi ora c'è
`eval(input(...))`, la forma usata da tutti gli altri esempi dello stesso deck.

### La formula delle radici era sbagliata

L'esercizio dell'equazione di secondo grado riportava

$$x_{1,2} = -b \pm \frac{\sqrt{b^2-4ac}}{2a}$$

con il **`-b` fuori dalla frazione**. Su `x² - 5x + 6`, le cui radici sono 2 e
3, quella scrittura dà 5.5 e 4.5. La forma corretta è

$$x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$

Il **codice** della slide successiva era invece giusto, e calcola 3.0 e 2.0:
quindi nel video la formula contraddice il programma che le sta accanto. Sui
lucidi è corretta la formula.

### Nel diagramma di flusso mancava una lettera

Nel flow chart dell'algoritmo migliorato il nodo del discriminante diceva
`delta = b*b - 4*c`, senza la `a`. Il codice accanto ha `4*a*c`. Corretto il
nodo.

### L'errore su cui si basa l'esercizio delle radici non avviene più

**Questa è la divergenza più importante, e non è una correzione: è un cambio di
linguaggio.** L'esercizio delle radici è costruito in tre passaggi — si esegue
il programma, si vede che si rompe, si migliora l'algoritmo con un `if` — e il
secondo passaggio si regge sul fatto che la radice di un discriminante negativo
dia errore.

In Python 3 **non lo dà**. Il programma usa `delta**0.5`, e

```python
>>> (-4)**0.5
(1.2246467991473532e-16+2j)
```

restituisce un **numero complesso**, senza protestare. Solo `math.sqrt(-4)`
solleva `ValueError`, e il programma non usa `math.sqrt`.

Nel video — e nella schermata che il deck mostra — si vede l'errore di Python
2. Il ragionamento che segue resta valido e utile: il programma **deve**
comportarsi in modo diverso a seconda del segno di `delta`, perché un complesso
dove ti aspetti due numeri reali è un risultato sbagliato. Ma è un bug
**peggiore** di un'eccezione, non migliore: un'eccezione si ferma e si vede,
un complesso prosegue e finisce nella relazione.

### Cinque frame hanno un titolo che prima non avevano

Nei video cinque slide compaiono senza titolo. Sui lucidi ne hanno uno — tra
cui *Flusso dell'informazione*, *Selezione concatenata* e *variante 2:
l'ipotenusa* — perché il tema stampa il titolo in testa a ogni slide e vuoto
lasciava una riga bianca.

---

## Un'avvertenza generale

I lucidi sono stati rifatti nel formato 16:10 e hanno **sezioni, titoli e
impaginazione diversi** da quelli che si vedono nei filmati. Il contenuto
segue, ma i numeri di slide no: se il video dice «slide 12», cercala per
titolo, non per numero.
