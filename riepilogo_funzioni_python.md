# Riepilogo generale delle funzioni Python — Informatica@SGI

Riferimento unico per il corso: **quello che si insegna e quello che si può
chiedere all'esame sono questo documento**, non due elenchi separati.

Prima di oggi erano due: la progressione delle lezioni da una parte, e gli elenchi
«Allowed — pandas» / «Allowed — matplotlib» dentro `temiEsame/CLAUDE.md` dall'altra.
Due liste che possono divergere in silenzio — e in effetti erano divergenti, vedi
[§13 Divergenze](#13-divergenze-da-sanare).

Organizzato secondo la progressione delle lezioni, con la numerazione di
`MAPPA_RINOMINI.md`.

## Come si legge

| Marca | Significato |
|:--:|---|
| **PYT** | può comparire in un tema d'esame del modulo Python |
| **FOD** | può comparire in un tema d'esame Focus on Data |
| — | si insegna, ma **non** si chiede all'esame |

Una funzione senza marca non è meno importante: è materiale che serve a capire, non
a essere interrogati. `pivot_table` e `apply` stanno qui.

**Regola d'oro per chi scrive i temi:** se non è in questo documento, non si chiede.
Se serve chiederlo, prima lo si insegna e lo si aggiunge qui.

---

## Indice

0. [Vincoli del modulo PYT](#0-vincoli-del-modulo-pyt)
1. [Input, output e conversioni (L04)](#1-input-output-e-conversioni-l04)
2. [Operatori ed espressioni (L04)](#2-operatori-ed-espressioni-l04)
3. [Logica booleana (L04_f)](#3-logica-booleana-l04_f)
4. [Selezione (L05)](#4-selezione-l05)
5. [Iterazione (L06)](#5-iterazione-l06)
6. [Stringhe (L07_b)](#6-stringhe-l07_b)
7. [Liste e tuple (L07_c, L07_d)](#7-liste-e-tuple-l07_c-l07_d)
8. [Dizionari e iteratori (L07_e, L07_f)](#8-dizionari-e-iteratori-l07_e-l07_f)
9. [Funzioni e moduli (L08)](#9-funzioni-e-moduli-l08)
10. [File (L09)](#10-file-l09)
11. [Pandas (L10)](#11-pandas-l10)
12. [Matplotlib (L11)](#12-matplotlib-l11)
13. [Divergenze da sanare](#13-divergenze-da-sanare)

---

## 0. Vincoli del modulo PYT

Il modulo Python si esamina con la sola logica di programmazione espressa nei
costrutti di base. **Non ammessi in un tema d'esame PYT**, né nelle soluzioni:

- classi e programmazione a oggetti
- espressioni `lambda`
- list, dict e set comprehension
- `map`, `filter`, `zip` come costrutti portanti

Non è un'imposizione arbitraria: è quello che i materiali fanno già. Su **124 script
di esempio e 5010 righe** di codice del corso, le comprehension trovate sono
**zero**.

Ammessi: `for`, `while`, `if/elif/else`, `def`, `return`, `break`, `continue`,
`pass`, e i built-in elencati sotto.

---

## 1. Input, output e conversioni (L04)

| Funzione | Scopo | Note |
|:---|:---|:---|
| `print(...)` | Stampa a video | **PYT** **FOD** — separatore `sep=`, terminatore `end=` |
| `input(prompt)` | Legge una riga da tastiera, **sempre come stringa** | **PYT** |
| `int(x)` | Converte in intero; su stringa non numerica solleva errore | **PYT** **FOD** |
| `float(x)` | Converte in numero con virgola | **PYT** **FOD** |
| `str(x)` | Converte in stringa | **PYT** **FOD** |
| `type(x)` | Tipo dell'oggetto | **PYT** |
| `id(x)` | Identità dell'oggetto in memoria | — serve a spiegare l'assegnamento, non si chiede |

> `input()` restituisce **sempre** una stringa: `int(input(...))` è il pattern per
> leggere un numero. È l'errore più frequente nei primi esercizi.

## 2. Operatori ed espressioni (L04)

| Operatore | Scopo |
|:---|:---|
| `+` `-` `*` `/` | Aritmetica. `/` dà sempre un `float`, anche fra interi |
| `//` | Divisione intera |
| `%` | Resto |
| `**` | Potenza |
| `==` `!=` `<` `<=` `>` `>=` | Confronto, restituiscono `True`/`False` |
| `=` `+=` `-=` `*=` `/=` | Assegnamento |

Tutti **PYT** e **FOD**.

| Funzione | Scopo | Note |
|:---|:---|:---|
| `abs(x)` | Valore assoluto | **PYT** |
| `round(x, n)` | Arrotondamento | **PYT** |
| `min(...)` `max(...)` | Minimo, massimo — su più argomenti o su una sequenza | **PYT** **FOD** |
| `sum(seq)` | Somma degli elementi | **PYT** |
| `len(x)` | Lunghezza di stringa, lista, tupla, dizionario | **PYT** **FOD** |

> **La precedenza degli operatori** è materia di `L04_d`: `2 + 3 * 4` fa 14, non 20.
> In caso di dubbio, parentesi.

## 3. Logica booleana (L04_f)

| Operatore | Vero quando |
|:---|:---|
| `and` | entrambi gli operandi sono veri |
| `or` | almeno uno è vero |
| `not` | l'operando è falso |

Tutti **PYT**.

| Valore | Vale come |
|:---|:---|
| `True`, `False` | i due letterali booleani |
| `0`, `""`, `[]`, `{}`, `None` | falsi in una condizione |
| qualsiasi altro | vero |

> Le condizioni si possono comporre: `if eta >= 18 and residenza == "Milano":`.
> `not (a and b)` equivale a `(not a) or (not b)` — De Morgan, materia di `L04_f`.

## 4. Selezione (L05)

| Costrutto | Scopo |
|:---|:---|
| `if condizione:` | Esegue il blocco se la condizione è vera |
| `else:` | Alternativa quando la condizione è falsa |
| `elif condizione:` | Selezione concatenata; si valuta solo se le precedenti sono false |
| `pass` | Istruzione che non fa nulla; tiene il posto di un blocco |

Tutti **PYT**.

> **L'indentazione è sintassi**, non stile: definisce quali istruzioni stanno dentro
> il blocco. Un'indentazione sbagliata è un programma diverso, non un programma
> brutto.
>
> Le condizioni si annidano (`if` dentro `if`), ma un `elif` è quasi sempre più
> leggibile di un `else` che contiene un altro `if`.

## 5. Iterazione (L06)

| Costrutto | Scopo |
|:---|:---|
| `while condizione:` | Ripete finché la condizione resta vera |
| `for elemento in sequenza:` | Ripete una volta per ogni elemento |
| `range(fine)` | Sequenza «0 … fine-1» |
| `range(inizio, fine)` | Da `inizio` a `fine-1` |
| `range(inizio, fine, passo)` | Con incremento `passo`, anche negativo |
| `break` | Esce immediatamente dal ciclo |
| `continue` | Salta al giro successivo |

Tutti **PYT**.

> **Il contatore.** Un `while` che deve girare *n* volte ha tre pezzi che devono
> esserci tutti: inizializzazione prima del ciclo, condizione, incremento dentro il
> corpo. Se manca l'incremento il ciclo è infinito — è l'errore di `L06`.
>
> **La sentinella.** Un ciclo che legge finché non arriva un valore d'arresto:
> si legge una prima volta prima del `while`, e si rilegge in fondo al corpo.
>
> **La trace table** — variabile per variabile, giro per giro — è lo strumento per
> capire un ciclo che non fa quello che dovrebbe. Materia di `L06`, e vale l'esame.

## 6. Stringhe (L07_b)

| Metodo | Scopo |
|:---|:---|
| `s.strip()` | Toglie spazi e a-capo agli estremi. `lstrip()`, `rstrip()` per un lato solo |
| `s.split(sep)` | Divide in lista di sottostringhe. Senza argomento divide sugli spazi |
| `sep.join(lista)` | Unisce una lista di stringhe usando `sep` come separatore |
| `s.replace(vecchio, nuovo)` | Sostituisce tutte le occorrenze |
| `s.count(sub)` | Quante volte compare `sub` |
| `s.find(sub)` | Posizione della prima occorrenza, `-1` se assente |
| `s.upper()` / `s.lower()` | Maiuscolo / minuscolo |

Tutti **PYT**.

| Operazione | Scopo |
|:---|:---|
| `s[i]` | Carattere in posizione `i`, da 0 |
| `s[i:j]` | Sottostringa da `i` a `j-1` |
| `s[i:]` `s[:j]` `s[-1]` | Dalla posizione in poi · fino a · ultimo carattere |
| `s1 + s2` | Concatenazione |
| `sub in s` | `True` se `sub` compare in `s` |

> **Le stringhe sono immutabili.** `s.upper()` non modifica `s`, restituisce una
> stringa nuova: va assegnata. Vale per tutti i metodi di questa tabella.

## 7. Liste e tuple (L07_c, L07_d)

| Metodo | Scopo |
|:---|:---|
| `l.append(x)` | Aggiunge `x` in fondo |
| `l.extend(altra)` | Aggiunge tutti gli elementi di un'altra lista |
| `l.insert(i, x)` | Inserisce in posizione `i` |
| `l.remove(x)` | Rimuove la prima occorrenza di `x` |
| `l.pop(i)` | Rimuove **e restituisce** l'elemento in posizione `i` |
| `l.sort()` | Ordina **sul posto**, non restituisce nulla |
| `l.count(x)` | Quante volte compare `x` |
| `l.index(x)` | Posizione della prima occorrenza |
| `l.copy()` | Copia superficiale |

Tutti **PYT**.

| Funzione | Scopo |
|:---|:---|
| `list(seq)` | Costruisce una lista da una sequenza |
| `sorted(seq)` | Restituisce una **nuova** lista ordinata, `reverse=True` per decrescente |
| `len(l)` | Numero di elementi |

> **`l.sort()` contro `sorted(l)`.** Il primo ordina la lista e restituisce `None`;
> il secondo lascia stare l'originale e restituisce una lista nuova.
> `l = l.sort()` è l'errore classico: assegna `None`.
>
> **Le tuple sono liste immutabili**: stessa indicizzazione e stesso `len()`, ma
> niente `append` né assegnamento a un elemento. Si usano quando i dati non devono
> cambiare, e come chiavi di dizionario.
>
> **Copia e riferimento.** `l2 = l1` non copia: dà un secondo nome alla stessa
> lista, e modificarla attraverso l'uno si vede anche dall'altro. Per una copia
> vera, `l1.copy()`. È materia di `L04_e` ed è il concetto che gli studenti
> sbagliano più a lungo.

## 8. Dizionari e iteratori (L07_e, L07_f)

| Costrutto | Scopo |
|:---|:---|
| `d[chiave]` | Valore associato; errore se la chiave non c'è |
| `d[chiave] = valore` | Inserisce o aggiorna |
| `d.get(chiave, default)` | Valore, oppure `default` se la chiave manca — non solleva errori |
| `d.keys()` | Le chiavi |
| `d.values()` | I valori |
| `d.items()` | Le coppie `(chiave, valore)` |
| `chiave in d` | `True` se la chiave esiste |
| `len(d)` | Numero di coppie |

Tutti **PYT**.

> **Iterare su un dizionario.** `for k in d:` scorre le **chiavi**;
> `for k, v in d.items():` scorre le coppie. Il secondo è il pattern per
> aggregare — contare, sommare per categoria — che è il cuore di metà degli
> esercizi PYT.
>
> **Il pattern dell'accumulatore:**
> ```python
> dConteggi = {}
> for elemento in lista:
>     if elemento in dConteggi:
>         dConteggi[elemento] = dConteggi[elemento] + 1
>     else:
>         dConteggi[elemento] = 1
> ```
> Da sapere a memoria. `d.get(elemento, 0) + 1` lo abbrevia.
>
> **Strutture annidate** (`L07_g`): liste di liste, dizionari di liste, liste di
> dizionari. `dati[i][j]` e `d[chiave][indice]`. È la forma in cui arrivano i dati
> caricati da file, quindi è materia d'esame.

## 9. Funzioni e moduli (L08)

| Costrutto | Scopo |
|:---|:---|
| `def nome(par1, par2):` | Definisce una funzione |
| `return valore` | Restituisce un risultato e termina la funzione |
| `return` senza valore, o assente | La funzione restituisce `None` |
| `nome(arg1, arg2)` | Chiamata |
| `def nome(par=valore):` | Parametro con valore di default |

Tutti **PYT**.

| Costrutto | Scopo |
|:---|:---|
| `import modulo` | Rende disponibile il modulo: si usa `modulo.funzione()` |
| `from modulo import funzione` | Importa un singolo nome, si usa senza prefisso |
| `import modulo as alias` | Importa con un nome breve — `import pandas as pd` |

| Modulo | Cosa se ne usa |
|:---|:---|
| `math` | `sqrt`, `floor`, `ceil`, `pi`, `log10`, `sin`, `cos`, `factorial` |
| `random` | `random()`, `randint(a, b)`, `choice(seq)`, `seed(n)` |
| `sys` | `argv`, `exit()` — solo accennato |

> **Parametri formali e attuali.** I nomi nella `def` sono formali, i valori nella
> chiamata sono attuali: sono cose diverse e la corrispondenza è posizionale.
>
> **Variabili locali.** Una variabile assegnata dentro una funzione vive solo lì.
> Modificare un parametro dentro la funzione non cambia la variabile del chiamante —
> **ma se il parametro è una lista, modificarne il contenuto sì**. È materia di
> `L08_b` ed è il punto più sottile del modulo.
>
> **Moduli e package** (`L08_a`): un modulo è un file `.py`, un package una cartella
> di moduli, il package manager (`pip`, `conda`) è ciò che li installa. Concetti,
> non esercizi.

## 10. File (L09)

| Costrutto | Scopo |
|:---|:---|
| `open(nome, "r")` | Apre in lettura |
| `open(nome, "w")` | Apre in scrittura, **azzerando** il file se esiste |
| `open(nome, "a")` | Apre in aggiunta in coda |
| `f.readline()` | Legge **una** riga, `""` a fine file |
| `f.readlines()` | Legge tutte le righe in una lista |
| `f.read()` | Legge tutto il contenuto in una stringa |
| `for riga in f:` | Scorre il file riga per riga |
| `f.write(stringa)` | Scrive; **non** aggiunge l'a-capo |
| `f.close()` | Chiude il file |

Tutti **PYT**.

> **Ogni riga letta finisce con `\n`**: `riga.strip()` prima di elaborarla, sempre.
> È l'errore numero uno negli esercizi sui file.
>
> **Il pattern di caricamento**, che è la domanda finale di quasi ogni tema PYT:
> ```python
> def caricaDati(fNameIn):
>     lDati = []
>     f = open(fNameIn, "r")
>     for riga in f:
>         riga = riga.strip()
>         if riga == "" or riga[0] == "#":
>             continue
>         lCampi = riga.split(";")
>         lDati.append([lCampi[0], int(lCampi[1])])
>     f.close()
>     return lDati
> ```
> Saltare righe vuote e commenti, dividere, convertire i tipi, accumulare.

## 11. Pandas (L10)

Import convenzionale: `import pandas as pd`.

### Caricare e salvare

| Funzione | Scopo | Argomenti principali |
|:---|:---|:---|
| `pd.read_csv(file)` | Legge un CSV | `sep=`, `delimiter=`, `header=`, `names=`, `index_col=`, `dtype=`, `skiprows=`, `decimal=`, `na_values=`, `encoding=`, `parse_dates=` |
| `pd.read_excel(file)` | Legge un foglio Excel | `sheet_name=` |
| `pd.read_json(file)` | Legge un JSON | — non richiesto all'esame |
| `df.to_csv(file)` | Salva su CSV | — |

`read_csv` e `read_excel` sono **FOD**.

> Il separatore non è sempre `,`: i file italiani usano spesso `;` con `,` come
> decimale, e allora servono `sep=";"` e `decimal=","`. Riconoscere il formato
> guardando il file **fa parte dell'esercizio** e non viene detto nel testo d'esame.

### Ispezionare

| Costrutto | Scopo |
|:---|:---|
| `df.head(n)` / `df.tail(n)` | Prime / ultime righe |
| `df.shape` | Tupla `(righe, colonne)` |
| `df.columns` / `df.index` | Nomi di colonne / indice |
| `df.dtypes` | Tipo di ogni colonna |
| `df.describe()` | Statistiche descrittive delle colonne numeriche |
| `df.info()` | Tipi, non-nulli e memoria, colonna per colonna |
| `df.sample(n)` | `n` righe casuali |

Tutti **FOD**.

### Selezionare

| Costrutto | Scopo |
|:---|:---|
| `df['colonna']` | Una colonna, come Series |
| `df[['c1', 'c2']]` | Più colonne, come DataFrame |
| `df.loc[righe, colonne]` | Selezione per **etichetta** |
| `df.iloc[righe, colonne]` | Selezione per **posizione** |
| `df[df['col'] > 10]` | Indicizzazione booleana |
| `df['col'].isin([...])` | `True` dove il valore è nell'elenco |

Tutti **FOD**.

> **Le condizioni si compongono con `&`, `|`, `~`**, non con `and`/`or`/`not`, e
> ogni pezzo va fra parentesi: `df[(df['a'] > 1) & (df['b'] == "x")]`.

### Colonne, valori mancanti, ordinamento

| Costrutto | Scopo |
|:---|:---|
| `df['nuova'] = df['a'] / df['b']` | Operazioni vettoriali fra colonne |
| `df['col'].astype(tipo)` | Conversione di tipo |
| `del df['col']` / `df.drop(columns=[...])` | Elimina colonne |
| `df.drop(index=[...])` | Elimina righe |
| `df.isnull()` / `df.notnull()` / `df.notna()` | Maschere per i valori mancanti |
| `df.dropna()` | Elimina le righe con valori mancanti — `subset=`, `how=` |
| `df.sort_values('col')` | Ordina per colonna — `ascending=` |
| `df.drop_duplicates()` | Elimina righe duplicate |
| `df.set_index('col')` / `df.reset_index()` | Imposta / azzera l'indice |
| `df.sort_index()` | Ordina per indice |

Tutti **FOD**.

### Aggregare e raggruppare

| Costrutto | Scopo |
|:---|:---|
| `.min()` `.max()` `.sum()` `.mean()` `.median()` `.std()` `.var()` | Statistiche su colonna o DataFrame |
| `.count()` | Numero di valori non nulli |
| `.size()` | Numero di elementi, nulli compresi |
| `.idxmax()` / `.idxmin()` | **Etichetta** della riga col valore massimo / minimo |
| `.unique()` | Valori distinti |
| `df.groupby('col')` | Raggruppa; si combina con le funzioni sopra |
| `df.groupby(['c1', 'c2'])` | Raggruppamento su più chiavi |
| `.get_group(valore)` | Estrae un singolo gruppo |
| `groupby(..., as_index=False)` | Lascia la chiave come colonna invece che come indice |

Tutti **FOD**.

> `.idxmax()` dà **l'etichetta**, non il valore: `df['col'].max()` dà quanto,
> `df['col'].idxmax()` dà chi. Le domande d'esame chiedono quasi sempre il secondo.

### Combinare più DataFrame

| Costrutto | Scopo |
|:---|:---|
| `pd.merge(df1, df2, on='chiave')` | Fusione su colonna comune |
| `pd.merge(..., left_on=, right_on=)` | Chiavi con nomi diversi |
| `pd.merge(..., how='inner'/'left'/'outer')` | Tipo di giunzione |
| `pd.concat([df1, df2])` | Concatenazione — `axis=0` righe, `axis=1` colonne |

Tutti **FOD**.

### Insegnato ma non chiesto all'esame

`pivot_table`, `apply`, `pd.Series(...)` e `pd.DataFrame(...)` come costruttori,
`melt`, `stack`/`unstack`, `.diff()`, `.div(axis=)`. Servono a capire cosa sa fare
la libreria; non compaiono nei temi.

## 12. Matplotlib (L11)

Import convenzionale: `import matplotlib.pyplot as plt`.

| Costrutto | Scopo |
|:---|:---|
| `plt.figure()` | Crea una figura — `figsize=(l, h)` |
| `fig.add_subplot(r, c, n)` | Aggiunge un sistema di assi |
| `plt.subplot(r, c, n)` | Forma abbreviata |
| `ax.plot(x, y)` | Linea — `color=`, `label=`, `linestyle=`, `marker=` |
| `ax.bar(x, h)` / `ax.barh(y, l)` | Barre verticali / orizzontali |
| `ax.scatter(x, y)` | Dispersione — `s=` per la dimensione (bubble plot) |
| `ax.hist(dati, bins=)` | Istogramma |
| `ax.boxplot(dati, tick_labels=)` | Box plot |
| `ax.set_title(...)` | Titolo |
| `ax.set_xlabel(...)` / `ax.set_ylabel(...)` | Etichette degli assi |
| `ax.set_xlim(a, b)` / `ax.set_ylim(a, b)` | Limiti degli assi |
| `ax.legend()` | Legenda — richiede `label=` nelle chiamate di disegno |
| `plt.tight_layout()` | Sistema i margini perché le etichette non si taglino |
| `plt.savefig(nome)` | Salva su file — il formato segue l'estensione |

Tutti **FOD**.

> **Un grafico d'esame senza titolo ed etichette degli assi è incompleto**, anche
> se i dati sono giusti.
>
> Insegnati ma non richiesti: `ax.violinplot`, `ax.pie`, `ax.errorbar`,
> `ax.fill_between`, `fig.add_axes`, la manipolazione delle `spines`.

---

## 13. Divergenze da sanare

Costruire questo documento significava mettere a confronto due elenchi che non si
erano mai guardati in faccia. Non coincidono.

### Chiesto all'esame, mai insegnato

Ricerca su tutto il materiale didattico FOD — i quattro notebook «Lezione11a–d», il
deck `L10a`, `Lezione12Matplotlib`, le esercitazioni E05 ed E06 — contro le
soluzioni d'esame:

| Costrutto | Temi che lo usano | Insegnato prima | Ora coperto da |
|:---|:--:|:---|:---|
| `.info()` | **15** | da nessuna parte | `L10_a_PandasLetturaDati.md` |
| `.sort_values()` | **10** | da nessuna parte | `L10_c_PandasUnDataFrame.md` §1 |
| `.std()` | **9** | solo come riga di `describe()` | `L10_c_PandasUnDataFrame.md` §4 |
| `.drop()` | **6** | solo in `Esercitazioni/` | `L10_c_PandasUnDataFrame.md` §3 |
| `.isin()` | **5** | da nessuna parte | `L10_c_PandasUnDataFrame.md` §2 |
| `plt.tight_layout()` | **3** | da nessuna parte | `L11_a_Matplotlib.md` |

**Colmato il 07/09/2026.** I sei costrutti hanno ora una sezione ciascuno nel
markdown pre-lezione della loro lezione, con esempi che girano su
`03_FocusOnData/data/MeteoMilano2011.csv` — lo stesso dataset dei notebook
esistenti, così il materiale nuovo si innesta su quello vecchio invece di
affiancarlo. Ogni blocco di codice è stato eseguito prima di essere scritto qui.

Restano file **parziali**: coprono il buco, non l'intera lezione. Il resto di `L10`
e `L11` va ancora riportato dai notebook del 2023.

`.info()` era il caso più serio: la progressione tipica delle domande FOD descritta
in `temiEsame/CLAUDE.md` la mette al primo quesito — *"display `.head()`,
`.info()`, `.shape`"* — e quindici temi la usano, ma nessuna lezione la mostrava.

Sono elencate come materia d'esame perché è la situazione di fatto e i temi
esistenti non si riscrivono. Il debito stava dalla parte delle lezioni, ed è lì che
è stato pagato.

### Ammesso all'esame ma mai usato

`.notna()`, `.median()`, `.var()` sono nell'elenco delle API ammesse di
`temiEsame/CLAUDE.md` e non compaiono in nessuna soluzione. Innocuo: restano
ammesse, e ora sono anche documentate qui.

### Insegnato e mai chiesto

`read_json`, `pivot_table`, `apply`, i costruttori `pd.Series`/`pd.DataFrame`,
`fill_between`, `violinplot`, `pie`, `errorbar`, `add_axes`, `unique`,
`intersection`, `to_csv`. Nessun problema — è la categoria "si insegna per capire",
purché resti dichiarata.

### Da aggiornare di conseguenza

- **`temiEsame/CLAUDE.md`** — le sezioni «Allowed — pandas» e «Allowed — matplotlib»
  vanno sostituite da un rimando a questo file, così la lista è una sola. Il
  riferimento "derivato da Lezione11a–d e Lezione12" va riscritto: con la
  numerazione nuova quei numeri esistono ancora ma indicano file diversi.
- **`info@Stat202526.md`** — descrive FOD in tre parti includendo `sys`/`os`, che non
  è mai stato materia d'esame in 113 temi.
