# Challenge 4 - Quattro in fila: orizzontale e verticale (difficoltà: 2/3)
#
# Data una griglia, c'è un vincitore? Vince chi ha quattro pedine uguali di fila. In questa challenge solo in orizzontale e in verticale: le diagonali sono la 5.
#
# Per ogni casella con una pedina, guarda le tre caselle alla sua destra e le tre sotto. Parti solo dalle caselle da cui le quattro non escono dalla griglia. Il programma stampa chi vince, o che non vince nessuno.
#
# Controllo: nel primo blocco vince X, nel secondo O, nel terzo nessuno.
#
# Rispondi nei commenti in fondo:
#
#   a. da quali colonne può cominciare una fila orizzontale di quattro? Scrivi il `range` che hai usato e spiega da dove viene il numero.
#   b. fai partire il ciclo orizzontale da tutte le colonne, con `range(colonne)`. Che errore dà? Basterebbe una griglia vuota per vederlo?
#   c. e se la griglia contenesse numeri, 0 per la casella vuota, 2 e 9 per i due giocatori? Per sapere se quattro caselle sono di uno stesso giocatore basterebbe sommarle: quali somme cerchi? Perché proprio 2 e 9, e non 1 e 2?

# --- dati ----------------------------------------------------------------------

# vince X, in orizzontale, in fondo a destra
griglia = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'O', 'O', '.', '.'],
    ['.', '.', 'O', 'X', 'X', 'X', 'X'],
]

# vince O, in verticale
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['O', '.', '.', '.', '.', '.', '.'],
#     ['O', '.', '.', '.', '.', '.', '.'],
#     ['O', 'X', '.', '.', '.', '.', '.'],
#     ['O', 'X', 'X', '.', '.', '.', 'X'],
# ]

# nessuno
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 'X', '.', '.', '.'],
#     ['.', '.', 'O', 'O', '.', '.', '.'],
#     ['.', 'X', 'X', 'O', '.', '.', '.'],
#     ['O', 'X', 'O', 'X', 'X', '.', 'O'],
# ]

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
# c.
