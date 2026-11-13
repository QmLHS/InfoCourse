# Challenge 2 - Una pedina che cade (difficoltà: 1/3)
#
# La griglia nei dati è a metà partita, e tocca a `pedina`. Il giocatore sceglie la colonna `scelta`, numerata da 1 come sullo schermo. La pedina cade fino alla casella vuota più in basso di quella colonna: cercala partendo dal fondo e salendo con un `while`, mettici la pedina e stampa la griglia.
#
# Se la colonna è piena, la pedina non si mette: il programma lo dice e lascia la griglia com'è.
#
# Controllo: con `scelta = 3` la pedina cade nella riga 3, con la 5 nella riga 5, con la 2 nella riga 4; la colonna 4 è piena. Prova tutti e quattro i valori.
#
# Rispondi nei commenti in fondo:
#
#   a. nella condizione del `while` togli il controllo che la riga non sia sotto lo zero, e prova la colonna 4. Che errore dà, e dopo quanti giri? Perché non subito, quando la riga arriva a -1?
#   b. come fai a sapere che una colonna è piena guardando una casella sola, senza cercare?
#   c. se tenessi una lista `altezze`, con il numero di pedine di ogni colonna, la ricerca non servirebbe: in che riga cade la pedina, quando la colonna è piena, e come tieni aggiornata la lista?

# --- dati ----------------------------------------------------------------------

griglia = [
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'O', '.', '.', '.'],
    ['.', '.', '.', 'X', '.', '.', '.'],
    ['.', '.', '.', 'O', '.', '.', '.'],
    ['.', '.', 'X', 'X', '.', '.', '.'],
    ['.', 'X', 'O', 'O', '.', '.', 'O'],
]
pedina = 'X'

scelta = 3
# scelta = 5
# scelta = 2
# scelta = 4

# --- il tuo codice -------------------------------------------------------------



# --- risposte ------------------------------------------------------------------
# a.
# b.
# c.
