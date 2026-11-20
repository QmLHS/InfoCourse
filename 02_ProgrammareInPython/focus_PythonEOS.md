# Focus — Python e il sistema operativo

> **Materiale facoltativo.** Non è materia d'esame e non serve per nessun esercizio del corso. È per chi, finita `L09`, vuole lavorare con i file senza scrivere percorsi a mano, scrivere script che funzionino su Linux, macOS e Windows, e lanciare un programma da un altro tenendo traccia di come è andata.

Si dà per saputo `L09`: aprire, leggere e scrivere un file, `with`, le modalità. Il focus ha tre parti, che si possono leggere separatamente:

- **I. I percorsi**: `pathlib`, cioè costruire, smontare e interrogare un percorso, cercare file, leggere e scrivere in una riga;
- **II. Lo script e il sistema**: `sys`, cioè gli argomenti da riga di comando e l'uscita con un messaggio;
- **III. Uno script che ne lancia un altro**: `subprocess` e un file di log, costruiti un passo alla volta.

Ogni esempio è eseguito con Python 3.12, la versione della VM, e 3.14. I percorsi assoluti stampati sono quelli della VM, dove l'utente si chiama `studente`; sul vostro computer la prima parte sarà diversa.

> **Una regola, prima di cominciare.** Un percorso scritto a mano, come `"/home/studente/InfoCourse/data/meteo.csv"`, funziona su un computer solo. Tutto quello che segue serve a non doverne scrivere.

---

# Parte I — I percorsi

## Relativo a che cosa

Un percorso **relativo**, come `"data/meteo.csv"`, si legge a partire dalla **cartella da cui si lancia lo script**, non da quella dove lo script sta. Con lo script `~/esercizi/dove.py`:

```python
import pathlib as pl

print(pl.Path.cwd())
print(pl.Path(__file__).parent)
```

lanciato dalla home, con `python esercizi/dove.py`, stampa:

```
/home/studente
/home/studente/esercizi
```

**`Path.cwd()` è la cartella corrente**, quella da cui avete lanciato il comando: è lì che Python cerca un percorso relativo. **`Path(__file__).parent` è la cartella dello script**, e non cambia, da dovunque lo si lanci. `__file__` è una variabile che Python riempie con il percorso dello script; nell'interprete interattivo non esiste, perché non c'è uno script.

Due punti fissi, quindi, per costruire un percorso che funzioni sempre:

- **`Path.home()`**, la home di chi lancia lo script, per i file che stanno in un posto noto, come `~/InfoCourse`;
- **`Path(__file__).parent`**, per i file che stanno accanto allo script.

## Costruire un percorso con `/`

```python
import pathlib as pl

percorso = pl.Path.home() / "InfoCourse" / "03_FocusOnData" / "data" / "MeteoMilano2011.csv"
```

**`/` fra un percorso e una stringa aggiunge un pezzo**, e mette il separatore giusto per il sistema: `/` su Linux e macOS, `\` su Windows. Il risultato non è una stringa, è un percorso: si può passare direttamente a `open`, e ha i suoi metodi.

## I pezzi di un percorso

```python
print(percorso.name)
print(percorso.stem)
print(percorso.suffix)
print(percorso.parent.name)
print(percorso.parts[-3:])
print(percorso.with_suffix(".tsv").name)
```

```
MeteoMilano2011.csv
MeteoMilano2011
.csv
data
('03_FocusOnData', 'data', 'MeteoMilano2011.csv')
MeteoMilano2011.tsv
```

| Attributo | Che cosa è |
|---|---|
| `name` | il nome del file, con l'estensione |
| `stem` | il nome senza l'estensione |
| `suffix` | l'estensione, con il punto |
| `parent` | la cartella che lo contiene, a sua volta un percorso |
| `parts` | tutti i pezzi, in una tupla |
| `with_suffix(".tsv")` | lo stesso percorso con un'altra estensione |

`with_suffix` è il modo pulito di costruire il nome di un file di uscita dal nome di quello di entrata: da `MeteoMilano2011.csv` a `MeteoMilano2011.tsv`, o a `MeteoMilano2011.log`. Con le stringhe si finisce a scrivere `nome.split(".")[0]`, che sbaglia sui nomi con più di un punto.

## Chiedere al file system

```python
print(percorso.exists(), percorso.is_file(), percorso.is_dir())
print(percorso.parent.is_dir())
```

```
True True False
True
```

**`exists()` dice se il percorso c'è**, `is_file()` se è un file, `is_dir()` se è una cartella. Sono la prima cosa da controllare prima di aprire un file che viene da fuori, per esempio dalla riga di comando, come nella parte II.

**`open` crea il file ma non la cartella.** Se la cartella non c'è:

```
FileNotFoundError: [Errno 2] No such file or directory: 'nuova/x.txt'
```

La cartella si crea con `mkdir`:

```python
uscita = pl.Path("risultati") / "gennaio" / "riassunto.txt"
uscita.parent.mkdir(parents=True, exist_ok=True)
```

`parents=True` crea anche le cartelle intermedie, qui `risultati`; `exist_ok=True` non dà errore se la cartella c'è già. Con tutti e due, la riga si può lasciare nello script e rilanciarlo quante volte si vuole.

## Cercare file

```python
dati = pl.Path.home() / "InfoCourse"
for file in sorted(dati.rglob("*.csv")):
    print(file.relative_to(dati))
```

```
01_AmbienteDiLavoro/data/2009-2013_iscritti.csv
02_ProgrammareInPython/data/telefonate.csv
03_FocusOnData/data/MeteoMilano2011.csv
```

- **`iterdir()`** dà il contenuto di una cartella, file e sottocartelle, senza scendere;
- **`glob("*.csv")`** dà i file della cartella che corrispondono al modello: `*` vuol dire «qualunque cosa», come nella shell di `L02`;
- **`rglob("*.csv")`** fa lo stesso **in tutte le sottocartelle**.

`relative_to(dati)` toglie la parte iniziale, e lascia il percorso a partire da `dati`. `sorted` mette i risultati in ordine: `glob` e `rglob` li danno nell'ordine del file system, che non è alfabetico e cambia da un sistema all'altro.

Con `iterdir` e `stat().st_size` si ha anche la dimensione di ogni file, in byte:

```python
cartella = dati / "02_ProgrammareInPython" / "data"
for file in sorted(cartella.iterdir()):
    print(file.name, file.stat().st_size)
```

```
gareNuoto.txt 111999
itemsFOD.tsv 6654
pubmedCoronavirus.txt 3143833
telefonate.csv 19826
```

È il modo di trattare tutti i file di una cartella con lo stesso codice: un ciclo su `glob`, e dentro la funzione che ne carica uno.

## Leggere e scrivere in una riga

```python
uscita.write_text("minima -8\nmassima 4\n", encoding="utf-8")
print(uscita.read_text(encoding="utf-8").splitlines())
```

```
['minima -8', 'massima 4']
```

**`write_text` apre il file in `"w"`, scrive la stringa e lo chiude**; `read_text` lo apre, lo legge tutto e lo chiude. Sono un `with` in una riga. `splitlines()` spezza il testo in righe, e a differenza di `readlines` toglie gli a capo.

Valgono le regole di `open`: `write_text` **svuota il file** se c'era, e l'`encoding` va scritto, perché il default dipende dal sistema.

Quando **non** usarli: su un file grande, `read_text` lo carica tutto in memoria. PubMed, tre megabyte, ci sta senza problemi; un file da qualche gigabyte no. Lì si torna al ciclo `for riga in f`, che tiene in memoria una riga alla volta.

## Lo stesso codice su ogni sistema

```python
p = pl.PurePosixPath("data") / "meteo.csv"
w = pl.PureWindowsPath("data") / "meteo.csv"
print(p, w)
print(w.as_posix())
```

```
data/meteo.csv data\meteo.csv
data/meteo.csv
```

`PurePosixPath` e `PureWindowsPath` costruiscono percorsi **come li scriverebbe** un sistema o l'altro, su qualunque computer: servono a vedere la differenza. `pl.Path` sceglie da solo quella del sistema su cui gira, ed è l'unico che serve davvero. `as_posix()` scrive un percorso con le barre `/`, anche se è di Windows.

**Il `\` di Windows dentro una stringa è una trappola.** In Python `\` comincia una sequenza speciale, come `\n`:

```python
print(repr("C:\nuovi\dati.csv"))
```

```
SyntaxWarning: invalid escape sequence '\d'
'C:\nuovi\\dati.csv'
```

`\n` è diventato un a capo, e `\d` un avviso. Con `/` e `pathlib` il problema non si pone.

---

# Parte II — Lo script e il sistema

## Gli argomenti da riga di comando

In `L02_challenge` uno script riceveva il nome di un file dalla riga di comando. **`sys.argv` è la lista di quello che è stato scritto dopo `python`**: il primo elemento è il nome dello script, gli altri sono gli argomenti, tutti stringhe.

```python
import pathlib as pl
import sys

if len(sys.argv) != 2:
    sys.exit("Uso: python contaRighe.py NOMEFILE")

percorso = pl.Path(sys.argv[1])
if not percorso.is_file():
    sys.exit(f"{percorso} non è un file")

with open(percorso, encoding="utf-8") as f:
    righe = f.readlines()
print(percorso.name, len(righe))
```

```
$ python esercizi/contaRighe.py InfoCourse/03_FocusOnData/data/MeteoMilano2011.csv
MeteoMilano2011.csv 367
$ python esercizi/contaRighe.py
Uso: python contaRighe.py NOMEFILE
$ python esercizi/contaRighe.py InfoCourse/03_FocusOnData/data
InfoCourse/03_FocusOnData/data non è un file
```

**`sys.exit(messaggio)` ferma lo script**, stampa il messaggio, e dice al sistema che qualcosa è andato storto: il **codice di uscita** è 1 invece di 0. È meglio di un errore di Python, perché dice a chi lo usa che cosa ha sbagliato. Lo stesso controllo, senza `sys.exit`, finirebbe in un `IndexError` su `sys.argv[1]`, o in un `FileNotFoundError` dentro `open`.

Il percorso dalla riga di comando è relativo alla cartella da cui si lancia, come tutti i percorsi relativi.

## Che cos'altro dice `sys`

- **`sys.executable`**: il percorso dell'interprete Python che sta girando. Serve nella parte III, per lanciare un altro script con lo stesso Python;
- **`sys.version_info`**: la versione; sulla VM `sys.version_info[:2]` è `(3, 12)`;
- **`sys.platform`**: il sistema, `linux` sulla VM, `darwin` su macOS, `win32` su Windows.

## `os.path`, per riconoscerlo

Nel codice che troverete in giro, scritto prima di `pathlib` o da chi non lo usa, i percorsi passano per il modulo `os`. Non serve scriverlo, ma serve leggerlo:

| Con `os` | Con `pathlib` |
|---|---|
| `os.path.join(cartella, "meteo.csv")` | `cartella / "meteo.csv"` |
| `os.path.exists(p)` | `p.exists()` |
| `os.path.isfile(p)`, `os.path.isdir(p)` | `p.is_file()`, `p.is_dir()` |
| `os.path.basename(p)` | `p.name` |
| `os.path.splitext(p)[0]` | `p.stem` (solo il nome) |
| `os.path.dirname(p)` | `p.parent` |
| `os.getcwd()` | `pl.Path.cwd()` |
| `os.path.expanduser("~")` | `pl.Path.home()` |
| `os.listdir(c)` | `c.iterdir()` |
| `os.makedirs(c, exist_ok=True)` | `c.mkdir(parents=True, exist_ok=True)` |
| `os.sep` | non serve: lo mette `/` |

La differenza di fondo: con `os.path` un percorso è **una stringa**, e ogni operazione è una funzione a cui la si passa; con `pathlib` è **un percorso**, che sa fare le sue operazioni.

---

# Parte III — Uno script che ne lancia un altro

Un'analisi vera spesso è fatta di più script: uno scarica i dati, uno li pulisce, uno fa i conti. Uno script che li lancia in fila, e che **tiene traccia** di come è andata, è il primo passo verso un'analisi che si può rifare. Lo costruiamo un passo alla volta: ogni passo aggiunge una cosa sola al precedente.

## Il programma da lanciare

`provaErrore.py`, nella vostra cartella `~/esercizi`, stampa il suo argomento, e una volta su due va in errore:

```python
import sys
import numpy as np

print(sys.argv[0], "con il parametro", sys.argv[1])
lettere = ["a", "b"]
if np.random.random() > 0.5:
    print(lettere[2])
print("finito")
```

L'errore è voluto: serve a vedere che cosa succede quando un programma lanciato da un altro fallisce.

## Passo 1 — Lanciarlo, e raccoglierne l'uscita

```python
import subprocess
import sys

esito = subprocess.run([sys.executable, "provaErrore.py", "7"],
                       capture_output=True, text=True)
print("uscita:", esito.stdout)
print("errori:", esito.stderr)
print("codice di uscita:", esito.returncode)
```

Una volta su due:

```
uscita: provaErrore.py con il parametro 7
finito

errori:
codice di uscita: 0
```

e l'altra:

```
uscita: provaErrore.py con il parametro 7

errori: Traceback (most recent call last):
  File "provaErrore.py", line 7, in <module>
    print(lettere[2])
          ~~~~~~~^^^
IndexError: list index out of range

codice di uscita: 1
```

**`subprocess.run` lancia un programma e aspetta che finisca.** Il comando è una lista: l'interprete, lo script, gli argomenti, come si scriverebbero nel terminale. `sys.executable` è lo stesso Python che sta girando, così il secondo script trova gli stessi moduli, numpy compreso.

**`capture_output=True` raccoglie quello che il programma stampa** invece di mandarlo sullo schermo, in due canali: `stdout`, l'uscita normale, e `stderr`, gli errori. `text=True` li restituisce come stringhe. **`returncode` è il codice di uscita**: 0 se è andato tutto bene, un altro numero se no. È lo stesso codice che `sys.exit` imposta nella parte II.

Il primo script **non si ferma** quando il secondo fallisce: riceve l'errore come testo, e decide lui che cosa farne.

## Passo 2 — Scrivere su un file di log

Le stampe sullo schermo si perdono quando si chiude il terminale. Si scrivono invece su un file:

```python
fileLog = "lancia.log"
with open(fileLog, "w", encoding="utf-8") as log:
    log.write("uscita:\n" + esito.stdout)
    log.write("errori:\n" + esito.stderr)
    log.write(f"codice di uscita: {esito.returncode}\n")
```

## Passo 3 — Il nome del log dal nome dello script

Un nome scritto a mano va cambiato in ogni script. Lo si ricava dal nome dello script stesso, con `stem`:

```python
fileLog = pl.Path(__file__).stem + ".log"
```

Da `lancia.py` viene `lancia.log`. Copiando lo script con un altro nome, il log cambia nome da solo.

## Passo 4 — Un log per ogni esecuzione

Con `"w"` ogni esecuzione cancella il log della precedente. Si aggiunge al nome **l'istante** in cui lo script parte:

```python
import time

istante = time.strftime("%Y%m%d%H%M%S")
fileLog = f"{pl.Path(__file__).stem}_{istante}.log"
```

`time.strftime` scrive data e ora secondo un modello: `%Y` l'anno, `%m` il mese, `%d` il giorno, poi ore, minuti e secondi. Il risultato è un nome come `lancia_20261120114729.log`. **Anno, mese, giorno, in quest'ordine**: così l'ordine alfabetico dei file è anche l'ordine cronologico, e `ls` li mette in fila da sé.

## Passo 5 — Una cartella per i log

I log si accumulano, e vanno tenuti insieme in una cartella, `logs`, accanto allo script, creata se non c'è:

```python
cartellaScript = pl.Path(__file__).parent
cartellaLog = cartellaScript / "logs"
cartellaLog.mkdir(exist_ok=True)
fileLog = cartellaLog / f"{pl.Path(__file__).stem}_{istante}.log"
```

**La cartella si costruisce da `Path(__file__).parent`, non dalla cartella corrente**: così i log finiscono sempre accanto allo script, da dovunque lo si lanci. È la differenza della parte I fra `cwd()` e `__file__`.

## Passo 6 — Controllare prima di lanciare

Se il programma da lanciare non c'è, `subprocess.run` lo scopre solo eseguendo, e l'errore finisce nel log, dove nessuno lo guarda subito. Meglio controllare prima, e fermarsi con un messaggio:

```python
programma = cartellaScript / "provaErrore.py"
if not programma.exists():
    sys.exit(f"Il programma {programma} non esiste: controlla il percorso")
```

Lo script completo, a questo punto:

```python
import pathlib as pl
import subprocess
import sys
import time

cartellaScript = pl.Path(__file__).parent
istante = time.strftime("%Y%m%d%H%M%S")
cartellaLog = cartellaScript / "logs"
cartellaLog.mkdir(exist_ok=True)
fileLog = cartellaLog / f"{pl.Path(__file__).stem}_{istante}.log"

programma = cartellaScript / "provaErrore.py"
if not programma.exists():
    sys.exit(f"Il programma {programma} non esiste: controlla il percorso")

esito = subprocess.run([sys.executable, programma, "7"],
                       capture_output=True, text=True)
with open(fileLog, "w", encoding="utf-8") as log:
    log.write("uscita:\n" + esito.stdout)
    log.write("errori:\n" + esito.stderr)
    log.write(f"codice di uscita: {esito.returncode}\n")
print("log scritto in", fileLog.relative_to(cartellaScript))
```

```
log scritto in logs/lancia_20261120114729.log
```

## Passo 7 — Le funzioni in un modulo

Ogni script che lancia qualcosa ha bisogno delle stesse righe: l'istante, la cartella, il controllo, il lancio, il log. Si spostano in un modulo, `strumenti.py`, come `temperature.py` in `L08_esercizi`:

```python
import pathlib as pl
import subprocess
import sys
import time


def istante():
    return time.strftime("%Y%m%d%H%M%S")


def cartelleDiLavoro(radice, nomi):
    cartelle = {}
    for chiave in nomi:
        cartella = pl.Path(radice) / nomi[chiave]
        cartella.mkdir(parents=True, exist_ok=True)
        cartelle[chiave] = cartella
    return cartelle


def esisteOEsci(percorso):
    if not pl.Path(percorso).exists():
        sys.exit(f"{percorso} non esiste: controlla il percorso")


def lancia(programma, *argomenti):
    return subprocess.run([sys.executable, programma, *argomenti],
                          capture_output=True, text=True)


def scriviLog(cartella, nomeScript, esito):
    fileLog = pl.Path(cartella) / f"{pl.Path(nomeScript).stem}_{istante()}.log"
    with open(fileLog, "w", encoding="utf-8") as log:
        log.write("uscita:\n" + esito.stdout)
        log.write("errori:\n" + esito.stderr)
        log.write(f"codice di uscita: {esito.returncode}\n")
    return fileLog
```

`*argomenti`, nella definizione di `lancia`, raccoglie in una tupla tutti gli argomenti dopo il primo, quanti che siano; `*argomenti` dentro la lista li rimette in fila. È il `*args` di `L08_b`.

## Passo 8 — Le cartelle di lavoro

Un progetto di analisi ha di solito tre cartelle: i **dati** grezzi, che non si toccano; i **log**; i **report**, cioè i risultati. `cartelleDiLavoro` le crea tutte e restituisce un dizionario con i loro percorsi. Lo script che lancia diventa:

```python
import pathlib as pl
import strumenti as st

cartellaScript = pl.Path(__file__).parent
cartelle = st.cartelleDiLavoro(cartellaScript, {"dati": "dati",
                                                "log": "logs",
                                                "report": "report"})
programma = cartellaScript / "provaErrore.py"
st.esisteOEsci(programma)
esito = st.lancia(programma, "7")
fileLog = st.scriviLog(cartelle["log"], __file__, esito)
print("log scritto in", fileLog.relative_to(cartellaScript))
```

Lo script dice **che cosa** fa, in sei righe; **come** lo fa sta nel modulo, scritto una volta e usato da tutti gli script del progetto.

## Da qui in avanti

- Per lanciare più programmi in fila basta una lista di programmi e un ciclo. Se uno fallisce, cioè se `returncode` non è 0, conviene fermarsi: i passi dopo lavorerebbero su dati che non ci sono.
- Python ha un modulo apposta per i log, `logging`, che aggiunge da solo l'ora a ogni riga e distingue i messaggi per gravità. Per uno script del corso basta quello che abbiamo costruito; per un progetto lungo vale la pena di guardarlo.

---

## Per approfondire

- `pathlib`, la documentazione ufficiale: <https://docs.python.org/3/library/pathlib.html>, con la tabella delle corrispondenze con `os.path` in fondo alla pagina.
- `sys`: <https://docs.python.org/3/library/sys.html>.
- `subprocess`: <https://docs.python.org/3/library/subprocess.html>.
- I modelli di `time.strftime`: <https://docs.python.org/3/library/time.html#time.strftime>.
- `logging`, il tutorial di base: <https://docs.python.org/3/howto/logging.html>.
