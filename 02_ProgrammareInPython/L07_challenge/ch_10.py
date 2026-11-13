# Challenge 10 - La colonna migliore (difficoltà: 3/3)
#
# Il giocatore 'migliore' fa quello che fa il furbo, ma quando non c'è niente da vincere o da bloccare non gioca a caso: sceglie la colonna in cui la sua pedina formerebbe la fila più lunga, contando come nella 8. Le colonne le prova nell'ordine della lista `ordine`; a parità di fila tiene la prima che ha trovato.
#
# Fai giocare il migliore contro il furbo della 9 per `partite` partite, una a testa per chi comincia, e stampa quante ne vince ciascuno. Poi cambia `ordine` e ripeti.
#
# Controllo: con le colonne provate da sinistra il migliore vince circa il 58% delle partite; con l'altro ordine circa l'80%.
#
# Rispondi nei commenti in fondo:
#
#   a. la colonna più lunga si trova come il massimo, ma non basta sapere quanto è lunga la fila: serve sapere in che colonna. Come l'hai tenuta? Perché cambiando solo l'ordine in cui si provano le colonne cambia tanto il risultato?
#   b. fai giocare il migliore contro un altro migliore con lo stesso `ordine`: tutte le partite sono uguali, e con l'ordine dal centro vince sempre chi comincia, in 7 mosse. Perché sono tutte uguali? Disegna la partita.
#   c. quante volte hai scritto il controllo delle file, in questo programma? Che cosa cambia fra una copia e l'altra? È il problema che in L08 risolvono le funzioni.

import numpy as np

# --- dati ----------------------------------------------------------------------

righe = 6
colonne = 7
partite = 1000

# le colonne nell'ordine in cui il migliore le prova, numerate da 1
ordine = [1, 2, 3, 4, 5, 6, 7]
# ordine = [4, 3, 5, 2, 6, 1, 7]

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
# c.
