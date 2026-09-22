# Challenge — dalla shell ai dati

**Lezione coperta:** `L02` — informazione, calcolatore, SO, file system, shell

Si svolge in aula al termine di `F02`. **Senza soluzioni** e **senza
consegna**: per parlarne, la lezione dopo o il ricevimento.

---

## Cosa ti serve

| | |
|:---|:---|
| **la macchina** | la VM del corso (`guida_VM.md`), o il tuo computer se preferisci |
| **l'editor** | Visual Studio Code, `guida_VSCode.md` — da qui in poi i file si scrivono con l'editor, non con `echo` |
| **il repository** | `~/InfoCourse`, aggiornato con `git pull` (`guida_GitHub.md`) |
| **lo script** | `01_AmbienteDiLavoro/esplora.sh`, che trovi nel repository |

**I dati.**

| File | Dove | Separatore | Codifica |
|:---|:---|:---:|:---|
| `2009-2013_iscritti.csv` | `01_AmbienteDiLavoro/data/` | `;` | UTF-8 |
| `MeteoMilano2011.csv` | `03_FocusOnData/data/` | `,` | UTF-8 |

Il secondo sta in un'altra cartella del repository.

---

## Come si lavora

Scrivi tutto in **un solo file**, `ch_L02.sh`, in una tua cartella — *non*
dentro `~/InfoCourse`, che al prossimo `git pull` si aggiorna.

Un blocco per challenge, così:

```bash
# --- Challenge 1 ---------------------------------------------------------
cd ~
pwd
# Risposta: la home e' /home/nomeutente
```

Il **comando** che hai usato, e sotto, **come commento**, la risposta o quello
che hai capito. Le challenge si concatenano: la 5 lavora su quello che ha
costruito la 4.

Alla fine `bash ch_L02.sh`, da una sessione appena aperta, non deve dare
errori.

---

## Parte prima — muoversi, e far lavorare uno script

### Challenge 1 — Dove sono (difficoltà: •)

Parti dalla tua home. Raggiungi la cartella dei dati di `01_AmbienteDiLavoro`
nel repository **senza mai scrivere un percorso assoluto**: solo passi
relativi. A ogni passo mostra dove sei.

Poi torna alla home in **due modi diversi**, e scrivi nel commento che
differenza c'è fra i due.

### Challenge 2 — Il percorso assoluto (difficoltà: •)

Del file `MeteoMilano2011.csv` sai solo il nome: non sai in quale cartella sia.
Trovalo partendo dalla home, con un comando solo, e scrivi nel commento il suo
**percorso assoluto**.

Poi verifica che sia davvero quello: da una cartella qualsiasi, mostra la prima
riga del file usando quel percorso.

### Challenge 3 — Il primo file scritto con l'editor (difficoltà: •)

Crea `ch_L02.sh` **con Visual Studio Code**, non con `echo` e non con `touch`:
apri la cartella in cui vuoi lavorare, crea il file, salvalo con il nome giusto.

Dal terminale integrato, dimostra che esiste e che è tuo: percorso, dimensione,
permessi, tutto in una riga sola.

Nel commento scrivi **cosa stampa la riga dei permessi** e che cosa significa
che manca la `x`.

### Challenge 4 — Lanciare uno script che sta altrove (difficoltà: ••)

`esplora.sh` sta in `~/InfoCourse/01_AmbienteDiLavoro/`. Lanciato senza
argomenti ti dice come si usa: parti da lì.

Poi eseguilo su `2009-2013_iscritti.csv` **tre volte**, ottenendo lo stesso
identico risultato:

1. dalla tua cartella di lavoro, passando il file con il **percorso assoluto**;
2. dalla stessa cartella, passando il file con un **percorso relativo**;
3. da dentro `~/InfoCourse/01_AmbienteDiLavoro/`, con il percorso più corto che
   riesci a scrivere.

Il separatore di quel file è dichiarato nella tabella dei dati, sopra.

### Challenge 5 — Rompere lo script, e capire il messaggio (difficoltà: ••)

Ora fallo fallire, apposta, in **due modi diversi**:

- chiamandolo con un percorso relativo che vale in un'altra cartella;
- chiamandolo con `./esplora.sh` da una cartella in cui lo script non c'è.

Copia nel commento i due messaggi d'errore e, per ciascuno, la causa. Poi fai
funzionare entrambi i casi senza spostare né copiare lo script.

Infine: rendi `esplora.sh` eseguibile in una tua copia e lancialo con `./`.
Nel commento, la differenza fra lanciarlo con `./` e lanciarlo con `bash`.

---

## Parte seconda — il primo sguardo a dati veri

Da qui in avanti usi `2009-2013_iscritti.csv`. È l'elenco degli iscritti per
ateneo e anno accademico, come lo pubblica il Ministero.

### Challenge 6 — Quanto è grande (difficoltà: •)

Quante righe ha il file? E quante di queste sono **dati**?

Quante colonne? Scrivi nel commento come hai fatto a contarle senza contarle a
mano.

### Challenge 7 — Le colonne, numerate (difficoltà: •)

Stampa l'intestazione una colonna per riga, **numerata**, come fa `esplora.sh`.
Ma fallo con i tuoi comandi, in una pipeline che scrivi tu.

Nel commento: il numero della colonna con il nome dell'ateneo, e quello della
colonna con gli iscritti alla laurea.

### Challenge 8 — Quanti atenei (difficoltà: ••)

Quanti atenei **distinti** compaiono nel file?

Nel commento, il numero e la pipeline che l'ha prodotto.

### Challenge 9 — La classifica (difficoltà: ••)

Per l'anno accademico più recente presente nel file, i **dieci atenei con più
iscritti alla laurea**, dal più grande al più piccolo, con il numero accanto.

Una pipeline sola. Nel commento, i primi tre.

### Challenge 10 — La virgola che non è un separatore (difficoltà: •••)

Estrai la colonna del nome dell'ateneo usando la **virgola** come separatore
invece del punto e virgola, e guarda cosa esce.

Poi trova **quante righe del file contengono almeno una virgola**, e guardane
una. Nel commento spiega, in due righe, perché un programma che «divide sulla
virgola» su questo file darebbe un risultato sbagliato senza dare nessun errore.

---

## Parte terza — il secondo file

Ora passa a `MeteoMilano2011.csv`, nell'altra cartella del repository. Sono le
misure meteo giornaliere di Milano per il 2011.

### Challenge 11 — Lo script sbaglia (difficoltà: ••)

Lancia `esplora.sh` su questo file. Dice che ha **una colonna sola** e non
mostra le righe di dati che ti aspetti.

Trova perché, guardando le prime righe del file **byte per byte**, e scrivi la
spiegazione nel commento.

### Challenge 12 — Le colonne vere (difficoltà: ••)

Ora che sai qual è l'intestazione vera, stampala numerata, una per riga.

Quante colonne ci sono? Nel commento scrivi anche una cosa che noti nei nomi di
alcune colonne e che ti darebbe fastidio se dovessi cercarle per nome.

### Challenge 13 — La colonna quasi vuota (difficoltà: •••)

La colonna `Eventi` dice che tempo ha fatto quel giorno — pioggia, nebbia,
temporale — ma non tutti i giorni ce l'hanno.

Quanti giorni hanno il campo **pieno**, e quanti **vuoto**? I due numeri devono
sommare ai giorni del 2011: riporta nel commento anche la somma.

### Challenge 14 — Qualcosa in coda a ogni riga (difficoltà: •••)

Nell'**ultima colonna** c'è attaccato, a ogni riga, qualcosa che non è un
dato.

Trova che cos'è, scrivi nel commento da dove arriva secondo te, e produci una
versione pulita del file — in una **tua** cartella, senza toccare l'originale —
in cui quella cosa non c'è più. Dimostra che la pulizia ha funzionato.

### Challenge 15 — Il tuo esplora.sh (difficoltà: •••)

Copia `esplora.sh` in una tua cartella e modificalo con l'editor perché faccia
due cose in più:

- **salti le righe vuote iniziali**, così da funzionare anche sul meteo;
- accetti un terzo argomento, il **numero di una colonna**, e stampi quanti dei
  suoi valori sono pieni e quanti vuoti — cioè la challenge 13, fatta una volta
  per tutte.

Deve continuare a funzionare come prima quando il terzo argomento non c'è.
Provalo su tutti e due i file di dati.

---

## Riferimenti

`L02_riepilogo.md` per la sintassi dei comandi, `L02_shell.md` per la
spiegazione, `man comando` sulla macchina per la documentazione completa.
