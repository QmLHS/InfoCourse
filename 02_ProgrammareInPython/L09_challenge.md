# Challenge — Quanti saremo

**Lezione coperta:** `L08` e `L09` — funzioni, moduli e file

Si svolge in aula al termine di `A04`. **Senza soluzioni** e **senza consegna**: per parlarne, la lezione dopo o il ricevimento.

---

## I dati

Il primo giorno del corso, in `L01`, c'era una domanda: **«Come varierà la distribuzione della popolazione, stratificata per genere, dal 2017 al 2050?»**. Le dieci challenge ci arrivano partendo dal file che risponde, così come l'ISTAT lo distribuisce.

`data/previsioniISTAT2017.csv` contiene le **previsioni probabilistiche della popolazione residente in Italia**, per sesso ed età, fatte dall'ISTAT con base 1° gennaio 2017, anno per anno dal 2017 al 2065. Comincia così:

```
"Previsioni probabilistiche della popolazione residente per sesso, età e regione - base 1.1.2017 - Anni 2017/2065"
"Anno: 2017 - Ripartizione: Italia"
"Maschi"
"Età";"Limite inferiore intervallo di confidenza al 90% (5° percentile)";...
0;240100;240100;240100;240100;240100;240100;240100;
1;249511;249511;249511;249511;249511;249511;249511;
```

Separatore `;`, codifica UTF-8. **Non è una tabella**, è un file a blocchi: per ogni anno ci sono tre blocchi, maschi, femmine e totale, e ogni blocco ha la sua intestazione, una riga per età da 0 a «110 e oltre», e una riga «Totale».

**Una previsione probabilistica non dà un numero, ne dà sette.** Per ogni anno, sesso ed età, l'ISTAT simula molti futuri possibili, con natalità, mortalità e migrazioni diverse, e riporta i percentili dei risultati: il 5°, il 10°, il 25°, la **mediana**, il 75°, il 90° e il 95°. Fra il 5° e il 95° percentile sta il 90% degli scenari. Nel codice le sette colonne sono numerate da 0 a 6, e la mediana è la colonna 3.

È il tipo di file che `read_csv` di pandas non legge da solo: per caricarlo bisogna riconoscerne le righe, come in `L09` e in `focus_FileSemistrutturati.md`.

---

## Cosa ti serve

| | |
|:---|:---|
| **la macchina** | la VM del corso (`guida_VM.md`), o il tuo computer se preferisci |
| **l'editor** | Visual Studio Code, `guida_VSCode.md` |
| **il repository** | `~/InfoCourse`, aggiornato con `git pull` (`guida_GitHub.md`) |
| **la traccia** | `02_ProgrammareInPython/L09_challenge/ch_ISTAT.py`, un file solo per tutte e dieci |
| **i dati** | `02_ProgrammareInPython/data/previsioniISTAT2017.csv`: la traccia lo trova da sola, con `pathlib` |

---

## Come si lavora

**Copia la cartella della traccia fuori dal repository**, per esempio:

```bash
cp -r ~/InfoCourse/02_ProgrammareInPython/L09_challenge ~/challenge_L09
```

Se lavori dentro `~/InfoCourse`, al prossimo `git pull` le tue modifiche vanno in conflitto con la traccia.

**La traccia ha due parti.**

- **La parte prima, le challenge da 1 a 6, ha la forma dell'esame.** Le funzioni sono già dichiarate e numerate, con la firma fissata; il commento sopra ciascuna dice che cosa riceve, che cosa restituisce, e dà un esempio. Il corpo principale, in fondo alla parte prima, è già scritto: chiama le funzioni e stampa `Es. 1)`, `Es. 2)` e così via. Tu completi le funzioni, e puoi aggiungerne altre. È il modo in cui è fatto il compito d'esame, e conviene abituarcisi adesso: i nomi dei parametri portano il tipo, `sRiga_IN` una stringa, `dBlocco_IN` un dizionario, `fName_IN` il nome di un file.
- **La parte seconda, le challenge da 7 a 10, è libera.** Ci sono solo gli enunciati: le funzioni e il codice li scrivi tu, usando quello che hai costruito nella parte prima.

Finché le funzioni della parte prima sono vuote, il programma si ferma all'`Es. 3)` con un errore: è normale, e sparisce quando `caricaPrevisioni` restituisce i due dizionari.

**Le domande di ragionamento**, una o due per challenge, stanno tutte in fondo al file: rispondi nei commenti. All'esame non ci sono; qui sono la parte che conta di più.

Alla fine `python3 ch_ISTAT.py`, da un terminale appena aperto, non deve dare errori.

**Le challenge si concatenano**: la 3 usa le funzioni della 1 e della 2, e dalla 4 in poi tutto parte dalla struttura della 3. La 6 scrive `popolazione`, che la 10 riusa, e la 4 lascia aperta una domanda a cui risponde la 9.

**Niente `break`**: un ciclo finisce quando la sua condizione diventa falsa.

**Ogni caricamento si controlla con un conto**, fatto per un'altra strada: `wc -l`, `grep -c`, o una somma che deve tornare. Quando un conto non torna, è lì che c'è qualcosa da capire.

---

## Le dieci

| # | Parte | Difficoltà | Argomento |
|:-:|:---|:-:|:---|
| 1 | prima — Guardare e classificare | • | i tipi di riga, e quante sono |
| 2 | prima — Una riga di dati | • | `split`, il campo vuoto in fondo, «110 e oltre» |
| 3 | prima — Tutto il file | •• | anno e sesso che sopravvivono da una riga all'altra |
| 4 | prima — I conti tornano? | •• | maschi più femmine, la somma delle età e la riga «Totale» |
| 5 | prima — Salvare un anno per file | •• | 49 file puliti, con `pathlib` |
| 6 | prima — Gli indicatori di un anno | ••• | indice di vecchiaia, di dipendenza, età mediana |
| 7 | seconda — La traiettoria | ••• | la popolazione dal 2017 al 2065, con il suo intervallo |
| 8 | seconda — Quanto è incerta | ••• | l'incertezza che cresce, e le età più certe |
| 9 | seconda — Il conto che non torna | ••• | perché i percentili non si sommano |
| 10 | seconda — Dal 2017 al 2050 | ••• | la piramide delle età, e la risposta alla domanda di `L01` |

La difficoltà sale **in fretta**. Le prime sei hanno i binari dell'esame; dalla 7 in poi i binari non ci sono, e bisogna ragionare sui dati più che su Python, e le risposte della 8, della 9 e della 10 non si trovano nel codice: si trovano pensando a che cosa vogliono dire i numeri.

---

## Riferimenti

`L08_esercizi.md` per le funzioni e i moduli, `L09_esercizi.md` per il caricamento dei file, `focus_FileSemistrutturati.md` per il metodo, `focus_PythonEOS.md` per `pathlib`.
