# Challenge 8 - Mille partite a caso (difficoltà: 3/3)
#
# Due computer giocano `partite` partite, tutti e due a caso come nella 7. Niente `input()` e niente stampe durante le partite: alla fine il programma stampa quante ne ha vinte chi comincia, quante chi gioca per secondo, quante sono patte, e quante mosse dura una partita in media.
#
# Il controllo della 5 guarda tutta la griglia dopo ogni mossa. Ma se la partita non era finita prima, l'unica fila nuova può passare solo per la pedina appena messa: scrivi un controllo che guarda solo quella. Per ogni direzione, conta le pedine uguali di fila andando avanti e poi indietro a partire dalla pedina; se in una direzione sono almeno quattro, ha vinto.
#
# Controllo: chi comincia vince circa il 55% delle partite, chi gioca per secondo circa il 44%, le patte sono due o tre su mille, una partita dura circa 21 mosse. Ogni esecuzione dà numeri un po' diversi.
#
# Rispondi nei commenti in fondo:
#
#   a. quante caselle guarda, al massimo, il controllo della 5 dopo ogni mossa? E il tuo?
#   b. il nuovo controllo conta avanti e indietro. Che cosa sbaglierebbe se contasse solo in avanti? Trova una mossa che vince e che il controllo in avanti non vede.
#   c. anche giocando a caso, chi comincia vince più spesso. Perché?

import numpy as np

# --- dati ----------------------------------------------------------------------

righe = 6
colonne = 7
partite = 1000

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
# c.
