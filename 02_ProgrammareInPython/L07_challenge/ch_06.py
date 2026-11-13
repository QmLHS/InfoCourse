# Challenge 6 - La griglia è possibile? (difficoltà: 2/3)
#
# Prima di chiedersi chi ha vinto, c'è una domanda che il testo di un esercizio di solito non fa: questa griglia può uscire da una partita vera?
#
# Controlla due cose: nessuna pedina è sospesa, cioè sotto ogni pedina c'è un'altra pedina o il fondo; le pedine dei due giocatori sono tante quante, o c'è una 'X' in più, perché comincia 'X'. Il programma stampa se la griglia è possibile e, se non lo è, perché.
#
# Controllo: il primo blocco è possibile, il secondo ha una pedina sospesa, il terzo ha più 'O' che 'X'. Gli ultimi due passano tutti e due i controlli: servono alle domande.
#
# Rispondi nei commenti in fondo:
#
#   a. nel quarto blocco vincono tutti e due. Può succedere in una partita vera?
#   b. nel quinto blocco vince 'X' e le pedine sono quattro e quattro. È possibile? Usa la challenge 5 per aggiungere il controllo che manca: chi ha vinto, e quante pedine deve avere in più o in meno.

# --- dati ----------------------------------------------------------------------

# possibile
griglia = [
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', 'O', 'O', '.', '.', '.'],
    ['.', 'X', 'X', 'O', '.', '.', '.'],
    ['O', 'X', 'O', 'X', 'X', '.', 'O'],
]

# una pedina sospesa
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', 'X', '.'],
#     ['.', '.', '.', 'X', '.', '.', '.'],
#     ['.', '.', 'O', 'O', '.', '.', '.'],
#     ['.', 'X', 'X', 'O', '.', '.', '.'],
#     ['O', 'X', 'O', 'X', 'X', '.', 'O'],
# ]

# più O che X
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 'X', '.', '.', '.'],
#     ['.', '.', 'O', 'O', '.', '.', '.'],
#     ['.', 'X', 'X', 'O', '.', '.', '.'],
#     ['O', 'X', 'O', 'X', 'X', 'O', 'O'],
# ]

# passa i due controlli: domanda a
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', 'O', '.', '.'],
#     ['.', '.', '.', '.', 'O', '.', '.'],
#     ['.', '.', '.', '.', 'O', '.', '.'],
#     ['X', 'X', 'X', 'X', 'O', '.', '.'],
# ]

# passa i due controlli: domanda b
# griglia = [
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', 'O', 'O', 'O', '.'],
#     ['.', '.', 'O', 'X', 'X', 'X', 'X'],
# ]

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
