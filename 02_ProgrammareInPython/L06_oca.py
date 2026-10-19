# Il gioco dell'oca, da soli: la traccia.
# Le regole e i passi sono in L06_oca.md.

import numpy as np

# ── Il lancio dei dadi ───────────────────────────────────────────────────────
# Due modi, scegline uno. Per ora sono qui in testa: vanno spostati nel punto
# del programma in cui si tirano i dadi.

# Modo 1: due dadi, e si sommano. randint(1, 7) estrae da 1 a 6
dado1 = np.random.randint(1, 7)
dado2 = np.random.randint(1, 7)
somma = dado1 + dado2

# Modo 2: un'estrazione sola, da 2 a 12, con la probabilita' di ogni somma
# somma = np.random.choice(range(2, 13), p=[1/36, 2/36, 3/36, 4/36, 5/36, 6/36,
#                                           5/36, 4/36, 3/36, 2/36, 1/36])

print("somma dei dadi:", somma)


# ── Passo 1: un turno ────────────────────────────────────────────────────────
# Prova con posizione e somma assegnate a mano, senza dadi:
# da 0 con 9, da 0 con 6, da 61 con 7, da 13 con 6.

posizione = 0

# avanzo

# se ho superato il 63, rimbalzo

# finche' sono su un'oca o sul ponte, avanzo ancora (e ricontrollo il rimbalzo)

# labirinto, scheletro, locanda


# ── Passo 2: la partita ──────────────────────────────────────────────────────
# Ripeto il turno finche' non arrivo al 63, contando i turni.
# Alla locanda si sta fermi: in quei turni non si tirano i dadi.


# ── Passo 3: la stampa ───────────────────────────────────────────────────────
# A ogni turno: numero del turno, somma, casella d'arrivo.
# Alla fine: in quanti turni sono arrivato al 63.
