# Scrivere file con un editor: Visual Studio Code sulla VM

> **A cosa serve.** Con la shell hai imparato a creare file con `echo` e a
> guardarli con `cat`. Va bene per una riga; per uno script di dieci non basta.
> Da qui in avanti i file li scrivi con un **editor**, e sulla macchina del
> corso l'editor è **Visual Studio Code** (VS Code).
>
> **Non è materia d'esame.** È lo strumento con cui scriverai tutto il resto:
> gli script della shell adesso, i programmi Python da `L04` in poi.
>
> Vale anche sul tuo computer, se ce l'hai installato: cambia solo il tasto
> `Ctrl`, che su Mac diventa `Cmd`.

---

## 1. Aprire VS Code

Sulla VM: menu delle applicazioni, cerca **Visual Studio Code**. La prima volta
ci mette qualche secondo; le successive si riapre com'era, con le stesse
schede aperte.

---

## 2. Aprire **la cartella**, non il file

È la cosa che cambia tutto, ed è controintuitiva: non aprire il singolo file,
apri la **cartella** in cui lavori.

*File > Apri cartella…*, e scegli `InfoCourse` nella tua home — o la cartella
degli esercizi, se stai lavorando là.

Perché conta:

- a sinistra vedi l'**albero dei file**, che è la stessa cosa che `ls` ti mostra
  un livello alla volta: qui la vedi tutta insieme;
- il **terminale integrato** (punto 4) parte già dentro quella cartella, quindi
  i percorsi relativi funzionano senza dover fare `cd`;
- quando salvi un file nuovo, VS Code propone quella cartella, non una a caso.

---

## 3. Creare un file e salvarlo dove vuoi tu

1. *File > Nuovo file di testo* (`Ctrl + N`).
2. Scrivi quello che ti serve.
3. **Salva subito** con `Ctrl + S`: si apre la finestra del nome.
4. Scrivi il nome **con l'estensione**: `esplora.sh`, non `esplora`. E controlla
   la cartella proposta in alto nella finestra: è lì che il file finirà.

Un file non salvato è segnato da un **pallino** al posto della X sulla sua
scheda. Se lanci uno script e vedi ancora il comportamento di prima, la prima
cosa da controllare è quel pallino: stai eseguendo la versione su disco, non
quella che hai davanti.

Per verificare dal terminale dove è finito davvero:

```bash
pwd
ls -l esplora.sh
```

---

## 4. Il terminale integrato

*Terminale > Nuovo terminale*, oppure `Ctrl + ù` su tastiera italiana (è il
tasto che sulle tastiere inglesi porta il backtick, sotto `Esc`).

Si apre **dentro la finestra di VS Code**, in basso, e parte nella cartella che
hai aperto al punto 2. È lo stesso identico terminale di prima: gli stessi
comandi, lo stesso `pwd`, la stessa shell. Il vantaggio è che editor e terminale
sono a un centimetro di distanza, e non devi ricordarti dove stavi.

Puoi tenerne aperti più di uno e passare dall'uno all'altro con l'elenco a
destra del pannello.

---

## 5. Rendere eseguibile uno script e lanciarlo

Un file appena creato **non è eseguibile**: il sistema lo tratta come testo. Dal
terminale integrato:

```bash
chmod +x esplora.sh     # una volta sola, per quel file
./esplora.sh dati.csv   # il ./ dice: sta qui, non fra i comandi di sistema
```

Se ti dimentichi `chmod`, c'è la via breve, che funziona sempre e non cambia i
permessi:

```bash
bash esplora.sh dati.csv
```

Il `./` davanti non è un capriccio: senza, la shell cerca `esplora.sh` fra i
programmi installati e non lo trova, perché la cartella corrente **non** è fra i
posti in cui guarda.

---

## Scorciatoie che userai davvero

Sono le stesse che trovi in *File > Preferenze > Scorciatoie da tastiera*, dove
puoi anche cambiarle.

### Scrivere e modificare

| Azione | Linux (VM) | Mac |
|:---|:---|:---|
| Salva | `Ctrl + S` | `Cmd + S` |
| Annulla / ripeti | `Ctrl + Z` / `Ctrl + Shift + Z` | `Cmd + Z` / `Cmd + Shift + Z` |
| Commenta o decommenta le righe selezionate | `Ctrl + /` | `Cmd + /` |
| Duplica la riga | `Shift + Alt + Giù` | `Shift + Option + Giù` |
| Sposta la riga su o giù | `Alt + Su` / `Alt + Giù` | `Option + Su` / `Option + Giù` |
| Cancella la riga | `Ctrl + Shift + K` | `Cmd + Shift + K` |
| Più cursori insieme | `Alt + clic` | `Option + clic` |
| Rientra o sporgi | `Tab` / `Shift + Tab` | `Tab` / `Shift + Tab` |

### Muoversi

| Azione | Linux (VM) | Mac |
|:---|:---|:---|
| Vai a un file per nome | `Ctrl + P` | `Cmd + P` |
| Vai a una riga | `Ctrl + G` | `Cmd + G` |
| Cerca nel file | `Ctrl + F` | `Cmd + F` |
| Cerca in tutti i file della cartella | `Ctrl + Shift + F` | `Cmd + Shift + F` |
| Sostituisci nel file | `Ctrl + H` | `Cmd + Option + F` |
| Mostra o nascondi l'albero dei file | `Ctrl + B` | `Cmd + B` |

### File e terminale

| Azione | Linux (VM) | Mac |
|:---|:---|:---|
| Nuovo file | `Ctrl + N` | `Cmd + N` |
| Chiudi la scheda | `Ctrl + W` | `Cmd + W` |
| Apri o chiudi il terminale integrato | `Ctrl + ù` | `Ctrl + ù` |
| Nuovo terminale accanto al primo | `Ctrl + Shift + ù` | `Ctrl + Shift + ù` |
| Palette dei comandi: **tutto** si fa da qui | `Ctrl + Shift + P` | `Cmd + Shift + P` |

La palette dei comandi è la scorciatoia che vale per dieci: ci scrivi una
parola di quello che vuoi fare — *terminale*, *salva*, *formatta* — e lui ti
propone il comando con la sua scorciatoia accanto. È anche il modo di imparare
le altre senza studiarle.

---

## Tre cose che fanno perdere mezz'ora

**Il file è salvato, ma non dove credi.** Succede quando salvi senza aver aperto
una cartella: VS Code propone l'ultima che ha visto. Rimedio: apri sempre la
cartella (punto 2), e se il dubbio resta, `ls -l` nel terminale integrato.

**Il nome senza estensione, o con quella sbagliata.** `esplora` e `esplora.sh`
per la shell sono la stessa cosa — l'estensione non decide nulla per Linux — ma
VS Code la usa per capire che linguaggio è, e quindi per colorare il testo e
avvisarti degli errori. Senza `.sh` scrivi in bianco e nero.

**La riga di stato, in basso a destra.** Dice tre cose che nella lezione sui
byte contano: la **codifica** (deve essere `UTF-8`), il **fine riga** (`LF` su
Linux, `CRLF` se il file viene da Windows) e il **linguaggio**. Se uno script
copiato da Windows dà errori incomprensibili, guarda lì: cliccando su `CRLF` lo
converti in `LF` e salvi.

---

## Due cose da non fare

**Non spuntare `trim trailing whitespace`.** Sembra una pulizia utile — toglie
gli spazi in fondo alle righe quando salvi — ma su un file di dati cancella
informazione: nel file degli iscritti il codice `T1 ` ha uno spazio che fa parte
del dato, e salvando lo perderesti senza accorgertene. Le impostazioni del punto
precedente **mostrano** i caratteri invisibili, non li toccano: è la differenza
che conta.

**Non aprire i dati con Excel o Word.** Un `.csv` è un file di testo, ma quei
programmi non lo mostrano: mostrano la loro interpretazione, e se salvi la
scrivono sul file. Gli zeri iniziali dei codici spariscono (`00101` diventa
`101`), le date vengono riscritte secondo la lingua del sistema, il separatore
cambia. Per **guardare** i dati si usa l'editor o la shell (`head`, `cut`); per
**modificarli** si scrive un programma che legge un file e ne scrive un altro,
lasciando l'originale dov'è.

---

## Se qualcosa non funziona

| Problema | Cosa fare |
|:---|:---|
| VS Code non parte o è lentissimo | la VM ha poca memoria: chiudi le finestre che non usi e riprova |
| il terminale integrato non si apre con la scorciatoia | usa il menu *Terminale > Nuovo terminale*: la scorciatoia dipende dalla tastiera |
| `./esplora.sh` dice «Permission denied» | manca `chmod +x`, oppure usa `bash esplora.sh` |
| `./esplora.sh` dice «No such file or directory» | non sei nella cartella dello script: `pwd` per vedere dove sei, `ls` per vedere cosa c'è |
| lo script fa ancora la cosa di prima | non l'hai salvato: guarda il pallino sulla scheda, poi `Ctrl + S` |
