# -*- coding: utf-8 -*-
# Challenge L09 - Quanti saremo
#
# Il file ha due parti.
#
# PARTE PRIMA, le challenge 1-6, ha la forma dell'esame: funzioni numerate, già dichiarate, da completare. Il commento sopra ogni funzione dice che cosa riceve, che cosa restituisce e un esempio. Il corpo principale del programma, in fondo alla parte prima, è già scritto: chiama le tue funzioni e stampa i risultati. Puoi aggiungere altre funzioni, se ti servono.
#
# PARTE SECONDA, le challenge 7-10, è libera: scrivi tu le funzioni che ti servono e il codice che le usa.
#
# Alle domande di ragionamento, in fondo al file, rispondi nei commenti.
#
# Alla fine `python3 ch_ISTAT.py`, da un terminale appena aperto, non deve dare errori.

import pathlib as pl

nomeEsercizio = "ISTAT"

"""
### I dati

Il file `previsioniISTAT2017.csv` contiene le previsioni probabilistiche della popolazione residente in Italia, per sesso ed età, fatte dall'ISTAT con base 1° gennaio 2017, anno per anno dal 2017 al 2065. Separatore `;`, codifica UTF-8.

Il file è fatto a blocchi:

    "Previsioni probabilistiche della popolazione residente per sesso, età e regione - base 1.1.2017 - Anni 2017/2065"
    "Anno: 2017 - Ripartizione: Italia"
    "Maschi"
    "Età";"Limite inferiore intervallo di confidenza al 90% (5° percentile)";...
    0;240100;240100;240100;240100;240100;240100;240100;
    1;249511;249511;249511;249511;249511;249511;249511;
    ...
    110 e oltre;...
    Totale;...
    "Femmine"
    ...

Per ogni anno ci sono tre blocchi: "Maschi", "Femmine" e "Totale". Ogni blocco ha la sua intestazione di colonne, una riga per età da 0 a "110 e oltre", e una riga "Totale".

Ogni riga di dati ha l'età e sette valori, i percentili degli scenari simulati: il 5°, il 10°, il 25°, la mediana, il 75°, il 90° e il 95°. Nel codice le sette colonne sono numerate da 0 a 6; la mediana è la colonna 3.
"""

fName = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data" / "previsioniISTAT2017.csv"

dSessi = {'"Maschi"': "maschi", '"Femmine"': "femmine", '"Totale"': "totale"}
iMediana = 3


##########################################################
# PARTE PRIMA - le challenge 1-6, in forma d'esame
##########################################################

"""
1a. La funzione `tipoRiga(sRiga_IN)` accetta una riga del file, come stringa, e restituisce una stringa con il suo tipo: "titolo", "anno", "sesso", "intestazione", "dato" o "totale".
Ad esempio dalla riga "Anno: 2030 - Ripartizione: Italia", fra virgolette come nel file, si ottiene "anno"; da "12;600120;...;" si ottiene "dato".
"""
def tipoRiga(sRiga_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
1b. La funzione `contaTipi(fName_IN)` accetta il percorso del file e restituisce un dizionario che a ogni tipo di riga, come lo restituisce `tipoRiga`, associa il numero di righe di quel tipo.
Ad esempio {'titolo': 1, 'anno': ..., 'sesso': ..., 'intestazione': ..., 'dato': ..., 'totale': ...}
"""
def contaTipi(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
2. La funzione `leggiRiga(sRiga_IN)` accetta una riga di dati o la riga "Totale" e restituisce una tupla (eta, valori): `eta` è un intero, `valori` una tupla dei sette valori interi. La riga "110 e oltre" ha età 110; per la riga "Totale" l'età resta la stringa "Totale".
Ad esempio dalla riga "0;240100;240100;240100;240100;240100;240100;240100;\n" si ottiene (0, (240100, 240100, 240100, 240100, 240100, 240100, 240100))
"""
def leggiRiga(sRiga_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
3. La funzione `caricaPrevisioni(fName_IN)` accetta il percorso del file, usa `tipoRiga` e `leggiRiga`, e restituisce una tupla di due dizionari (dPrevisioni, dTotali):
    * dPrevisioni[anno][sesso][eta] è la tupla dei sette valori; l'anno è un intero, il sesso è "maschi", "femmine" o "totale";
    * dTotali[anno][sesso] è la tupla dei sette valori della riga "Totale" di quel blocco.
Ad esempio dPrevisioni[2017]["maschi"][0] vale (240100, 240100, 240100, 240100, 240100, 240100, 240100)
"""
def caricaPrevisioni(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
4a. La funzione `somma(dBlocco_IN, iColonna_IN)` accetta un blocco, cioè un dizionario età -> tupla dei sette valori come dPrevisioni[anno][sesso], e il numero di una colonna da 0 a 6, e restituisce la somma di quella colonna su tutte le età.
Ad esempio somma({0: (1, 2, 3, 4, 5, 6, 7), 1: (10, 20, 30, 40, 50, 60, 70)}, 3) restituisce 44
"""
def somma(dBlocco_IN, iColonna_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
4b. La funzione `contaSessiDiversi(dPrevisioni_IN)` accetta il primo dizionario restituito da `caricaPrevisioni` e restituisce un intero: il numero di coppie (anno, età) in cui, nello scenario mediano, maschi più femmine non fa il totale.
"""
def contaSessiDiversi(dPrevisioni_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
4c. La funzione `scarto(dPrevisioni_IN, dTotali_IN, iAnno_IN, sSesso_IN, iColonna_IN)` restituisce un intero: la somma delle età della colonna data, per quell'anno e quel sesso, meno il valore della riga "Totale" nella stessa colonna.
Ad esempio per il 2017, il totale e qualunque colonna restituisce 0
"""
def scarto(dPrevisioni_IN, dTotali_IN, iAnno_IN, sSesso_IN, iColonna_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
5. La funzione `salvaAnno(dPrevisioni_IN, iAnno_IN, sCartella_IN)` scrive nella cartella data un file `proiezioneISTAT2017_ANNO.csv`, con l'intestazione `eta,maschi,femmine,totale,anno` e una riga per età, con lo scenario mediano. La cartella va creata se non c'è. La funzione restituisce il percorso del file scritto.
Ad esempio il file del 2050 comincia con le righe
    eta,maschi,femmine,totale,anno
    0,224007,210806,434813,2050
"""
def salvaAnno(dPrevisioni_IN, iAnno_IN, sCartella_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
6a. La funzione `popolazione(dBlocco_IN, iDa_IN, iA_IN, iColonna_IN=3)` restituisce un intero: le persone del blocco con età fra iDa_IN e iA_IN, estremi compresi, nella colonna data, che se non è indicata è la mediana.
Ad esempio popolazione(dPrevisioni[2017]["totale"], 0, 14) restituisce 8182584
"""
def popolazione(dBlocco_IN, iDa_IN, iA_IN, iColonna_IN=3):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
6b. La funzione `indicatori(dBlocco_IN)` restituisce una tupla di due float, calcolati sullo scenario mediano:
    * l'indice di vecchiaia: le persone di 65 anni e più, ogni 100 sotto i 15;
    * l'indice di dipendenza: le persone sotto i 15 e sopra i 64, ogni 100 fra i 15 e i 64.
Ad esempio indicatori(dPrevisioni[2017]["totale"]) restituisce circa (165.3, 55.8)
"""
def indicatori(dBlocco_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
6c. La funzione `etaMediana(dBlocco_IN)` restituisce un intero: l'età mediana dello scenario mediano, cioè la prima età alla quale le persone di quell'età o più giovani superano la metà del totale.
Ad esempio etaMediana(dPrevisioni[2017]["totale"]) restituisce 45
"""
def etaMediana(dBlocco_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


##########################################################
# Corpo principale della parte prima: già scritto.
# Puoi modificarlo, ma deve girare senza errori.
##########################################################

print(f"Challenge {nomeEsercizio}.")

print("\nEs. 1)\n")
print(tipoRiga('"Anno: 2030 - Ripartizione: Italia"\n'))
print(tipoRiga("12;600120;600120;600120;600120;600120;600120;600120;\n"))
print(contaTipi(fName))

print("\nEs. 2)\n")
print(leggiRiga("0;240100;240100;240100;240100;240100;240100;240100;\n"))
print(leggiRiga("110 e oltre;12;21;56;136;371;827;1254;\n"))
print(leggiRiga("Totale;46431633;48029882;50789729;54086662;57275541;60189489;61964654;\n"))

print("\nEs. 3)\n")
dPrevisioni, dTotali = caricaPrevisioni(fName)
print(len(dPrevisioni), min(dPrevisioni), max(dPrevisioni))
print(dPrevisioni[2030]["femmine"][100])
print(dTotali[2065]["totale"])

print("\nEs. 4)\n")
print(somma({0: (1, 2, 3, 4, 5, 6, 7), 1: (10, 20, 30, 40, 50, 60, 70)}, 3))
print(contaSessiDiversi(dPrevisioni))
iScartoMassimo = 0
for iAnno in dPrevisioni:
    for sSesso in dPrevisioni[iAnno]:
        iScarto = abs(scarto(dPrevisioni, dTotali, iAnno, sSesso, iMediana))
        if iScarto > iScartoMassimo:
            iScartoMassimo = iScarto
print(iScartoMassimo)
for iAnno in [2017, 2065]:
    lScarti = []
    for iColonna in range(7):
        lScarti.append(scarto(dPrevisioni, dTotali, iAnno, "totale", iColonna))
    print(iAnno, lScarti)

print("\nEs. 5)\n")
pCartella = pl.Path(__file__).parent / "proiezioni"
for iAnno in dPrevisioni:
    salvaAnno(dPrevisioni, iAnno, pCartella)
print(len(list(pCartella.glob("*.csv"))))
print((pCartella / "proiezioneISTAT2017_2050.csv").read_text(encoding="utf-8").splitlines()[:2])

print("\nEs. 6)\n")
for iAnno in [2017, 2030, 2050, 2065]:
    fVecchiaia, fDipendenza = indicatori(dPrevisioni[iAnno]["totale"])
    print(iAnno, round(fVecchiaia, 1), round(fDipendenza, 1), etaMediana(dPrevisioni[iAnno]["totale"]))


##########################################################
# PARTE SECONDA - le challenge 7-10, libere
#
# Usa dPrevisioni e dTotali, già caricati qui sopra, e le funzioni della parte prima. Le funzioni nuove scrivile qui, prima del codice che le usa.
##########################################################

# Challenge 7 - La traiettoria (difficoltà: 3/3)
#
# Le righe "Totale" di dTotali danno, per ogni anno, la popolazione italiana prevista con il suo intervallo: il 5° e il 95° percentile racchiudono il 90% degli scenari. Stampa la popolazione ogni otto anni, dal 2017 al 2065, con l'intervallo. Poi trova l'anno in cui lo scenario mediano è più alto.

print("\nChallenge 7\n")



# Challenge 8 - Quanto è incerta (difficoltà: 3/3)
#
# L'ampiezza relativa dell'intervallo è (95° percentile - 5° percentile) / mediana, in percentuale: dice quanto è larga l'incertezza rispetto al valore previsto. Calcolala sul totale, per gli anni 2018, 2030, 2050 e 2065; e nel 2065, per ogni età, trova le età con l'incertezza più piccola.

print("\nChallenge 8\n")



# Challenge 9 - Il conto che non torna (difficoltà: 3/3)
#
# L'Es. 4 ha lasciato una domanda: nel 2065 la somma dei 5° percentili per età non fa il 5° percentile del totale. Stampa, per il 2030 e il 2065, la somma per età del 5° e del 95° percentile, accanto ai valori della riga "Totale".

print("\nChallenge 9\n")



# Challenge 10 - Dal 2017 al 2050 (difficoltà: 3/3)
#
# Il primo giorno del corso, in L01, c'era una domanda: «Come varierà la distribuzione della popolazione, stratificata per genere, dal 2017 al 2050?». Ora hai gli strumenti per rispondere.
#
#   - raggruppa le età in classi di cinque anni, "0-4", "5-9", fino a "95-99", e una classe "100+";
#   - stampa la piramide delle età del 2017 e del 2050: una riga per classe, dall'alto in basso, i maschi a sinistra e le femmine a destra, un carattere # ogni 100 000 persone;
#   - salva un file piramidi.csv con l'intestazione anno,sesso,classe,popolazione e una riga per anno, sesso e classe;
#   - confronta le classi del 2017 e del 2050.
#
# Il CSV non è fine a sé stesso: quando arriverà pandas, piramidi.csv e i file dell'Es. 5 si leggeranno con una riga, e la piramide diventerà un grafico.

print("\nChallenge 10\n")



##########################################################
# DOMANDE DI RAGIONAMENTO - rispondi nei commenti
##########################################################
#
# 1a. Quante righe ha ciascun tipo? Controlla almeno due conti con `grep -c` nel terminale.
# 1b. Quante righe di dati ha ogni blocco, cioè ogni anno e sesso? Perché proprio quel numero?
#
# 2a. Che cosa restituisce `split(";")` su una riga di dati, dopo `strip()`? Quanti pezzi, e perché l'ultimo è vuoto? E senza `strip()`?
# 2b. Che cosa succede con `int("110 e oltre")`? Che cosa si perde trasformandolo in 110?
#
# 3a. Il conto: quanti anni, quanti blocchi, quante età per blocco ha la tua struttura? Tornano con l'Es. 1?
# 3b. Perché la riga "Totale" sta in un dizionario a parte, e non in dPrevisioni come se fosse un'età?
#
# 4a. Nel 2017 tutto torna, in tutte le colonne. Perché il 2017 è diverso dagli altri anni? Guarda i sette valori di una riga qualsiasi del 2017.
# 4b. Per la mediana le differenze ci sono, ma sono minuscole. Di quanto, al massimo? Da dove vengono?
# 4c. Nel 2065, per il 5° e il 95° percentile, la differenza è di più di un milione. Tieni la domanda per la challenge 9.
#
# 5a. Quanti file hai scritto? Controlla con `ls proiezioni | wc -l`.
# 5b. L'anno sta sia nel nome del file sia in una colonna. A che cosa serve la colonna, se c'è già nel nome?
#
# 6a. In che anno l'indice di vecchiaia è più alto? E quello di dipendenza? Per rispondere aggiungi tu il codice, in fondo al corpo principale della parte prima.
# 6b. L'età mediana cresce di quanti anni dal 2017 al 2065? Che cosa vuol dire, in parole?
#
# 7a. In che anno la popolazione mediana tocca il massimo? Quanto si perde dal massimo al 2065?
# 7b. La popolazione del 2017 sta dentro l'intervallo al 90% del 2065? Che cosa vuol dire per la frase «la popolazione italiana calerà»?
#
# 8a. Come cresce l'incertezza con gli anni?
# 8b. Nel 2065, quali sono le età più certe? Quanti anni avevano nel 2017? Perché proprio loro, e non i bambini?
#
# 9a. Quale dei due numeri è più piccolo, per il 5° percentile? Perché sommare i casi peggiori di ogni età non dà il caso peggiore del totale?
# 9b. A qualcuno serve sapere quanti saremo nel 2065 «nel caso peggiore». Quale dei due numeri gli dai, e perché?
#
# 10a. Rispondi alla domanda di L01 in tre o quattro righe, con i numeri che hai trovato.
# 10b. Quale classe cresce di più in proporzione, e quale cala di più?
# 10c. Fra gli ultraottantacinquenni, quante donne ci sono per ogni uomo nel 2017? E nel 2050? Perché il rapporto cambia?
#
# 1a.
# 1b.
# 2a.
# 2b.
# 3a.
# 3b.
# 4a.
# 4b.
# 5a.
# 5b.
# 6a.
# 6b.
# 7a.
# 7b.
# 8a.
# 8b.
# 9a.
# 9b.
# 10a.
# 10b.
# 10c.
