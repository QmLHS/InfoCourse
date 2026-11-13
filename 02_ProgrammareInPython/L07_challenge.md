# Challenge — Forza 4

**Lezione coperta:** `L07` — strutture dati complesse e iteratori

Si svolge in aula al termine di `A03`. **Senza soluzioni** e **senza consegna**: per parlarne, la lezione dopo o il ricevimento.

---

## Il gioco

Una griglia di **6 righe e 7 colonne**, due giocatori. A turno ciascuno sceglie una colonna e ci lascia cadere una pedina, che si ferma sulla casella libera più in basso. **Vince chi mette quattro pedine di fila**: in orizzontale, in verticale o in diagonale. Se la griglia si riempie senza un vincitore, la partita è patta.

La griglia è una **lista di liste**, e le dieci challenge la costruiscono un pezzo alla volta: una griglia vuota, una pedina che cade, una partita fra due persone, chi ha vinto, una partita contro il computer, mille partite a caso. Poi si prova a far giocare bene il computer.

---

## Cosa ti serve

| | |
|:---|:---|
| **la macchina** | la VM del corso (`guida_VM.md`), o il tuo computer se preferisci |
| **l'editor** | Visual Studio Code, `guida_VSCode.md` |
| **il repository** | `~/InfoCourse`, aggiornato con `git pull` (`guida_GitHub.md`) |
| **le tracce** | la cartella `02_ProgrammareInPython/L07_challenge/`, dieci file da `ch_01.py` a `ch_10.py` |

**Come si scrive la griglia.** Una casella vuota è il carattere `'.'`, le pedine sono `'X'`, di chi comincia, e `'O'`. La riga 0 è quella **in alto**, la riga 5 è il fondo; le colonne vanno da 0 a 6 nel programma e da 1 a 7 sullo schermo, dove le sceglie il giocatore. `griglia[riga][colonna]` è una casella.

**I numeri a caso.** Dalla 7 in poi il computer gioca, e per scegliere una colonna a caso usa `numpy`, come in `L06_challenge`. La riga è già scritta nella traccia:

```python
colonna = np.random.randint(0, colonne)
```

estrae un intero **da 0 a `colonne - 1`**: il secondo estremo è escluso.

---

## Come si lavora

**Copia la cartella delle tracce fuori dal repository**, per esempio:

```bash
cp -r ~/InfoCourse/02_ProgrammareInPython/L07_challenge ~/challenge_L07
```

Se lavori dentro `~/InfoCourse`, al prossimo `git pull` le tue modifiche vanno in conflitto con le tracce.

Ogni traccia ha quattro parti: l'**enunciato** in testa, in commento; i **dati**, già pronti; il **codice**, che scrivi tu; le **risposte** alle domande, nei commenti in fondo. Dove ci sono più blocchi di dati, prova il programma su **tutti**, ricommentando il blocco attivo e togliendo il commento al successivo.

Alla fine `python3 ch_N.py`, da un terminale appena aperto, non deve dare errori. Le tracce 3 e 7 chiedono le mosse con `input()`: aspettano che tu le scriva.

**Le challenge si concatenano**: la 2 parte dalla griglia della 1, la 3 mette insieme la 1 e la 2; la 5 riscrive la 4, la 6 la usa; la 7 aggiunge alla 3 il controllo della 5; la 8 riparte dalla 7 con un controllo più rapido, la 9 lo usa per provare le mosse, la 10 riparte dalla 9. Non avendo ancora le funzioni, «riusare» qui vuol dire ricopiare il tuo codice da un file all'altro.

**Niente `break`**: un ciclo finisce quando la sua condizione diventa falsa. Se servono due motivi per finire, stanno tutti e due nella condizione.

---

## Le dieci

| # | Traccia | Difficoltà | Argomento |
|:-:|:---|:-:|:---|
| 1 | `ch_01.py` — La griglia vuota | • | una lista di liste, e come non costruirla |
| 2 | `ch_02.py` — Una pedina che cade | • | cercare in una colonna con il `while` |
| 3 | `ch_03.py` — Una partita in due | •• | il turno che passa, l'input controllato |
| 4 | `ch_04.py` — Quattro in fila: orizzontale e verticale | •• | visitare una griglia senza uscirne |
| 5 | `ch_05.py` — Le diagonali, e una direzione sola | •• | quattro pezzi di codice che sono uno, con una lista di tuple |
| 6 | `ch_06.py` — La griglia è possibile? | •• | la domanda che il testo non fa |
| 7 | `ch_07.py` — Contro il computer | •• | due motivi per finire, nella condizione |
| 8 | `ch_08.py` — Mille partite a caso | ••• | guardare solo dove qualcosa è cambiato |
| 9 | `ch_09.py` — Il computer furbo | ••• | provare una mossa e tornare indietro |
| 10 | `ch_10.py` — La colonna migliore | ••• | la colonna della fila più lunga, e l'ordine in cui la si cerca |

La difficoltà sale **in fretta**. Le prime cinque si fanno con quello che hai visto a lezione e negli esercizi; dalla 6 in poi bisogna ragionare sul gioco più che su Python, e la 10 è lunga.

---

## Riferimenti

`riepilogo_funzioni_python.md` e `L07_riepilogo.md` per la sintassi, `L07_esercizi.md` per gli esempi svolti di liste, tuple e liste di liste, `L06_challenge.md` per un altro gioco costruito un pezzo alla volta.
