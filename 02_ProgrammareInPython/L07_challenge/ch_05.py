# Challenge 5 - Le diagonali, e una direzione sola (difficoltà: 2/3)
#
# Aggiungi le due diagonali: verso il basso a destra e verso l'alto a destra. Scritte come nella 4, le direzioni diventano quattro pezzi di codice quasi uguali.
#
# Riscrivi allora il controllo con una direzione sola: una direzione è una coppia (passo sulle righe, passo sulle colonne), per esempio (0, 1) è «a destra» e (1, 0) è «in giù». Metti le quattro direzioni in una lista di tuple e percorrila con un `for`: il codice che guarda le quattro caselle si scrive una volta sola.
#
# Controllo: nel primo blocco vince X in diagonale verso l'alto, nel secondo O in diagonale verso il basso, nel terzo nessuno; i blocchi della challenge 4 devono dare gli stessi risultati di prima.
#
# Rispondi nei commenti in fondo:
#
#   a. qual è la coppia della diagonale verso l'alto a destra? Perché non serve controllare anche le direzioni verso sinistra?
#   b. il controllo che la quarta casella non esca dalla griglia ha più parti. Togli quella che guarda la riga sotto lo zero e prova l'ultimo blocco: chi vince? Guarda la griglia: ha ragione il programma? Perché Python non dà errore?

# --- dati ----------------------------------------------------------------------

# vince X, in diagonale verso l'alto
griglia = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', 'X', 'O', '.', '.', '.'],
    ['.', 'X', 'O', 'O', '.', '.', '.'],
    ['X', 'O', 'X', 'O', 'X', '.', '.'],
]

# vince O, in diagonale verso il basso
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 'O', '.', '.', '.'],
#     ['.', '.', '.', 'X', 'O', '.', '.'],
#     ['.', '.', '.', 'X', 'X', 'O', '.'],
#     ['O', '.', 'X', 'X', 'O', 'X', 'O'],
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

# nessuno, e serve alla domanda b
# griglia = [
#     ['.', 'O', 'O', '.', '.', '.', 'X'],
#     ['O', 'O', 'X', '.', '.', '.', 'X'],
#     ['X', 'X', 'O', '.', '.', '.', 'X'],
#     ['O', 'O', 'O', 'X', 'O', '.', 'O'],
#     ['X', 'X', 'X', 'O', 'O', '.', 'X'],
#     ['X', 'O', 'X', 'O', 'X', 'X', 'O'],
# ]

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
