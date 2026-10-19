# Videolezioni — L06: Cicli, while

Quattordici video, **1 ora e 42 minuti in tutto**: nove sui cicli (54′) e cinque di esercizi svolti (48′). Si guardano **prima** della lezione in aula, dopo quelli di `L05`: il `while` usa le condizioni e l'indentazione della selezione.

I video stanno nella cartella **Videolezioni** su Google Drive, in `L06_CicliWhile/`:

<https://drive.google.com/drive/folders/1V1L8G9y0Rp7lQDawD49cLpxYVbG995hD>

Si apre con l'**account campus**: è condivisa con i soli account d'Ateneo, e il link è anche sulla pagina Moodle nella sezione di questa lezione.

> **Attenzione: questi video non mostrano i lucidi del corso.** Sono stati registrati su un altro deck, con sfondo bianco, preparato insieme a Mirko Cesarini, e i cinque di esercizi sono registrazioni dello schermo mentre si scrive il codice. Il percorso è lo stesso — perché servono i cicli, il `while`, la trace table, i cicli annidati, i numeri primi — ma esempi, ordine e slide sono diversi.
>
> **Il riferimento sono i lucidi**, `L06_a_CicliWhile` e `L06_b_CicliEsercizi`. I video sono un secondo modo di vedere le stesse cose: la tabella qui sotto dice, per ciascuno, in quale sezione dei lucidi ritrovarlo.

## I cicli — `L06_a`

| Video | Durata | Lucidi | Di cosa parla |
|:---|:---:|:---|:---|
| `L06_a_p1_Introduzione` | 4′45″ | `L06_a`, *Intro* | la media di 2, 3 e *n* numeri scritta **senza cicli**: a ogni numero in più il codice va cambiato in più punti |
| `L06_a_p2_Contatori` | 6′55″ | `L06_a`, *Intro*, *Contatori*, *Accumulatori* | un contatore e un accumulatore al posto di tante variabili; e se i numeri fossero mille? |
| `L06_a_p3_FlowChart` | 1′57″ | `L06_a`, *while* | il ciclo disegnato come diagramma di flusso; perché l'`if` da solo non basta: non torna indietro |
| `L06_a_p4_While` | 5′32″ | `L06_a`, *while* | la sintassi del `while`, l'esempio `a = 0`, `while a < 5` con il suo diagramma |
| `L06_a_p5_EsSequenzaNumeri` | 1′42″ | — | l'esercizio: leggere un numero e stampare i cinque successivi |
| `L06_a_p6_TraceTable` | 8′42″ | `L06_a`, *Trace table* | la trace table della prima soluzione, che stampa da 50 a 54 invece che da 51 a 55: dov'è l'errore? |
| `L06_a_p7_EsSequenzaNumeriCorretto` | 7′25″ | `L06_a`, *Trace table* | la soluzione corretta, e la trace table come strumento per trovare gli errori |
| `L06_a_p8_WhileEIfAnnidati` | 7′22″ | `L06_a`, *while e if*, *Annidati* | un `if` dentro il ciclo; un ciclo dentro un ciclo, con le lancette dell'orologio |
| `L06_a_p9_EsNumeriPrimi` | 10′00″ | `L06_b`, *Primi* | che cos'è un numero primo, e un programma con due cicli annidati che li trova |

L'ordine è quello della tabella.

## Gli esercizi svolti — `L06_b`

Cinque registrazioni dello schermo: l'enunciato è scritto in testa al file, e il video mostra come si arriva alla soluzione, errori compresi. **Prova prima da solo**, poi guarda: gli stessi esercizi sono in `L06_esercizi.md`.

| Video | Durata | L'esercizio |
|:---|:---:|:---|
| `L06_b_p1_Multipli` | 6′23″ | stampare i multipli di 7 o di 9 compresi fra 2 e un limite scelto dall'utente |
| `L06_b_p2_Divisori` | 7′29″ | trovare i divisori comuni di due numeri interi |
| `L06_b_p3_Somma` | 5′56″ | sommare i numeri da 1 a N con un ciclo, e verificare il risultato con la formula di Gauss |
| `L06_b_p4_Casuale` | 16′51″ | contare quante volte escono 1, 2 e 3 estraendo numeri a caso |
| `L06_b_p5_Floyd` | 11′04″ | stampare il triangolo di Floyd: 1, poi 2 3, poi 4 5 6… |

Questi esercizi non sono sui lucidi: `L06_b` ne svolge altri — varianza, numeri primi, l'area sotto una parabola. Sono complementari, non alternativi.

## Come usarli assieme al resto del materiale

| Se vuoi… | Guarda | Leggi |
|:---|:---|:---|
| capire perché servono i cicli | `a_p1`, `a_p2` | `L06_a`, *Intro* |
| scrivere il tuo primo `while` | `a_p3`, `a_p4` | `L06_a`, *while* |
| seguire un programma riga per riga | `a_p6`, `a_p7` | `L06_a`, *Trace table* |
| contare e accumulare | `a_p2` | `L06_a`, *Contatori*, *Accumulatori*, *Sentinella* |
| mettere un ciclo dentro un altro | `a_p8` | `L06_a`, *Annidati* |
| un esempio completo | `a_p9` | `L06_b`, *Primi* |
| esercitarti | `b_p1` … `b_p5` | `L06_esercizi.md` |

---

## Dove i lucidi dicono più dei video

**Sui lucidi c'è materiale che nei video non c'è**, e serve:

- il **ciclo infinito**, e come interrompere un programma con `ctrl + c`;
- gli **operatori di incremento** `+=`, `-=`, `*=`, `/=`, `%=`;
- il **valore sentinella**: un valore speciale che chiude l'inserimento;
- la **varianza**, con la differenza fra quella della popolazione e quella campionaria;
- **più algoritmi per lo stesso problema**: sui numeri primi, saltare i pari e fermarsi alla radice di *n* riduce i giri da un milione a mille.

## Tre cose dei video da leggere con attenzione

### `float()` per avere i decimali

In `a_p1` la media è scritta `me = float(a1+a2)/2`, con un commento che dice che il `float` serve «in Py2» per avere risultati con la virgola. In Python 3 **non serve**: la divisione `/` restituisce sempre un numero decimale, come hai visto in `L04`. `(a1 + a2) / 2` basta.

### `%f` per stampare

I video stampano con `print('Media: %f' % (me))`. Funziona, ed è descritto in `L04_c`; nei lucidi si usano le **f-string**, `print(f"Media: {me}")`, che mettono la variabile direttamente dove si legge.

### `Casuale` usa un modulo che non abbiamo ancora visto

`b_p4` genera numeri a caso con `randint`, del modulo `random`, che si importa con `import random`. I moduli arrivano in `L08`: guarda il video per il ragionamento sul ciclo e sui contatori, e prendi `import` come una riga da ricopiare.

---

## Un'avvertenza generale

Video e lucidi **non hanno le stesse slide**: se un video dice «slide 12», non cercarla sui lucidi. Usa la colonna *Lucidi* della prima tabella, che indica la sezione — il nome sta in testa a ogni slide.
