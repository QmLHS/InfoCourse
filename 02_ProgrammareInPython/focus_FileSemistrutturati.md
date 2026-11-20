# Focus — Caricare un file semistrutturato

> **Materiale facoltativo.** Non è materia d'esame. È per chi, finita `L09`, vuole un metodo per caricare un file che non ha mai visto, invece di una ricetta per ciascun file del corso.

Si dà per saputo `L09`, con i suoi esercizi: aprire e leggere un file, `strip` e `split`, i dizionari di `L07`. Il focus ha cinque parti:

- **I. Il metodo**: guardare il file, trovarne le regolarità, riconoscere i tipi di riga, scegliere la struttura, verificare;
- **II. Le forme del corso**: i file di `L09`, riletti con il metodo;
- **III. Forme nuove e file complessi**: sezioni, TOML, sequenze, log, CSV con le virgolette, righe sporche, JSON;
- **IV. La cassetta degli attrezzi**: le funzioni e i moduli che aiutano;
- **V. Python puro o pandas**: quando conviene l'uno e quando l'altro.

Ogni esempio è eseguito con Python 3.12, la versione della VM, e 3.14.

> **L'idea, in una riga.** Un file semistrutturato non ha una struttura dichiarata, ma ha delle **regolarità**: righe che si somigliano, caratteri che stanno sempre allo stesso posto, parole che aprono e chiudono. Caricarlo vuol dire trovarle, e scrivere una regola per ciascuna.

---

# Parte I — Il metodo

## 1. Guardare il file, prima di scrivere codice

Il codice si scrive **dopo** aver guardato il file, con gli strumenti della shell di `L02`:

| Comando | Che cosa dice |
|---|---|
| `head -20 file`, `tail -20 file` | come comincia e come finisce: intestazioni, commenti, righe vuote, una riga finale incompleta |
| `wc -l file` | quante righe: il primo conto, con cui confrontare il caricamento |
| `grep -c "^PMID" file` | quante righe cominciano in un certo modo: quanti record, quanti commenti |
| `cat -A file` | i caratteri invisibili, meglio sulle prime righe con `head`: `$` a fine riga, `^I` per il tab, `^M` per il `\r` di Windows |

`cat -A` su `MeteoMilano2011.csv` mostra subito tre cose che il codice dovrà sapere:

```
$
CET,Temperatura maxC,Temperatura mediaC,Temperatura minC,Punto di rugiadaC,...
2011-1-1,6,1,-4,1,-1,-4,100,88,66,1022,1018,1015,8,5,1,8,2,,0.00,6,,225<br />$
```

La prima riga è **vuota**, la seconda è l'intestazione, e ogni riga di dati finisce con `<br />`, un resto di pagina web. Nessuna delle tre si vede aprendo il file con un foglio di calcolo, e tutte e tre romperebbero un caricamento scritto a occhio.

## 2. Le regolarità: che tipi di riga ci sono

Guardando il file, si fa l'elenco dei **tipi di riga** che si incontrano. Sono quasi sempre questi:

| Tipo di riga | Come si riconosce, di solito |
|---|---|
| **vuota** | `riga.strip() == ""` |
| **commento** | comincia con un carattere fisso: `riga.startswith("#")`, o `;` |
| **intestazione di colonne** | è la prima, o la prima dopo i commenti: si salta con un `readline` |
| **intestazione di gruppo** | contiene una parola fissa, o comincia con un segno: `"Categoria" in riga`, `riga.startswith(">")`, `riga.startswith("[")` |
| **riga di separazione** | fatta di un carattere ripetuto: `riga.startswith("-")` |
| **dato** | il caso normale: si spezza e si converte |
| **etichetta e valore** | l'etichetta sta in una posizione fissa: `riga[:4].strip()` |
| **continuazione** | non ha etichetta, e prosegue il valore della riga prima: `riga[:4].strip() == ""` |

Per ogni tipo servono due cose: **una regola che lo riconosca**, e **un'azione** da fare quando lo si incontra. La regola deve essere vera per tutte le righe di quel tipo, e falsa per tutte le altre: per questo si guardano anche le righe strane, non solo le prime.

## 3. Classificare e contare, prima di caricare

Prima di scrivere il caricamento, conviene scrivere **solo la classificazione**, e contare le righe per tipo. Sul file del nuoto:

```python
def tipoNuoto(riga):
    if riga.strip() == "":
        return "vuota"
    if riga.startswith("-"):
        return "separatore"
    if "Categoria" in riga:
        return "intestazione"
    if riga[:10].strip() == "":
        return "senza posizione"
    return "prestazione"


conteggio = {}
with open(percorso, encoding="utf-8") as f:
    for riga in f:
        tipo = tipoNuoto(riga)
        if tipo in conteggio:
            conteggio[tipo] = conteggio[tipo] + 1
        else:
            conteggio[tipo] = 1
print(conteggio)
```

```
{'intestazione': 171, 'separatore': 171, 'prestazione': 859, 'vuota': 171, 'senza posizione': 13}
```

**I conti si confrontano con `grep -c`**: 171 righe con `Categoria`, 171 che cominciano con `-`, 171 vuote. Tornano. Le 13 righe senza posizione sono la sorpresa: 10 squalificati e 3 pari merito. Senza questo passo, sarebbero state scoperte solo quando il caricamento si rompeva su `int("")`.

**Se ogni riga ha un tipo, e i conti tornano, il caricamento è quasi scritto**: resta da decidere che cosa fare per ciascun tipo.

## 4. Lo schema del ciclo

Il caricamento di un file semistrutturato ha quasi sempre questa forma:

```python
struttura = {}
corrente = None
with open(percorso, encoding="utf-8") as f:
    for riga in f:
        if ...:            # regola del tipo 1
            ...            # azione del tipo 1
        elif ...:          # regola del tipo 2
            ...
        else:              # il caso normale: un dato
            ...
```

Tre decisioni, che vanno prese **prima** di scrivere:

- **L'ordine delle regole.** Le regole si provano dalla più specifica alla più generale, e il dato normale va per ultimo, nell'`else`. Nel nuoto, «senza posizione» si controlla dopo «vuota»: anche una riga vuota ha i primi 10 caratteri vuoti.
- **Lo stato che sopravvive da una riga all'altra.** Una variabile creata **fuori** dal ciclo, come `corrente`, ricorda qualcosa delle righe già lette: la gara di cui si stanno leggendo le prestazioni, la pubblicazione che si sta riempiendo. Le intestazioni la cambiano, le righe di dati la usano.
- **Quando un record è finito.** Se un record occupa più righe, bisogna decidere quando metterlo nella struttura. **Alla riga che lo chiude**, una riga vuota, è naturale, ma l'ultimo record si perde se il file non finisce con quella riga: è la trappola di PubMed in aula. **Alla riga che lo apre**, mettendolo nella struttura subito e riempiendolo dopo, non si perde niente.

## 5. La struttura viene dalla domanda

Lo stesso file si carica in strutture diverse, a seconda di che cosa si vuole sapere. Il nuoto per gara risponde a «chi ha vinto i 400 stile?»; per atleta, a «che gare ha fatto?». **Si sceglie la struttura in cui la risposta è una chiave sola**: se la domanda comincia con «per ogni gara», la chiave è la gara.

| Domanda | Struttura |
|---|---|
| una riga, un fatto | lista di tuple, o di dizionari |
| ritrovare un record dal suo codice | dizionario: a ogni codice il suo record |
| contare per categoria | dizionario: a ogni categoria un numero |
| raggruppare | dizionario: a ogni gruppo una lista di record |
| un campo che si ripete | una lista dentro il record |

## 6. Verificare: il conto

Un caricamento sbagliato **non dà quasi mai errore**: perde una riga, ne conta una due volte, mette un valore nel campo sbagliato. Per questo ogni caricamento finisce con **un conto fatto per un'altra strada**:

- il numero di record contro `grep -c` della riga che li apre;
- il numero di righe di dati contro `wc -l`, meno intestazioni e commenti;
- due strutture diverse dello stesso file che devono dare lo stesso totale: le 872 prestazioni del nuoto, per gara e per atleta;
- un record a caso, stampato e confrontato a occhio con il file.

---

# Parte II — Le forme del corso

I file di `L09_esercizi.md` e dell'aula, riletti con il metodo. Il codice completo è negli esercizi; qui ci sono le regolarità.

## Con separatore: CSV e TSV

**Regolarità**: ogni riga è un record, i campi sono separati da un carattere fisso. **Tipi di riga**: intestazione, commenti, dati.

- `MeteoMilano2011.csv`: una riga vuota e l'intestazione da saltare, la virgola, il `<br />` in fondo, e **campi vuoti** per i giorni senza misura;
- `telefonate.csv`: il `;`, le righe `#` da scartare, e **un separatore dentro un campo**, `giorno:ora:minuto`, che vuole un secondo `split`;
- `itemsFOD.tsv`: il tab, scelto perché le descrizioni contengono virgole.

Il numero di campi è una regolarità da controllare: in `MeteoMilano2011.csv` tutte le 366 righe non vuote ne hanno 23. Una riga con un numero diverso è un problema, e conviene scoprirlo con un conto, non con un `IndexError`.

## A colonne fisse

**Regolarità**: ogni campo sta **sempre negli stessi caratteri**, e i campi sono allineati con spazi. `split()` non funziona, perché i nomi hanno quante parole vogliono: 7 pezzi su una riga del nuoto, 10 su un'altra. Si usa lo **slicing**, `riga[10:42]`, e poi `strip()`.

Le posizioni si trovano guardando il file con un righello: in un editor, la colonna del cursore; oppure stampando `riga.find("1990")` sulla riga di un atleta.

## A gruppi con intestazione

**Regolarità**: un'intestazione dice di che cosa sono le righe sotto, che **non lo ripetono**. Nel nuoto, la gara. Serve uno stato che sopravvive da una riga all'altra: la gara corrente, cambiata dalle intestazioni e usata dalle prestazioni.

## Record su più righe

**Regolarità**: un record comincia con una riga riconoscibile, `PMID`, ha un campo per riga con un'etichetta in posizione fissa, e finisce con una riga vuota. Classificate e contate, le righe di PubMed sono:

```
{'vuota': 14817, 'PMID': 14817, 'DP': 14817, 'TI': 14814, 'continuazione': 12012, 'PL': 14817, 'AID': 19765}
```

Il conto dice già tre cose: 3 pubblicazioni senza titolo; `AID` più numeroso dei record, quindi **ripetuto**, e da tenere in una lista; e 14 817 righe vuote per 14 817 pubblicazioni, anche se l'ultima non è chiusa da una riga vuota. Il conto torna perché c'è **una riga vuota in testa al file**: `head -2` la mostra. Due anomalie che si compensano sono il caso peggiore, perché il conto sembra giusto; per questo il metodo dice di guardare anche `head` e `tail`.

---

# Parte III — Forme nuove e file complessi

Forme che si incontrano spesso fuori dal corso, ciascuna con una regolarità diversa, e due formati già strutturati da mettere a confronto.

## A sezioni: i file di configurazione

Molti programmi tengono le impostazioni in file così, con estensione `.ini` o `.cfg`:

```
; stazioni meteo della rete urbana
[Brera]
quota = 122
tipo = urbana

[Lambrate]
quota = 120
; sensore sostituito nel 2010
tipo = periferica
attiva = no
```

**Regolarità**: la sezione è fra parentesi quadre, ogni riga dopo è `chiave = valore`, i commenti cominciano con `;`. È un file a gruppi con intestazione, come il nuoto, ma con coppie chiave-valore invece di colonne:

```python
def leggiIni(nomeFile):
    sezioni = {}
    corrente = None
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if riga == "" or riga.startswith(";"):
                pass
            elif riga.startswith("[") and riga.endswith("]"):
                corrente = riga[1:-1]
                sezioni[corrente] = {}
            else:
                chiave, uguale, valore = riga.partition("=")
                sezioni[corrente][chiave.strip()] = valore.strip()
    return sezioni
```

```
{'Brera': {'quota': '122', 'tipo': 'urbana'}, 'Lambrate': {'quota': '120', 'tipo': 'periferica', 'attiva': 'no'}}
```

**`partition("=")` spezza al primo `=`**, e restituisce sempre tre pezzi: prima, il separatore, dopo. A differenza di `split`, non sbaglia se il valore contiene a sua volta un `=`.

Il commento in mezzo alla sezione non cambia niente: la regola dei commenti viene prima, e la riga si salta. Per i file `.ini` veri Python ha il modulo `configparser`, che fa lo stesso lavoro e gestisce i casi limite.

## Configurazione già strutturata: TOML

TOML è il successore moderno dei file `.ini`, e lo usano molti strumenti di Python: `pyproject.toml` descrive un progetto, i suoi moduli e le sue dipendenze. Le stesse stazioni:

```
# stazioni meteo della rete urbana
rete = "Milano"
aggiornato = 2011-12-31

[Brera]
quota = 122
tipo = "urbana"

[Lambrate]
quota = 120
tipo = "periferica"   # sensore sostituito nel 2010
attiva = false
minime = [-4, -5, -3]
```

La forma è quella del file `.ini`, ma **i valori hanno un tipo**: le stringhe stanno fra virgolette, i numeri no, `false` è un booleano, `[-4, -5, -3]` una lista, `2011-12-31` una data. Non c'è niente da riconoscere riga per riga, e nemmeno da convertire: lo fa il modulo `tomllib`, nella libreria standard da Python 3.11.

```python
import tomllib

with open("stazioni.toml", "rb") as f:
    stazioni = tomllib.load(f)
print(stazioni["Lambrate"])
print(stazioni["Brera"]["quota"] + 1, stazioni["aggiornato"])
```

```
{'quota': 120, 'tipo': 'periferica', 'attiva': False, 'minime': [-4, -5, -3]}
123 2011-12-31
```

**Il file si apre in `"rb"`**, in byte, come chiede `tomllib`: la codifica la gestisce lui, ed è sempre UTF-8. Le sezioni diventano dizionari, e la quota è già un intero: `+ 1` funziona senza `int`. Il commento in fondo alla riga di `tipo` sparisce da solo, mentre nel file `.ini` un commento in fondo a una riga sarebbe finito dentro il valore.

`tomllib` sa solo **leggere**. Per un file di impostazioni è quello che serve: lo scrive una persona, lo legge il programma.

## Sequenze su più righe: il formato FASTA

In biologia le sequenze di DNA e di proteine si scambiano in questo formato:

```
>seq1 sequenza di esempio
MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFLPFFS
NVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFAS
>seq2 sequenza di esempio
MSDNGPQNQRNAPRITFGGPSDSTGSNQNGERSGARSKQRRPQGLPNNTASWFTALTQHG
KEDLKFPRGQGVPINTNSSPDDQIGYYRRATRRIRGGDGKMKDLSPRWYFYYLGTGPEAG
LPYGANKDGIIWVATEGALNTPKDHIGTRNPANNAAIVLQLPQGTTLPKGFYAE
```

**Regolarità**: un record comincia con `>`, seguito dal nome e da una descrizione; le righe dopo, **senza etichetta**, sono pezzi della sequenza da attaccare uno all'altro. Non c'è una riga che chiude il record: lo chiude il `>` del successivo, o la fine del file. È il caso in cui conviene mettere il record nella struttura **appena comincia**:

```python
def leggiFasta(nomeFile):
    sequenze = {}
    nome = None
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            riga = riga.strip()
            if riga.startswith(">"):
                nome = riga[1:].split()[0]
                sequenze[nome] = ""
            elif riga != "":
                sequenze[nome] = sequenze[nome] + riga
    return sequenze
```

```
seq1 94
seq2 174
```

**Il conto**: `grep -c "^>"` dice 2. Le righe di continuazione sono le stesse del titolo di PubMed, portate all'estremo: qui il dato vero sta tutto lì.

## Righe con struttura interna: un log

I programmi scrivono quello che fanno in un file di log, una riga per evento:

```
2026-11-20 08:31:02 INFO caricamento: lette 367 righe da MeteoMilano2011.csv
2026-11-20 08:31:02 WARNING caricamento: riga 18 senza minima
2026-11-20 08:31:02 WARNING caricamento: riga 19 senza minima
2026-11-20 08:31:03 ERROR calcolo: divisione per zero nel mese 13
2026-11-20 08:31:03 INFO fine: 2 avvisi, 1 errore
```

**Regolarità**: i primi tre campi sono separati da spazi e hanno sempre la stessa forma; il quarto, il messaggio, è testo libero, **con spazi dentro**. `split(" ")` lo farebbe a pezzi:

```python
riga = "2026-11-20 08:31:02 WARNING caricamento: riga 18 senza minima"
print(riga.split(" "))
print(riga.split(" ", 3))
```

```
['2026-11-20', '08:31:02', 'WARNING', 'caricamento:', 'riga', '18', 'senza', 'minima']
['2026-11-20', '08:31:02', 'WARNING', 'caricamento: riga 18 senza minima']
```

**`split(" ", 3)` fa al massimo tre tagli**, e lascia intero tutto quello che resta: quattro pezzi, l'ultimo con i suoi spazi. Raggruppando per livello:

```python
def contaLivelli(nomeFile):
    livelli = {}
    with open(nomeFile, encoding="utf-8") as f:
        for riga in f:
            data, ora, livello, messaggio = riga.strip().split(" ", 3)
            if livello in livelli:
                livelli[livello].append(messaggio)
            else:
                livelli[livello] = [messaggio]
    return livelli
```

```
INFO 2
WARNING 2
ERROR 1
```

## CSV con le virgolette

Un CSV può avere la virgola anche dentro un campo, se il campo è fra virgolette; e una virgoletta dentro un campo si scrive doppia:

```
id,descrizione,prezzo
0,"Esselunga, Cornetti gusto formaggio 100 g",0.59
1,"Biscotti ""della nonna"", 350 g",2.19
```

Qui **`split(",")` non basta più**: sulla riga 0 dà quattro pezzi, con le virgolette attaccate.

```
['0', '"Esselunga', ' Cornetti gusto formaggio 100 g"', '0.59']
```

La regolarità c'è, ma la regola è complicata: una virgola separa solo se non sta fra virgolette, e una virgoletta doppia non chiude. Scriverla a mano si può, carattere per carattere, ma è il caso in cui conviene uno strumento: **`read_csv` di pandas**, che arriva con `FOD`, conosce le virgolette e le tratta da sé. Il metodo serve comunque per accorgersene: è `cat -A`, o `head`, che mostra le virgolette prima che `split` produca un pezzo di troppo.

## Righe sporche

I file veri hanno difetti che il metodo deve prevedere:

- **campi vuoti**: in `MeteoMilano2011.csv` il 16 e il 17 gennaio non hanno la minima, e `int("")` darebbe errore. Si controlla prima, e si mette `None`, come in aula;
- **spazi attorno ai valori**: `" 12"`, `"Brera "`. `strip()` su ogni campo, sempre;
- **maiuscole e minuscole**: `"BRERA"` e `"Brera"` sono chiavi diverse. Si normalizza, con `lower()` o `title()`, prima di usare il valore come chiave;
- **numeri con la virgola**: `"962,68"`. `replace(",", ".")` prima di `float`;
- **il `\r` di Windows**: in modalità testo Python lo toglie da solo, e `strip()` comunque lo toglierebbe;
- **il BOM**: alcuni programmi su Windows mettono all'inizio del file un carattere invisibile, che finisce attaccato al primo campo dell'intestazione:

```python
with open("bom.csv", encoding="utf-8") as f:
    print(repr(f.readline()))
with open("bom.csv", encoding="utf-8-sig") as f:
    print(repr(f.readline()))
```

```
'﻿giorno;minima\n'
'giorno;minima\n'
```

  `encoding="utf-8-sig"` lo toglie se c'è, e non fa niente se non c'è.

**Per trovare le righe sporche serve il loro numero.** `enumerate` numera le righe mentre le legge, e il messaggio può dire dove guardare:

```python
with open(percorso, encoding="utf-8") as f:
    for numero, riga in enumerate(f, start=1):
        campi = riga.strip().split(",")
        if numero > 2 and campi[3] == "":
            print("riga", numero, "senza minima:", campi[0])
```

```
riga 18 senza minima: 2011-1-16
riga 19 senza minima: 2011-1-17
```

`sed -n 18p MeteoMilano2011.csv` mostra la riga 18 nel terminale.

## Un formato già strutturato: JSON

Molti servizi web restituiscono dati in JSON, che ha la forma dei dizionari e delle liste di Python:

```python
import json

testo = '{"stazione": "Brera", "quota": 122, "minime": [-4, -5, -3], "attiva": true}'
dati = json.loads(testo)
print(dati["minime"], type(dati["quota"]), dati["attiva"])
```

```
[-4, -5, -3] <class 'int'> True
```

Qui non c'è niente da riconoscere: la struttura è dichiarata nel testo, e **i tipi sono già convertiti**, numeri, liste, `True`. `json.load(f)` legge da un file aperto, `json.loads(testo)` da una stringa. È il contrario di un file semistrutturato, ed è utile vederli vicini: quando un servizio offre il JSON, conviene prendere quello.

---

# Parte IV — La cassetta degli attrezzi

**Metodi delle stringhe**, per riconoscere e spezzare una riga:

| Metodo | Che cosa fa | Esempio |
|---|---|---|
| `strip()`, `lstrip()`, `rstrip()` | toglie spazi e a capo dai due lati, da sinistra, da destra | `"  Brera ".strip()` dà `'Brera'` |
| `split(sep)` | spezza a ogni separatore | `"2011-1-16".split("-")` dà `['2011', '1', '16']` |
| `split(sep, n)` | al massimo `n` tagli, il resto intero | il log della parte III |
| `partition(sep)` | spezza al primo separatore, sempre tre pezzi | `chiave = valore` |
| `startswith(...)`, `endswith(...)` | come comincia, come finisce | `riga.startswith("#")` |
| `x in riga` | se contiene un pezzo | `"Categoria" in riga` |
| `find(x)` | dove comincia un pezzo, o -1 | trovare le colonne fisse |
| `isdigit()` | se sono tutte cifre | `"12".isdigit()` è `True`, ma `"-4".isdigit()` è `False` |
| `replace(a, b)` | sostituisce | `"962,68".replace(",", ".")` |
| `lower()`, `upper()`, `title()` | normalizza le maiuscole | `"LAMBRATE".title()` dà `'Lambrate'` |
| slicing `riga[a:b]` | i caratteri da `a` a `b - 1` | le colonne fisse |

**Funzioni e moduli**:

| Strumento | Quando serve |
|---|---|
| `enumerate(f, start=1)` | il numero di riga, per i messaggi |
| `f.readline()` prima del ciclo | saltare un'intestazione |
| `pl.Path(...).read_text().splitlines()` | il file intero come lista di righe senza a capo, vedi `focus_PythonEOS.md` |
| `json.load`, `json.loads` | dati già strutturati |
| `configparser` | file `.ini` |
| `tomllib` | file `.toml`, già con i tipi |
| `Counter`, `defaultdict` | contare e raggruppare in una riga, vedi `focus_StruttureDati.md` |

**Le espressioni regolari**, il modulo `re`, descrivono un modello di testo, per esempio «quattro cifre, un trattino, una o due cifre»: servono quando la regolarità sta **dentro** la riga e non si riduce a un separatore o a una posizione fissa. Sono uno strumento potente e difficile da leggere; con i metodi delle stringhe si arriva quasi sempre allo stesso risultato, e più chiaro. Il tutorial ufficiale è nei link in fondo.

---

# Parte V — Python puro o pandas

pandas, che arriva con `FOD`, carica in una riga i file **regolari**:

- `read_csv` legge CSV e TSV, con `sep=`, `skiprows=` per le righe in testa, `comment="#"` per i commenti, `decimal=","` per la virgola dei decimali, e le virgolette;
- `read_fwf` legge i file a **colonne fisse**, se le colonne sono le stesse in tutto il file;
- `read_json` legge il JSON.

Quello che **non** sa fare è il resto: i gruppi con intestazione, dove una riga dice di che cosa sono le righe sotto; i record su più righe, come PubMed e FASTA; i campi che si ripetono; le righe di tipi diversi mescolate nello stesso file. Il nuoto, con intestazioni, separatori e prestazioni intercalati, `read_fwf` non lo carica da solo.

**La strada, nei casi difficili, è in due passi**: Python puro riconosce le righe e costruisce una lista di record tutti uguali, e da lì pandas fa i conti. Il metodo di questa pagina è il primo passo, e nessuna libreria lo fa al posto vostro: per scriverlo bisogna aver guardato il file.

---

## Per approfondire

- I metodi delle stringhe: <https://docs.python.org/3/library/stdtypes.html#string-methods>.
- Il modulo `tomllib`: <https://docs.python.org/3/library/tomllib.html>; il formato TOML: <https://toml.io/en/>.
- Il modulo `json`: <https://docs.python.org/3/library/json.html>.
- Il modulo `configparser`: <https://docs.python.org/3/library/configparser.html>.
- Le espressioni regolari, il tutorial: <https://docs.python.org/3/howto/regex.html>.
- Il formato FASTA: <https://en.wikipedia.org/wiki/FASTA_format>.
- In pandas, `read_csv` e `read_fwf`: <https://pandas.pydata.org/docs/reference/io.html>.
