# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

nomeEsercizio = "iscrittiAtenei"

strutturaDati = {
    '01501': {'nome': 'Milano - Università degli studi',
              'laurea':    {'2008-2009': 58093, '2009-2010': 58279, '2010-2011': 59890, '2011-2012': 59770, '2012-2013': 58865},
              'dottorato': {'2008-2009': 1548, '2009-2010': 1464, '2010-2011': 1374, '2011-2012': 1332, '2012-2013': 1388}},
    '01502': {'nome': 'Milano - Politecnico',
              'laurea':    {'2008-2009': 35434, '2009-2010': 35451, '2010-2011': 36722, '2011-2012': 37626, '2012-2013': 38807},
              'dottorato': {'2008-2009': 851, '2009-2010': 914, '2010-2011': 980, '2011-2012': 1123, '2012-2013': 1073}},
    '01503': {'nome': 'Milano - Università commerciale "Luigi Bocconi"',
              'laurea':    {'2008-2009': 12927, '2009-2010': 12925, '2010-2011': 13065, '2011-2012': 13342, '2012-2013': 13290},
              'dottorato': {'2008-2009': 123, '2009-2010': 140, '2010-2011': 125, '2011-2012': 121, '2012-2013': 128}},
    '01504': {'nome': 'Milano - Università Cattolica del "Sacro Cuore"',
              'laurea':    {'2008-2009': 39974, '2009-2010': 40429, '2010-2011': 40121, '2011-2012': 39888, '2012-2013': 39137},
              'dottorato': {'2008-2009': 755, '2009-2010': 689, '2010-2011': 675, '2011-2012': 651, '2012-2013': 618}},
    '01505': {'nome': 'Milano - Libera Università di Lingue e Comunicazione (IULM)',
              'laurea':    {'2008-2009': 4845, '2009-2010': 4423, '2010-2011': 4361, '2011-2012': 4307, '2012-2013': 4179},
              'dottorato': {'2008-2009': 51, '2009-2010': 57, '2010-2011': 59, '2011-2012': 54, '2012-2013': 48}},
    '01508': {'nome': 'Milano - Università Vita-Salute San Raffaele',
              'laurea':    {'2008-2009': 1911, '2009-2010': 1968, '2010-2011': 1942, '2011-2012': 1972, '2012-2013': 1986},
              'dottorato': {'2008-2009': 187, '2009-2010': 191, '2010-2011': 185, '2011-2012': 171, '2012-2013': 156}},
    '01509': {'nome': 'Milano-Bicocca - Università degli studi',
              'laurea':    {'2008-2009': 29861, '2009-2010': 30725, '2010-2011': 30692, '2011-2012': 33142, '2012-2013': 32923},
              'dottorato': {'2008-2009': 645, '2009-2010': 653, '2010-2011': 653, '2011-2012': 596, '2012-2013': 589}},
    '01510': {'nome': 'Milano - Università telematica internazionale "UNITEL"',
              'laurea':    {'2008-2009': 159, '2009-2010': 262},
              'dottorato': {'2008-2009': 0, '2009-2010': 0}},
    '01601': {'nome': 'Bergamo - Università degli studi',
              'laurea':    {'2008-2009': 14093, '2009-2010': 14729, '2010-2011': 14615, '2011-2012': 14424, '2012-2013': 14853},
              'dottorato': {'2008-2009': 201, '2009-2010': 239, '2010-2011': 284, '2011-2012': 277, '2012-2013': 272}},
    '01701': {'nome': 'Brescia - Università degli studi',
              'laurea':    {'2008-2009': 14132, '2009-2010': 14512, '2010-2011': 14457, '2011-2012': 14310, '2012-2013': 14209},
              'dottorato': {'2008-2009': 184, '2009-2010': 186, '2010-2011': 200, '2011-2012': 204, '2012-2013': 226}},
    '01801': {'nome': 'Pavia - Università degli studi',
              'laurea':    {'2008-2009': 22061, '2009-2010': 22210, '2010-2011': 22148, '2011-2012': 21610, '2012-2013': 21496},
              'dottorato': {'2008-2009': 639, '2009-2010': 643, '2010-2011': 662, '2011-2012': 617, '2012-2013': 603}},
    '01802': {'nome': 'Pavia - Istituto universitario di studi superiori',
              'laurea':    {'2008-2009': 0, '2009-2010': 0, '2010-2011': 0, '2011-2012': 0, '2012-2013': 0},
              'dottorato': {'2008-2009': 49, '2009-2010': 49, '2010-2011': 54, '2011-2012': 62, '2012-2013': 76}},
}

"""
### Esercizio

L'esercizio riguarda gli iscritti agli atenei della Lombardia, dall'anno accademico 2008-2009 al 2012-2013.
Sono gli stessi dati del file `2009-2013_iscritti.csv` delle esercitazioni precedenti, solo le righe «Totale iscritti».

Le informazioni sono immagazzinate in un dizionario di dizionari (`strutturaDati`) avente la seguente struttura:
    ```python
    {
        codiceAteneo_1: {
            "nome": nomeAteneo_1,
            "laurea": {annoAccademico_1: iscritti_1, annoAccademico_2: iscritti_2, ...},
            "dottorato": {annoAccademico_1: iscritti_1, annoAccademico_2: iscritti_2, ...},
        },
        codiceAteneo_2: { ... },
        ...
        codiceAteneo_n: { ... },
    }
    ```
    A ciascun ateneo corrisponde una chiave del dizionario esterno ed un dizionario interno strutturato
    nel seguente modo:
    * `codiceAteneo_i` - stringa - e' il codice dell'ateneo, di cinque cifre, ed e' la chiave del dizionario esterno;
    * `nomeAteneo_i` - stringa - e' il nome dell'ateneo, nella forma "Citta' - nome dell'ateneo";
    * `"laurea"` - dizionario - associa a ogni anno accademico il numero di iscritti ai corsi di laurea;
    * `"dottorato"` - dizionario - associa a ogni anno accademico il numero di iscritti ai corsi di dottorato;
    * `annoAccademico_i` - stringa - e' l'anno accademico nel formato "AAAA-AAAA";
    * `iscritti_i` - intero - e' il numero di iscritti in quell'anno.

Non tutti gli atenei hanno i dati di tutti gli anni.

Rispondete alle domande qui sotto, scrivendo il codice sotto ciascuna domanda.
Il programma deve funzionare anche se strutturaDati contenesse altri atenei o altri anni:
non scrivete a mano i valori che potete ricavare dalla struttura.
"""


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################


"""
1. Quanti atenei ci sono in `strutturaDati`? Stampate il numero.
"""


"""
2. Stampate il nome dell'ateneo con codice '01509', e il numero dei suoi iscritti
ai corsi di laurea nell'anno accademico 2012-2013.
"""


"""
3. Di che tipo e' ciascun livello della struttura? Stampate il tipo di
`strutturaDati`, di `strutturaDati['01509']`, di `strutturaDati['01509']['laurea']`
e di `strutturaDati['01509']['laurea']['2012-2013']`.
"""


"""
4. Per ogni ateneo, stampate su una riga il nome e il numero di iscritti ai corsi
di laurea nell'anno accademico 2012-2013.
"""


"""
5. Costruite la lista `milanesi`, che contiene i nomi degli atenei con sede a Milano,
e stampatela insieme alla sua lunghezza.
"""


"""
6. Costruite il dizionario `totali`, che associa a ogni anno accademico il numero
totale di iscritti ai corsi di laurea in tutti gli atenei della struttura, e stampatelo.
"""


"""
7. Costruite il dizionario `variazioni`, che associa al codice di ogni ateneo la variazione
percentuale degli iscritti ai corsi di laurea fra il 2008-2009 e il 2012-2013:

    variazione = (iscritti 2012-2013 - iscritti 2008-2009) / iscritti 2008-2009 * 100

Stampate, per ogni ateneo del dizionario, il nome e la variazione con un decimale.
"""


"""
8. Costruite il dizionario `perCitta`, che associa a ogni citta' la lista delle tuple
(nome dell'ateneo, iscritti ai corsi di laurea nel 2012-2013) degli atenei che vi hanno sede.
La citta' e' la parte del nome che precede il trattino.
Stampate le citta' e, per ciascuna, quanti atenei ha.
"""


"""
9. (se avanza tempo) Costruite la lista `cresciuti`, con i nomi degli atenei i cui iscritti
ai corsi di laurea sono aumentati in OGNI anno rispetto all'anno precedente.
"""

