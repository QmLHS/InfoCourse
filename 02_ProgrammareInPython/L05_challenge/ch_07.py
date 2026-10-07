# Challenge 7 - Che giorno della settimana (difficoltà: 3/3)
#
# Il dataset non dice che giorno della settimana fosse. Lo si calcola con la
# congruenza di Zeller (1882), che usa solo divisione intera e resto:
#
#   h = (g + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7
#
# dove
#
#   g   è il giorno del mese
#   m   è il mese, ma contato da MARZO = 3 fino a FEBBRAIO = 14:
#       gennaio e febbraio sono i mesi 13 e 14 dell'anno PRECEDENTE
#   K   sono le ultime due cifre dell'anno (quello eventualmente corretto)
#   J   sono le prime due cifre dell'anno (idem)
#
# e h vale 0 per sabato, 1 per domenica, 2 per lunedì, ... 6 per venerdì.
#
# Stampa il nome del giorno, in italiano.
#
# Verifiche: il 1° gennaio 2011 era un sabato. Il 20 ottobre 2026, il giorno
# di questa sessione, è un martedì.
#
# Rispondi nei commenti in fondo:
#
#   a. che cosa ottieni per il 1° gennaio 2011 se dimentichi di spostare
#      gennaio e febbraio all'anno prima? Perché il programma non se ne
#      accorge?
#   b. perché secondo te Zeller ha scelto di far cominciare l'anno a marzo?
#      (Pensa a quale mese ha una lunghezza diversa dagli altri.)

# --- dati --------------------------------------------------------------------

anno, mese, giorno = 2011, 1, 1         # atteso: sabato

# anno, mese, giorno = 2026, 10, 20     # atteso: martedì
# anno, mese, giorno = 2000, 2, 29      # atteso: martedì

# --- il tuo codice -----------------------------------------------------------



# --- risposte ----------------------------------------------------------------
# a.
# b.
