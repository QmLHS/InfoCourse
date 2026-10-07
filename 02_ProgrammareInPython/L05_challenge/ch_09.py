# Challenge 9 - Il dato sporco (difficoltà: 3/3)
#
# Finora i dati erano già numeri. Nel file però sono TESTO, e non sempre ci
# sono: qui sotto la riga è come la leggerebbe un programma, campo per campo,
# tutto fra virgolette.
#
# Scrivi un controllo della riga che segnali OGNI problema che trova, non
# solo il primo:
#
#   - una temperatura vuota è un dato mancante;
#   - se ci sono tutte e due, la minima non può superare la massima;
#   - l'umidità, se c'è, sta fra 0 e 100;
#   - la raffica vuota NON è un errore: nel 2011 manca in 341 giorni su
#     365, semplicemente non veniva misurata. Se c'è, però, non può essere
#     più debole del vento massimo;
#   - la direzione "-1" non è un errore e non è un angolo (challenge 4);
#     qualunque altro valore deve stare fra 0 e 360.
#
# Alla fine il programma stampa quanti problemi ha trovato, oppure che la
# riga è valida.
#
# Usa int() per convertire, e solo quando puoi.
#
# Prova tutte e tre le righe. La terza non viene dal file: l'abbiamo inventata
# noi per farla sbagliare in tutti i modi possibili.
#
# Rispondi nei commenti in fondo:
#
#   a. che cosa succede se chiami int() su una stringa vuota? E perché il
#      tuo programma non ci arriva mai?
#   b. perché qui non va bene una catena di elif dall'inizio alla fine?
#   c. la raffica vuota e la direzione -1 non sono errori ma sono comunque
#      «dati che mancano». Il tuo programma li distingue dagli errori veri?

# --- dati: MeteoMilano2011.csv, come testo ------------------------------------

data = "2011-01-16"
tmax = ""
tmin = ""
umidita_max = ""
vento_max = "8"
raffica_max = ""
direzione = "330"

# data = "2011-01-01"
# tmax = "6"
# tmin = "-4"
# umidita_max = "100"
# vento_max = "8"
# raffica_max = ""
# direzione = "225"

# data = "riga inventata"
# tmax = "6"
# tmin = "8"
# umidita_max = "104"
# vento_max = "8"
# raffica_max = "5"
# direzione = "400"

# --- il tuo codice -----------------------------------------------------------



# --- risposte ----------------------------------------------------------------
# a.
# b.
# c.
