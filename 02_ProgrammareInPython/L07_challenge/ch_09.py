# Challenge 9 - Il computer furbo (difficoltà: 3/3)
#
# Il computer 'furbo' prima di muovere prova tutte le colonne: se in una vince subito, gioca lì; altrimenti, se in una vincerebbe subito l'avversario, gioca lì per bloccarlo; altrimenti gioca a caso. Per provare una colonna si mette la pedina, si usa il controllo della 8, e si toglie la pedina.
#
# Fai giocare il furbo contro un giocatore a caso per `partite` partite e stampa quante ne vince ciascuno e quante sono patte. Prova il furbo prima per secondo e poi per primo.
#
# Controllo: il furbo vince circa il 95% delle partite quando gioca per secondo, e circa il 97% quando comincia.
#
# Rispondi nei commenti in fondo:
#
#   a. perché bisogna togliere la pedina di prova? Che cosa succede se te ne dimentichi?
#   b. il furbo blocca sempre una mossa vincente dell'avversario, eppure a volte perde. Come? Disegna una griglia in cui il furbo non può evitare di perdere.

import numpy as np

# --- dati ----------------------------------------------------------------------

righe = 6
colonne = 7
partite = 1000

furbo = 'O'          # il furbo gioca per secondo
# furbo = 'X'        # il furbo comincia

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
