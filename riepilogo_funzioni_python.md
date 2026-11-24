# Riepilogo generale delle funzioni Python — Informatica@SGI

Le funzioni e i costrutti Python visti nel corso, nell'ordine delle lezioni: una guida per lo studio.

---

## Indice

0. [Convenzioni del corso](#0-convenzioni-del-corso)
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

---

## 0. Convenzioni del corso

**`break` e `continue` esistono, ma nel corso non si usano**: un ciclo finisce quando la sua condizione diventa falsa, e chi legge il codice deve trovare il motivo dell'uscita lì, non in mezzo al corpo.

---

## 1. Input, output e conversioni (L04)

| Funzione | Scopo | Note |
|:---|:---|:--- |
| `print(...)` | Stampa a video | separatore `sep=`, terminatore `end=` |
| `print(..., file=, flush=)` | Stampa su un file aperto, svuota subito il buffer | mostrati in `L08_aula` |
| `input(prompt)` | Legge una riga da tastiera, **sempre come stringa** |  |
| `int(x)` | Converte in intero; su stringa non numerica solleva errore |  |
| `float(x)` | Converte in numero con virgola |  |
| `str(x)` | Converte in stringa |  |
| `bool(x)` | Converte in booleano: `False` per `0`, `""`, `[]`, `{}`, `None` (`L04_f`) |  |
| `type(x)` | Tipo dell'oggetto |  |
| `id(x)` | Identità dell'oggetto in memoria | serve a spiegare l'assegnamento |
| `dir(x)` | I nomi disponibili su un oggetto | `L04_e` |
| `repr(x)` | La stringa com'è scritta nel codice, apici e `\n` compresi | `L09_aula`, per vedere a-capo e spazi in una riga letta |

> `input()` restituisce **sempre** una stringa: `int(input(...))` è il pattern per leggere un numero. È l'errore più frequente nei primi esercizi.

**Due modi di formattare**.

| forma | esempio | dove si insegna |
|:---|:---|:--- |
| f-string | `print(f"media: {media:.2f}")` | `L04_c`, in coda — **non è nel video** |
| con `%` | `print("media: %f" % media)` | `L04_c`, e il video la mostra |

Della forma con `%`: `%d` intero, `%f` float, `%s` stringa, `%r` la rappresentazione di `repr()`, con gli apici, e `\t` `\n` per tabulazione e a capo. Delle f-string si usano l'interpolazione `{nome}` e lo specificatore dei decimali, `{nome:.2f}` o `{nome:.1f}`.

> Esiste anche una terza forma, `.format()`: nel corso usiamo le due qui sopra.

> `eval(input(...))` compare in coda a `L04_c` perché è nel video, ma **non è il pattern del corso**: la conversione si scrive esplicita, `int(input(...))` o `float(input(...))`. Il frame che segue lo dice.

## 2. Operatori ed espressioni (L04)

| Operatore | Scopo |
|:---|:--- |
| `+` `-` `*` `/` | Aritmetica. `/` dà sempre un `float`, anche fra interi |
| `//` | Divisione intera |
| `%` | Resto |
| `**` | Potenza |
| `==` `!=` `<` `<=` `>` `>=` | Confronto, restituiscono `True`/`False` |
| `a <= x < b` | Confronto concatenato: vale `a <= x and x < b` (`L04_aula`) |
| `=` `+=` `-=` `*=` `/=` `%=` | Assegnamento |

| Funzione | Scopo | Note |
|:---|:---|:--- |
| `abs(x)` | Valore assoluto |  |
| `round(x, n)` | Arrotondamento |  |
| `min(...)` `max(...)` | Minimo, massimo — su più argomenti o su una sequenza |  |
| `sum(seq)` | Somma degli elementi |  |
| `len(x)` | Lunghezza di stringa, lista, tupla, dizionario |  |
| `pow(x, y)` | Potenza, come `x ** y` | `L08_a`, esempio di funzione predefinita |
| `bin(n)` `hex(n)` | Il numero scritto in base 2, in base 16 | `L08_esercizi`, per controllare le conversioni di base |

> **La precedenza degli operatori** è materia di `L04_d`: `2 + 3 * 4` fa 14, non 20. In caso di dubbio, parentesi.

## 3. Logica booleana (L04_f)

| Operatore | Vero quando |
|:---|:--- |
| `and` | entrambi gli operandi sono veri |
| `or` | almeno uno è vero |
| `not` | l'operando è falso |

| Valore | Vale come |
|:---|:--- |
| `True`, `False` | i due letterali booleani |
| `0`, `""`, `[]`, `{}`, `None` | falsi in una condizione |
| qualsiasi altro | vero |

| Operatore | Vero quando | |
|:---|:---|:--- |
| `x is None` | `x` è proprio `None` | `L08_aula`: il modo di chiedere se una funzione ha restituito qualcosa |
| `x is not None` | `x` non è `None` |  |

> Le condizioni si possono comporre: `if eta >= 18 and residenza == "Milano":`. `not (a and b)` equivale a `(not a) or (not b)` — De Morgan, materia di `L04_f`.

## 4. Selezione (L05)

| Costrutto | Scopo |
|:---|:--- |
| `if condizione:` | Esegue il blocco se la condizione è vera |
| `else:` | Alternativa quando la condizione è falsa |
| `elif condizione:` | Selezione concatenata; si valuta solo se le precedenti sono false |
| `pass` | Istruzione che non fa nulla; tiene il posto di un blocco |

> **L'indentazione è sintassi**, non stile: definisce quali istruzioni stanno dentro il blocco. Un'indentazione sbagliata è un programma diverso, non un programma brutto.
>
> Le condizioni si annidano (`if` dentro `if`), ma un `elif` è quasi sempre più leggibile di un `else` che contiene un altro `if`.

## 5. Iterazione (L06)

| Costrutto | Scopo |
|:---|:--- |
| `while condizione:` | Ripete finché la condizione resta vera |
| `for elemento in sequenza:` | Ripete una volta per ogni elemento |
| `range(fine)` | Sequenza «0 … fine-1» |
| `range(inizio, fine)` | Da `inizio` a `fine-1` |
| `range(inizio, fine, passo)` | Con incremento `passo`, anche negativo |

> **Uscire prima dal ciclo, senza `break`.** Il motivo dell'uscita va nella condizione, con una variabile di controllo:
> ```python
> trovato = False
> i = 0
> while i < len(lista) and not trovato:
>     if lista[i] == cercato:
>         trovato = True
>     i = i + 1
> ```
> E invece di `continue` si mette dentro un `if` la parte del corpo che va eseguita.
>
> **Il contatore.** Un `while` che deve girare *n* volte ha tre pezzi che devono esserci tutti: inizializzazione prima del ciclo, condizione, incremento dentro il corpo. Se manca l'incremento il ciclo è infinito — è l'errore di `L06`.
>
> **La sentinella.** Un ciclo che legge finché non arriva un valore d'arresto: si legge una prima volta prima del `while`, e si rilegge in fondo al corpo.
>
> **La trace table** — variabile per variabile, giro per giro — è lo strumento per capire un ciclo che non fa quello che dovrebbe. Materia di `L06`.

## 6. Stringhe (L07_b)

| Metodo | Scopo |
|:---|:--- |
| `s.strip()` | Toglie spazi e a-capo agli estremi |
| `s.rstrip()` | Lo stesso, solo a destra |
| `s.split(sep)` | Divide in lista di sottostringhe. Senza argomento divide sugli spazi |
| `sep.join(lista)` | Unisce una lista di stringhe usando `sep` come separatore |
| `s.replace(vecchio, nuovo)` | Sostituisce tutte le occorrenze |
| `s.count(sub)` | Quante volte compare `sub` |
| `s.find(sub)` | Posizione della prima occorrenza, `-1` se assente |
| `s.upper()` | Maiuscolo |
| `s.lower()` | Minuscolo |
| `s.lstrip()` | Toglie spazi e a-capo solo a sinistra |
| `s.startswith(pre)` / `s.endswith(suf)` | `True` se `s` comincia con `pre`, finisce con `suf` |

| Operazione | Scopo |
|:---|:--- |
| `s[i]` | Carattere in posizione `i`, da 0 |
| `s[i:j]` | Sottostringa da `i` a `j-1` |
| `s[i:]` `s[:j]` `s[-1]` | Dalla posizione in poi · fino a · ultimo carattere |
| `s[i:j:k]` `s[::-1]` | Con passo `k` · la stringa al contrario |
| `s1 + s2` | Concatenazione |
| `sub in s` / `sub not in s` | `True` se `sub` compare / non compare in `s` |

> **Le stringhe sono immutabili.** `s.upper()` non modifica `s`, restituisce una stringa nuova: va assegnata. Vale per tutti i metodi di questa tabella.

## 7. Liste e tuple (L07_c, L07_d)

| Metodo | Scopo |
|:---|:--- |
| `l.append(x)` | Aggiunge `x` in fondo |
| `l.extend(altra)` | Aggiunge tutti gli elementi di un'altra lista |
| `l.insert(i, x)` | Inserisce in posizione `i` |
| `l.remove(x)` | Rimuove la prima occorrenza di `x` |
| `l.pop(i)` | Rimuove **e restituisce** l'elemento in posizione `i` |
| `l.sort()` | Ordina **sul posto**, non restituisce nulla |
| `l.count(x)` | Quante volte compare `x` |
| `l.index(x)` | Posizione della prima occorrenza |
| `l.copy()` | Copia superficiale |
| `del l[i]` | Toglie l'elemento in posizione `i`; `del d[chiave]` toglie una chiave |

| Funzione | Scopo |
|:---|:--- |
| `list(seq)` | Costruisce una lista da una sequenza |
| `sorted(seq)` | Restituisce una **nuova** lista ordinata, `reverse=True` per decrescente |
| `len(l)` | Numero di elementi |
| `a, b = t` | Spacchettamento: un nome per ogni elemento della tupla o della lista (`L04_aula`, `L07`) |
| `x not in l` | `True` se `x` non compare in `l` |
| `tuple(seq)` | Costruisce una tupla da una sequenza — in `L07_riepilogo` |
| `l.reverse()`, `l.sort(reverse=True)` | Rovescia la lista sul posto · ordina in modo decrescente sul posto — in `L07_riepilogo` |

> **`l.sort()` contro `sorted(l)`.** Il primo ordina la lista e restituisce `None`; il secondo lascia stare l'originale e restituisce una lista nuova. `l = l.sort()` è l'errore classico: assegna `None`.
>
> **Le tuple sono liste immutabili**: stessa indicizzazione e stesso `len()`, ma niente `append` né assegnamento a un elemento. Si usano quando i dati non devono cambiare, e come chiavi di dizionario.
>
> **Copia e riferimento.** `l2 = l1` non copia: dà un secondo nome alla stessa lista, e modificarla attraverso l'uno si vede anche dall'altro. Per una copia vera serve `l1.copy()`, che però si vede solo in `focus_StruttureDati`. Il concetto è materia di `L04_e` ed è quello che gli studenti sbagliano più a lungo.

## 8. Dizionari e iteratori (L07_e, L07_f)

| Costrutto | Scopo |
|:---|:--- |
| `d[chiave]` | Valore associato; errore se la chiave non c'è |
| `d[chiave] = valore` | Inserisce o aggiorna |
| `d.get(chiave, default)` | Valore, oppure `default` se la chiave manca — non solleva errori |
| `d.keys()` | Le chiavi |
| `d.values()` | I valori |
| `d.items()` | Le coppie `(chiave, valore)` |
| `chiave in d` / `chiave not in d` | `True` se la chiave esiste / non esiste |
| `len(d)` | Numero di coppie |

| Funzione | Scopo | |
|:---|:---|:--- |
| `zip(x, y)` | Le coppie degli elementi nella stessa posizione; **si ferma alla più corta**, senza avvisare | `L07_aula` |
| `dict(zip(chiavi, valori))` | Un dizionario da due liste parallele | `L07_aula` |
| `enumerate(x)` | Le coppie `(indice, elemento)` | `L07_aula` |

> **Iterare su un dizionario.** `for k in d:` scorre le **chiavi**; `for k, v in d.items():` scorre le coppie. Il secondo è il pattern per aggregare — contare, sommare per categoria — che è il cuore di metà degli esercizi PYT.
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
> **Strutture annidate** (`L07_g`): liste di liste, dizionari di liste, liste di dizionari. `dati[i][j]` e `d[chiave][indice]`. È la forma in cui arrivano i dati caricati da file.

## 9. Funzioni e moduli (L08)

| Costrutto | Scopo |
|:---|:--- |
| `def nome(par1, par2):` | Definisce una funzione |
| `return valore` | Restituisce un risultato e termina la funzione |
| `return` senza valore, o assente | La funzione restituisce `None` |
| `nome(arg1, arg2)` | Chiamata |
| `def nome(par=valore):` | Parametro con valore di default |
| `nome(par=valore)` | Argomento passato per nome, in qualsiasi ordine |
| `def nome(*valori)` / `def nome(**misure)` | Un numero variabile di argomenti, per posizione / per nome (`L08_aula`) |

| Costrutto | Scopo |
|:---|:--- |
| `import modulo` | Rende disponibile il modulo: si usa `modulo.funzione()` |
| `from modulo import funzione` | Importa un singolo nome, si usa senza prefisso |
| `import modulo as alias` | Importa con un nome breve — `import pandas as pd` |

| Modulo | Cosa se ne usa |
|:---|:--- |
| `math` | `sqrt`, `floor`, `ceil`, `log10`, `sin`, `factorial` (`L08_a`) |
| `numpy` | `np.random.randint(a, b)`, con `b` escluso, e `np.random.choice(seq, p=...)` (`L06_oca`): per i numeri casuali il corso usa numpy, mai `random` |
| `sys` | `argv` (`L02`, lanciare uno script con un argomento), `path` (`L08_a`) |

> **Parametri formali e attuali.** I nomi nella `def` sono formali, i valori nella chiamata sono attuali: sono cose diverse e la corrispondenza è posizionale.
>
> **Variabili locali.** Una variabile assegnata dentro una funzione vive solo lì. Modificare un parametro dentro la funzione non cambia la variabile del chiamante — **ma se il parametro è una lista, modificarne il contenuto sì**. È materia di `L08_b` ed è il punto più sottile del modulo.
>
> **Moduli e package** (`L08_a`): un modulo è un file `.py`, un package una cartella di moduli, il package manager (`pip`, `conda`) è ciò che li installa. Concetti, non esercizi.

## 10. File (L09)

| Costrutto | Scopo |
|:---|:--- |
| `with open(nome, "r", encoding="utf-8") as f:` | Apre il file e lo chiude da solo alla fine del blocco: è la forma degli esercizi di `L09` e delle esercitazioni |
| `open(nome, "r")` | Apre in lettura |
| `open(nome, "w")` | Apre in scrittura, **azzerando** il file se esiste |
| `open(nome, "a")` | Apre in aggiunta in coda |
| `f.readline()` | Legge **una** riga, `""` a fine file |
| `f.readlines()` | Legge tutte le righe in una lista |
| `f.read()` | Legge tutto il contenuto in una stringa |
| `for riga in f:` | Scorre il file riga per riga |
| `f.write(stringa)` | Scrive; **non** aggiunge l'a-capo |
| `f.close()` | Chiude il file; con `with` non serve |

| Costrutto | Scopo | |
|:---|:---|:--- |
| `f.tell()` / `f.seek(pos)` | Dove si trova la lettura / spostarla | `L09_a` |
| `pl.Path(...)`, `.home()`, `.glob()`, `.exists()`, `.read_text()` | `pathlib`, con `import pathlib as pl`: percorsi e file | `L09_aula`, `E04` |
| `s.encode()` | La stringa come byte | `L09_aula`, per spiegare le codifiche |

> **Ogni riga letta finisce con `\n`**: `riga.strip()` prima di elaborarla, sempre. È l'errore numero uno negli esercizi sui file.

## 11. Pandas (L10)

Import convenzionale: `import pandas as pd`.

### Caricare e salvare

| Funzione | Scopo | Argomenti principali |
|:---|:---|:--- |
| `pd.read_csv(file)` | Legge un CSV | `sep=`, `delimiter=`, `header=`, `names=`, `index_col=`, `dtype=`, `skiprows=`, `decimal=`, `na_values=`, `encoding=`, `parse_dates=` |
| `pd.read_excel(file)` | Legge un foglio Excel | `sheet_name=` |
| `pd.read_json(file)` | Legge un JSON |  |
| `df.to_csv(file)` | Salva su CSV |  |

> Il separatore non è sempre `,`: i file italiani usano spesso `;` con `,` come decimale, e allora servono `sep=";"` e `decimal=","`. Riconoscere il formato guardando il file **fa parte dell'esercizio**.

### Ispezionare

| Costrutto | Scopo |
|:---|:--- |
| `df.head(n)` / `df.tail(n)` | Prime / ultime righe |
| `df.shape` | Tupla `(righe, colonne)` |
| `df.columns` / `df.index` | Nomi di colonne / indice |
| `df.dtypes` | Tipo di ogni colonna |
| `df.describe()` | Statistiche descrittive delle colonne numeriche |
| `df.info()` | Tipi, non-nulli e memoria, colonna per colonna |
| `df.sample(n)` | `n` righe casuali |

### Selezionare

| Costrutto | Scopo |
|:---|:--- |
| `df['colonna']` | Una colonna, come Series |
| `df[['c1', 'c2']]` | Più colonne, come DataFrame |
| `df.loc[righe, colonne]` | Selezione per **etichetta** |
| `df.iloc[righe, colonne]` | Selezione per **posizione** |
| `df[df['col'] > 10]` | Indicizzazione booleana |
| `df['col'].isin([...])` | `True` dove il valore è nell'elenco |

> **Le condizioni si compongono con `&`, `|`, `~`**, non con `and`/`or`/`not`, e ogni pezzo va fra parentesi: `df[(df['a'] > 1) & (df['b'] == "x")]`.

### Colonne, valori mancanti, ordinamento

| Costrutto | Scopo |
|:---|:--- |
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

### Aggregare e raggruppare

| Costrutto | Scopo |
|:---|:--- |
| `.min()` `.max()` `.sum()` `.mean()` `.median()` `.std()` `.var()` | Statistiche su colonna o DataFrame |
| `.count()` | Numero di valori non nulli |
| `.size()` | Numero di elementi, nulli compresi |
| `.idxmax()` / `.idxmin()` | **Etichetta** della riga col valore massimo / minimo |
| `.unique()` | Valori distinti |
| `df.groupby('col')` | Raggruppa; si combina con le funzioni sopra |
| `df.groupby(['c1', 'c2'])` | Raggruppamento su più chiavi |
| `.get_group(valore)` | Estrae un singolo gruppo |
| `groupby(..., as_index=False)` | Lascia la chiave come colonna invece che come indice |

> `.idxmax()` dà **l'etichetta**, non il valore: `df['col'].max()` dà quanto, `df['col'].idxmax()` dà chi.

### Combinare più DataFrame

| Costrutto | Scopo |
|:---|:--- |
| `pd.merge(df1, df2, on='chiave')` | Fusione su colonna comune |
| `pd.merge(..., left_on=, right_on=)` | Chiavi con nomi diversi |
| `pd.merge(..., how='inner'/'left'/'outer')` | Tipo di giunzione |
| `pd.concat([df1, df2])` | Concatenazione — `axis=0` righe, `axis=1` colonne |

### Si vede anche

`pivot_table`, `apply`, `pd.Series(...)` e `pd.DataFrame(...)` come costruttori, `melt`, `stack`/`unstack`, `.diff()`, `.div(axis=)`. Servono a capire cosa sa fare la libreria.

## 12. Matplotlib (L11)

Import convenzionale: `import matplotlib.pyplot as plt`.

| Costrutto | Scopo |
|:---|:--- |
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

> **Un grafico senza titolo ed etichette degli assi è incompleto**, anche se i dati sono giusti.
>
> Si vedono anche: `ax.violinplot`, `ax.pie`, `ax.errorbar`, `ax.fill_between`, `fig.add_axes`, la manipolazione delle `spines`.

