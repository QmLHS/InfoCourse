# Challenge 5 - Il freddo percepito (difficoltà: 2/3)
#
# In aula abbiamo visto la formula del wind chill, la temperatura percepita
# per effetto del vento:
#
#   percepita = 13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16
#
# con t in gradi Celsius e v in km/h. Quello che in aula non abbiamo detto è
# che la formula vale SOLO quando fa freddo e c'è vento:
#
#   t <= 10   e   v > 4.8
#
# Fuori da questo campo dà comunque un numero, ma è un numero senza senso.
#
# Usa la minima e il vento massimo, il caso peggiore della giornata. Il
# programma stampa la temperatura percepita con una cifra decimale quando la
# formula si può applicare. Quando non si può, dice perché: troppo caldo,
# troppo poco vento, o entrambe le cose.
#
# Provalo su tutte e tre le giornate.
#
# Rispondi nei commenti in fondo:
#
#   a. che cosa stampa il 15 luglio se togli il controllo? Ha senso?
#   b. scegli tu una giornata in cui MANCANO ENTRAMBE le condizioni, e
#      verifica che il programma le dica tutte e due.

# --- dati: MeteoMilano2011.csv -----------------------------------------------

data = "2011-01-13"
tmin = -3           # Temperatura minC
vento_max = 11      # Max Velocità del ventoKm/h

# data = "2011-11-15"
# tmin = -3
# vento_max = 3

# data = "2011-07-15"
# tmin = 17
# vento_max = 8

# --- il tuo codice -----------------------------------------------------------



# --- risposte ----------------------------------------------------------------
# a.
# b.
