# Challenge — una giornata a Milano

**Lezioni coperte:** `L04` — variabili, istruzioni, espressioni, logica
booleana · `L05` — selezione

Si svolge in aula al termine di `A01`. **Senza soluzioni** e **senza
consegna**: per parlarne, la lezione dopo o il ricevimento.

---

## Cosa ti serve

| | |
|:---|:---|
| **la macchina** | la VM del corso (`guida_VM.md`), o il tuo computer se preferisci |
| **l'editor** | Visual Studio Code, `guida_VSCode.md` |
| **il repository** | `~/InfoCourse`, aggiornato con `git pull` (`guida_GitHub.md`) |
| **le tracce** | la cartella `02_ProgrammareInPython/L05_challenge/`, dieci file da `ch_01.py` a `ch_10.py` |

**I dati.** Vengono tutti da `MeteoMilano2011.csv` (`03_FocusOnData/data/`,
separatore `,`, codifica UTF-8), le misure meteo giornaliere di Milano nel
2011. **Non devi aprirlo**: le righe che servono sono già nelle tracce,
trascritte in variabili. Leggere un file con Python è l'argomento di `L09`.

---

## Come si lavora

**Copia la cartella delle tracce fuori dal repository**, per esempio:

```bash
cp -r ~/InfoCourse/02_ProgrammareInPython/L05_challenge ~/challenge_L05
```

Se lavori dentro `~/InfoCourse`, al prossimo `git pull` le tue modifiche vanno
in conflitto con le tracce.

Ogni traccia ha tre parti:

```python
# Challenge 4 - Da dove soffia (difficoltà: 2/3)
#
# ... l'enunciato, completo ...

# --- dati: MeteoMilano2011.csv -----------------------------------------------
data = "2011-01-01"
direzione = 225

# --- il tuo codice -----------------------------------------------------------

# --- risposte ----------------------------------------------------------------
# a.
```

L'**enunciato** sta in testa, in commento, e c'è solo lì: questo file è
l'indice. I **dati** sono già pronti. Il **codice** lo scrivi tu, e le
**risposte** alle domande vanno nei commenti in fondo.

Quasi tutte le tracce hanno più blocchi di dati, quelli in più commentati:
prova il programma su **tutti**, ricommentando il blocco attivo e togliendo il
commento al successivo. Un programma provato su un caso solo non è provato.

Alla fine `python ch_N.py`, da un terminale appena aperto, non deve dare
errori. Dalla 2 in poi, se lo script chiede dati con `input()`, aspetta che
tu li scriva: è normale.

**Le challenge si concatenano**: la 2 riparte dai dati della 1, la 9 riusa la
4, la 10 riusa la 6 e verifica la 7. Non avendo ancora le funzioni, «riusare»
qui vuol dire ricopiare il tuo codice da un file all'altro. Se ti sembra
scomodo hai ragione: è il problema che risolve `L08`.

**Converti con `int()` e `float()`.**

---

## Le dieci

| # | Traccia | Difficoltà | Argomento |
|:-:|:---|:-:|:---|
| 1 | `ch_01.py` — La giornata in variabili | • | espressioni, tipi, f-string |
| 2 | `ch_02.py` — Cambiare unità | • | precedenze, decimali, una conversione che non si può fare due volte, `input()` |
| 3 | `ch_03.py` — Gelo, ghiaccio, notti tropicali | •• | etichette che si escludono e etichette che convivono |
| 4 | `ch_04.py` — Da dove soffia | •• | settori, un valore che non è un dato |
| 5 | `ch_05.py` — Il freddo percepito | •• | una formula che vale solo in un campo |
| 6 | `ch_06.py` — Che giorno dell'anno | •• | il calendario, anni bisestili |
| 7 | `ch_07.py` — Che giorno della settimana | ••• | tradurre una formula, divisione intera e resto |
| 8 | `ch_08.py` — Il giorno dopo | ••• | selezione annidata, tutti i casi di bordo |
| 9 | `ch_09.py` — Il dato sporco | ••• | testo, campi vuoti, segnalare tutto e non solo il primo errore |
| 10 | `ch_10.py` — Quanto distano | ••• | contare i giorni senza cicli |

La difficoltà sale **in fretta**. Le prime cinque si fanno con quello che
hai visto a lezione e negli esercizi; le ultime quattro chiedono di ragionare
su un calendario più di quanto chiedano Python.

---

## Riferimenti

`riepilogo_funzioni_python.md` per la sintassi, `L04_esercizi.md` e
`L05_esercizi.md` per gli esempi svolti — l'anno bisestile è l'esercizio 12 di
`L04`, il wind chill l'abbiamo visto in aula a `F04`.
