---
title: "Il gioco dell'oca, da soli"
subtitle: "Informatica@SGI — L06, cicli: scomporre un problema"
---

Si simula una partita al gioco dell'oca con **un giocatore solo**. Il programma è troppo grande per scriverlo di getto: va **scomposto** in pezzi più piccoli, ciascuno dei quali si scrive e si prova da solo. È lo stesso lavoro fatto con l'area sotto la parabola, su un problema diverso.

La traccia da completare è `L06_oca.py`.

---

## Le regole

Il tabellone ha **63 caselle**. Si parte dalla casella **0**, fuori dal tabellone. A ogni turno si tirano **due dadi** e si avanza della loro somma.

| Casella | Nome | Che cosa succede |
|:--|:--|:--|
| 9, 18, 27, 36, 45, 54 | oca | si avanza **ancora** della stessa somma |
| 6 | ponte | come l'oca: si avanza ancora della stessa somma |
| 19 | locanda | si sta fermi **3 turni** |
| 31 | pozzo | vedi sotto |
| 42 | labirinto | si torna alla casella 33 |
| 52 | prigione | vedi sotto |
| 58 | scheletro | si torna alla casella 1 |
| 63 | arrivo | la partita finisce |

**Il 63 va raggiunto esatto.** Chi lo supera torna indietro dei punti in più: da 60, con un 7, si arriva a 67, cioè 4 oltre il 63, e si finisce sulla **59**.

**Le caselle si controllano dopo ogni spostamento**, anche quelli dovuti a un'oca o a un rimbalzo: da un'oca si può finire su un'altra oca, e da un rimbalzo sullo scheletro.

**Pozzo e prigione.** Nel gioco a più giocatori si resta bloccati finché un'altra pedina non arriva a liberarci. Giocando da soli, in questo esercizio **non hanno effetto**. Prima di scrivere il codice, chiediti: che cosa succederebbe al ciclo se applicassimo la regola alla lettera?

---

## Il lancio dei dadi: due modi

Nella traccia il lancio è già scritto, in due modi. Servono `numpy` e una funzione che si chiama con un nome con il punto: per ora si usano così come sono, e si capiranno in `L08`.

**Modo 1: due dadi, e si sommano.**

```python
dado1 = np.random.randint(1, 7)
dado2 = np.random.randint(1, 7)
somma = dado1 + dado2
```

`np.random.randint(1, 7)` estrae un intero da 1 a **6**: il secondo estremo è **escluso**. Con `randint(1, 6)` il 6 non uscirebbe mai.

**Modo 2: un'estrazione sola, da 2 a 12.**

```python
somma = np.random.choice(range(2, 13), p=[1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36])
```

`range(2, 13)` sono i valori da 2 a 12, e `p` dice la probabilità di ciascuno. Con due dadi l'**1** non può uscire.

Da dove vengono quelle probabilità? Le 36 coppie di facce sono tutte ugualmente probabili, ma le somme no:

| | 1 | 2 | 3 | 4 | 5 | 6 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **1** | 2 | 3 | 4 | 5 | 6 | 7 |
| **2** | 3 | 4 | 5 | 6 | 7 | 8 |
| **3** | 4 | 5 | 6 | 7 | 8 | 9 |
| **4** | 5 | 6 | 7 | 8 | 9 | 10 |
| **5** | 6 | 7 | 8 | 9 | 10 | 11 |
| **6** | 7 | 8 | 9 | 10 | 11 | 12 |

Il 7 compare **6 volte** su 36, il 2 e il 12 una volta sola: la probabilità di una somma è il numero delle sue caselle diviso 36.

Domanda: e se scrivessimo `np.random.choice(range(2, 13))`, senza `p`? Il programma funzionerebbe lo stesso. Che cosa simulerebbe?

---

## Scomporre il problema

Non si scrive la partita: si scrive **un turno**, e poi lo si ripete.

**Passo 1 — un turno.** Scrivi il codice che, partendo da una `posizione`:

1. tira i dadi;
2. avanza della somma;
3. se ha superato il 63, rimbalza indietro;
4. finché è su un'oca o sul ponte, avanza ancora, e controlla di nuovo il rimbalzo;
5. controlla le caselle che spostano (labirinto, scheletro) o fermano (locanda).

Provalo assegnando a mano `posizione` e `somma`, invece di tirare i dadi: da 0 con 9, da 0 con 6, da 61 con 7, da 13 con 6. Sai già dove deve finire ciascuno?

**Passo 2 — la partita.** Ripeti il turno **finché** la posizione non è 63, contando i turni. Serve una variabile che ricordi per quanti turni si è ancora fermi alla locanda: in quei turni non si tira.

**Passo 3 — la stampa.** A ogni turno stampa il numero del turno, la somma uscita e la casella d'arrivo, così da poter seguire la partita. Alla fine: in quanti turni si è arrivati al 63.

---

## Per chi finisce prima

**Molte partite.** Metti la partita dentro un altro ciclo e giocane 1000, senza stampare i turni. Quanti turni dura una partita in media? Qual è la più lunga?

**Al primo lancio.** Quante delle 1000 partite finiscono **al primo turno**? Prima di contarle, prova a capire come sia possibile, e quante te ne aspetti.

**I due modi.** Rifai le 1000 partite con il modo 2 del lancio: la durata media cambia?
