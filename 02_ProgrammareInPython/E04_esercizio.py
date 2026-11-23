# -*- coding: utf-8 -*-
# il commento sopra serve per le lettere accentate,
# per favore non modificate queste prime righe

# E04 - Caricare file di forma diversa, con le funzioni.
# Copiate questo file fuori dal repository del corso prima di modificarlo.
# Alla fine `python3 E04_esercizio.py`, da un terminale appena aperto, non deve dare errori.

import pathlib as pl

nomeEsercizio = "caricamentoFile"

pDati = pl.Path.home() / "InfoCourse" / "02_ProgrammareInPython" / "data"
fPrenotazioni = pDati / "prenotazioni.txt"
fTurbine = pDati / "turbine.csv"
fConsumazioni = pDati / "consumazioni.csv"
fOrchidee = pDati / "ls_orchid.fasta"
fIscritti = pl.Path.home() / "InfoCourse" / "01_AmbienteDiLavoro" / "data" / "2009-2013_iscritti.csv"

# La struttura di E03, la stessa: serve per controllare la funzione 13.
dIscrittiE03 = {
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

L'esercizio riguarda il caricamento di cinque file di forma diversa. Sono tutti nella cartella `data` del repository del corso, e i loro percorsi sono gia' nelle variabili qui sopra, costruiti con `pathlib`.

**`prenotazioni.txt`** contiene le prenotazioni delle visite di uno studio medico, nell'ordine in cui sono state raccolte. La prima riga e' l'intestazione:

    Giorno settimana,data(annommgg),ora,dottore,cliente,importo

Ogni riga successiva contiene, separati da `,`: il giorno della settimana, la data nel formato `AAAAMMGG`, l'ora in cui comincia la visita (un intero), il cognome del dottore, il cognome del paziente, l'importo in euro. Ogni visita dura un'ora. Lo studio ha **una sola stanza** per le visite.

**`turbine.csv`** contiene le rilevazioni fatte su alcune turbine per il pompaggio dell'acqua. La prima riga e' l'intestazione. Ogni riga successiva contiene, separati da `;`: l'identificativo della turbina (un intero), `S` o `N` a seconda che la turbina si sia rotta alla fine delle rilevazioni, e poi, per ogni ora di funzionamento, tre valori interi: la portata (`flow`), i giri al minuto (`rpm`) e le vibrazioni in hertz (`hz`). Le ore di funzionamento cambiano da turbina a turbina, quindi le righe hanno lunghezze diverse:

    ID_Machine;Rottura(S/N);flow_1;rpm_1;hz_1;flow_2;rpm_2;hz_2;...
    0;S;110;1980;37620;60;1080;9720;210;3570;32130;...

**`consumazioni.csv`** contiene le consumazioni ai distributori di due campus universitari. Le prime righe cominciano con `%` e descrivono il file: una riga di spiegazione, una riga con il solo `%`, e poi un nome di campo per riga, nell'ordine delle colonne. Segue una riga vuota, e poi una consumazione per riga, con i campi separati da `;`:

    6;2;acqua;4;0.5;Bicocca;U1;

**`ls_orchid.fasta`** contiene 94 sequenze di DNA di orchidee nel formato FASTA. Ogni sequenza comincia con una riga di intestazione, che comincia con `>`, e prosegue su una o piu' righe di basi. Fra una sequenza e l'altra c'e' una riga vuota. L'intestazione ha la forma

    >gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA

dove i campi separati da `|` sono: `gi`, il numero gi, `emb`, l'accession (`Z78533.1`), e il locus seguito da una descrizione libera, in cui la seconda parola e' la specie (`C.irapeanum`). Le basi sono le lettere `A`, `C`, `G`, `T`; la lettera `N` indica una base non determinata.

**`2009-2013_iscritti.csv`** e' il file di `E01` e `E02`: gli iscritti agli atenei italiani dal 2008-2009 al 2012-2013, separatore `;`, codifica UTF-8. Il campo `CODICE_ISCRIZIONE` vale `T1` per le righe dei totali, e `T1a`, `T1b`, `T1c` per le righe «di cui». I nomi che contengono virgolette sono scritti fra virgolette, con le virgolette interne raddoppiate, come si fa nei CSV.

Implementate le seguenti funzioni: il commento che precede ogni funzione vi spieghera' in dettaglio che cosa fare.
Controllate nel corpo principale del programma (in fondo allo script) come vengono invocate le funzioni che implementerete.
Se volete, potete implementare delle funzioni aggiuntive rispetto a quelle gia' presenti qua sotto.
Le funzioni che caricano un file devono funzionare con qualunque file della stessa forma: non scrivete a mano ne' il nome del file ne' i valori che potete ricavare dal file.
"""


##########################################################
# INIZIO DELLA PARTE DA EDITARE
##########################################################

cognome = "Sostituiscimi con il cognome"  # inserisci qua il tuo cognome
nome = "Sostituiscimi con il nome"  # inserisci qua il tuo nome


# ---------- Una funzione per tutti i file ----------

"""
1. La funzione `righeDati(fName_IN, sCommento_IN=None, bIntestazione_IN=True)` accetta in input il nome di un file, una stringa o `None`, e un booleano, e restituisce una lista di stringhe.
La lista di stringhe restituita contiene le righe di dati del file, ciascuna senza il carattere di a capo e senza gli spazi in fondo, nell'ordine del file.
La funzione deve scartare:
    * le righe vuote;
    * le righe che cominciano con `sCommento_IN`, se `sCommento_IN` non e' `None`;
    * l'intestazione, cioe' la prima riga che non e' vuota e non e' un commento, se `bIntestazione_IN` e' `True`.
Ad esempio un file con le righe `"a;b\\n"`, `"\\n"`, `"1;2\\n"`, `"3;4\\n"` da' `["1;2", "3;4"]`, e con `bIntestazione_IN=False` da' `["a;b", "1;2", "3;4"]`.
"""
def righeDati(fName_IN, sCommento_IN=None, bIntestazione_IN=True):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# ---------- Prenotazioni ----------

"""
2. La funzione `leggiPrenotazioni(fName_IN)` accetta il nome del file delle prenotazioni e restituisce una lista di tuple.
Ogni tupla corrisponde a una prenotazione, nell'ordine del file, e ha la forma `(giorno, data, ora, dottore, cliente, importo)`, dove `ora` e' un intero, `importo` un float e gli altri campi sono stringhe.
Ad esempio la riga `dom,20150816,12,Brambilla,Rinaldi,56.00` diventa `('dom', '20150816', 12, 'Brambilla', 'Rinaldi', 56.0)`.
Usate la funzione 1.
"""
def leggiPrenotazioni(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
3. La funzione `numeroSovrapposizioni(lPrenotazioni_IN, bPerDottore_IN=False)` accetta la lista restituita dalla funzione 2 e un booleano, e restituisce un intero.
Una prenotazione e' sovrapposta quando la stanza e' gia' stata prenotata da una prenotazione precedente, nella stessa data e alla stessa ora: la prima ha diritto alla stanza, le successive sono sovrapposte. La funzione restituisce il numero di prenotazioni sovrapposte.
Se `bPerDottore_IN` e' `True`, si contano invece le prenotazioni sovrapposte per lo stesso dottore: stessa data, stessa ora e stesso dottore.
Ad esempio con tre prenotazioni il 20150816 alle 12, due per Brambilla e una per Verdi, la funzione restituisce 2, e 1 con `bPerDottore_IN=True`.
"""
def numeroSovrapposizioni(lPrenotazioni_IN, bPerDottore_IN=False):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# ---------- Turbine ----------

"""
4. La funzione `terne(lValori_IN)` accetta una lista di stringhe che rappresentano numeri interi e restituisce una tupla di tre liste di interi, oppure `None`.
Gli elementi della lista vanno letti a tre a tre: il primo di ogni terna va nella prima lista, il secondo nella seconda, il terzo nella terza.
Se il numero di elementi non e' un multiplo di 3, la funzione restituisce `None`.
Ad esempio `terne(['1', '2', '3', '4', '5', '6'])` restituisce `([1, 4], [2, 5], [3, 6])`, e `terne(['1', '2'])` restituisce `None`.
"""
def terne(lValori_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
5. La funzione `leggiRilevazioni(fName_IN)` accetta il nome del file delle turbine e restituisce un dizionario.
Il dizionario ha una coppia per ogni turbina:
    * la chiave e' l'identificativo della turbina, il primo campo della riga, convertito in intero;
    * il valore e' una tupla di quattro elementi `(rottura, lFlow, lRpm, lHz)`.
Gli elementi della tupla sono:
    * `rottura`: il secondo campo della riga, la stringa `'S'` o `'N'`, lasciata com'e';
    * `lFlow`: la lista delle portate, una per ora, cioe' il primo valore di ogni terna;
    * `lRpm`: la lista dei giri al minuto, cioe' il secondo valore di ogni terna;
    * `lHz`: la lista delle vibrazioni, cioe' il terzo valore di ogni terna.
Le tre liste contengono interi, hanno tutte la lunghezza pari al numero di ore di funzionamento della turbina, e seguono l'ordine delle ore: l'elemento di posizione 0 e' la prima ora.
L'intestazione non entra nel dizionario. Nemmeno le righe in cui i valori dopo i primi due campi non sono in numero multiplo di 3 entrano nel dizionario: per ciascuna la funzione stampa `riga scartata, turbina` seguito dall'identificativo.
Ad esempio una riga come `2;N;140;2380;28560;150;2550;30600`, di due ore, diventerebbe la coppia `2: ('N', [140, 150], [2380, 2550], [28560, 30600])`.
Usate le funzioni 1 e 4.
"""
def leggiRilevazioni(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
6. La funzione `vibrazioneMassima(dRilevazioni_IN, iTurbina_IN)` accetta il dizionario restituito dalla funzione 5 e l'identificativo di una turbina, un intero, e restituisce una tupla di due interi, oppure `None`.
La tupla e' `(ora, hz)`: la vibrazione massima della turbina e l'ora in cui e' stata rilevata, contando le ore da 1. Se la massima compare in piu' ore, vale la prima.
Se la turbina non e' nel dizionario, la funzione restituisce `None`.
Ad esempio per una turbina con vibrazioni `[28560, 30600, 29000]` la funzione restituisce `(2, 30600)`.
"""
def vibrazioneMassima(dRilevazioni_IN, iTurbina_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# ---------- Consumazioni ----------

"""
7. La funzione `nomiCampi(fName_IN)` accetta il nome del file delle consumazioni e restituisce una lista di stringhe.
La lista contiene i nomi dei campi scritti nelle righe che cominciano con `%`, nell'ordine del file, senza il `%` e senza gli spazi intorno. La riga di spiegazione e la riga con il solo `%` non sono nomi di campi.
Ad esempio le righe `"% Segue un elenco dei campi."`, `"%"`, `"% ora"`, `"% Campus"` danno `['ora', 'Campus']`.
"""
def nomiCampi(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
8. La funzione `leggiConsumazioni(fName_IN)` accetta il nome del file delle consumazioni e restituisce una lista di dizionari.
Ogni dizionario corrisponde a una consumazione, nell'ordine del file. Le chiavi sono i sette nomi di campo restituiti dalla funzione 7, uguali per tutti i dizionari, e i valori sono i campi della riga. Tutti i valori sono di tipo `str`, senza conversioni: alcuni rappresentano numeri, e li convertira' la funzione 9 quando servono.
    * `'ora'`: un intero da 0 a 23, l'ora della consumazione;
    * `'giorno settimana'`: un intero da 1 a 6, il giorno della settimana;
    * `'tipo Consumazione'`: che cosa e' stato consumato, ad esempio `'caffe'`;
    * `'quantita'`: un intero, quante unita';
    * `'prezzo unitario'`: un numero decimale scritto con il punto, ad esempio `'0.5'`, il prezzo di una unita';
    * `'Campus'`: il campus del distributore, `'Bicocca'` o `'PoliMi'`;
    * `'Edificio'`: l'edificio del distributore, ad esempio `'U1'`.
Il `;` in fondo a ogni riga non produce una chiave.
Ad esempio la riga `6;2;acqua;4;0.5;Bicocca;U1;` diventa
    `{'ora': '6', 'giorno settimana': '2', 'tipo Consumazione': 'acqua', 'quantita': '4', 'prezzo unitario': '0.5', 'Campus': 'Bicocca', 'Edificio': 'U1'}`.
Usate le funzioni 1 e 7.
"""
def leggiConsumazioni(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
9. La funzione `spesaMedia(lConsumazioni_IN, sChiave_IN="Edificio")` accetta la lista restituita dalla funzione 8 e il nome di un campo, e restituisce un dizionario.
Il dizionario associa a ogni valore del campo `sChiave_IN` la spesa media delle consumazioni con quel valore, dove la spesa di una consumazione e' la quantita' per il prezzo unitario.
Il campo su cui raggruppare si sceglie con `sChiave_IN`, che se non viene passato vale `"Edificio"`:
    * `spesaMedia(lConsumazioni)` raggruppa per edificio, e le chiavi del dizionario sono gli edifici, ad esempio `'U1'`;
    * `spesaMedia(lConsumazioni, "Campus")` raggruppa per campus, e le chiavi sono `'Bicocca'` e `'PoliMi'`.
Ad esempio, con tre consumazioni nell'edificio `'U1'` di spesa 2.0, 1.0 e 3.0 e una nell'edificio `'U2'` di spesa 5.0, `spesaMedia` restituisce `{'U1': 2.0, 'U2': 5.0}`.
"""
def spesaMedia(lConsumazioni_IN, sChiave_IN="Edificio"):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# ---------- FASTA ----------

"""
10. La funzione `leggiFasta(fName_IN)` accetta il nome di un file FASTA e restituisce un dizionario.
Il dizionario associa all'accession di ogni sequenza la tupla `(specie, sequenza)`, dove `sequenza` e' la stringa di tutte le basi della sequenza, le righe unite senza a capo.
Ad esempio la sequenza che comincia con `>gi|2765658|emb|Z78533.1|CIZ78533 C.irapeanum 5.8S rRNA gene and ITS1 and ITS2 DNA` diventa la coppia `'Z78533.1': ('C.irapeanum', 'CGTAACAAGGTTTCCGTAGG...')`.
Usate la funzione 1.
"""
def leggiFasta(fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
11. La funzione `percentualeGC(sSequenza_IN)` accetta una sequenza di basi e restituisce un float, oppure `None`.
La percentuale GC e' la percentuale di basi `G` o `C` fra le basi determinate, cioe' fra le `A`, `C`, `G`, `T` della sequenza: le `N` non contano.
Se la sequenza non contiene basi determinate, la funzione restituisce `None`.
Ad esempio `percentualeGC("GGCAT")` restituisce `60.0`, `percentualeGC("GGCATNNNNN")` restituisce `60.0`, e `percentualeGC("NNN")` e `percentualeGC("")` restituiscono `None`.
"""
def percentualeGC(sSequenza_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


"""
12. La funzione `salvaGC(dSequenze_IN, fName_IN)` accetta il dizionario restituito dalla funzione 10 e il nome di un file, e restituisce un intero.
La funzione scrive un nuovo file, diverso da quello letto: se il file esiste gia', lo riscrive da capo. Nel file scrive l'intestazione `accession;specie;GC` e poi una riga per sequenza, con l'accession, la specie e la percentuale GC con due decimali, separate da `;`. Restituisce il numero di sequenze scritte.
Ad esempio la prima riga dopo l'intestazione e' `Z78533.1;C.irapeanum;59.59`.
Usate la funzione 11.
"""
def salvaGC(dSequenze_IN, fName_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


# ---------- Iscritti, se avanza tempo ----------

"""
13. La funzione `caricaIscritti(fName_IN, lCodici_IN)` accetta il nome del file degli iscritti e una lista di codici di ateneo, stringhe, e restituisce un dizionario di dizionari.
Il dizionario ha la stessa forma di `strutturaDati` di `E03`, che trovate qui in testa come `dIscrittiE03`. Ha tre livelli.
Il dizionario esterno ha una coppia per ogni ateneo della lista:
    * la chiave e' il codice dell'ateneo, il campo `COD_ATENEO`, una stringa come `'01501'`;
    * il valore e' il dizionario dell'ateneo.
Il dizionario dell'ateneo ha sempre le stesse tre chiavi:
    * `'nome'`: il campo `NOME_ATENEO`, una stringa, senza le virgolette del CSV;
    * `'laurea'`: il dizionario degli iscritti ai corsi di laurea, anno per anno;
    * `'dottorato'`: il dizionario degli iscritti al dottorato, anno per anno.
I dizionari `'laurea'` e `'dottorato'` hanno una coppia per ogni anno accademico:
    * la chiave e' il campo `ANNO_ACCADEMICO`, una stringa come `'2008-2009'`;
    * il valore e' il campo `ISCRITTI_LAUREA`, o `ISCRITTI_DOTTORATO`, convertito in intero.
Si usano solo le righe dei totali, quelle con `CODICE_ISCRIZIONE` uguale a `T1`. Ogni riga di un ateneo della lista aggiunge un anno ai suoi dizionari `'laurea'` e `'dottorato'`; il dizionario dell'ateneo si crea alla prima riga che lo riguarda.
Ad esempio, in forma ridotta a un ateneo e a un anno:
    `{'01501': {'nome': 'Milano - Università degli studi', 'laurea': {'2008-2009': 58093}, 'dottorato': {'2008-2009': 1548}}}`.
Chiamata con i codici di `dIscrittiE03`, deve restituire un dizionario uguale a `dIscrittiE03`.
Usate la funzione 1.
"""
def caricaIscritti(fName_IN, lCodici_IN):
    pass     # Implementa il codice della funzione qua sotto. Questa riga puo' essere cancellata.


##########################################################
# Fine del compito e della parte da editare obbligatoriamente.
# Inizio del corpo principale del programma. Potete
# modificare o lasciare invariato il codice qua sotto
# (a vostra scelta), se lo modificate, accertatevi
# che il codice non dia errori in esecuzione.
##########################################################


def mostra(oggetto_IN, iQuanti_IN=2):
    """Stampa il tipo dell'oggetto e, per liste, tuple e dizionari, la lunghezza e i primi elementi."""
    if oggetto_IN is None:
        print("None: la funzione non restituisce ancora niente")
    elif type(oggetto_IN) == dict:
        print(type(oggetto_IN), len(oggetto_IN), list(oggetto_IN.items())[:iQuanti_IN])
    elif type(oggetto_IN) == list or type(oggetto_IN) == tuple:
        print(type(oggetto_IN), len(oggetto_IN), oggetto_IN[:iQuanti_IN])
    else:
        print(type(oggetto_IN), oggetto_IN)


print(f"Esercizio {nomeEsercizio}.")
print(f"nome: {nome}\ncognome: {cognome}.")

print("\nEs. 1)\n")
mostra(righeDati(fPrenotazioni))
mostra(righeDati(fTurbine), 1)
mostra(righeDati(fConsumazioni, "%", False))
mostra(righeDati(fOrchidee, None, False))

print("\nEs. 2)\n")
lPrenotazioni = leggiPrenotazioni(fPrenotazioni)
mostra(lPrenotazioni)

print("\nEs. 3)\n")
print(numeroSovrapposizioni(lPrenotazioni))
print(numeroSovrapposizioni(lPrenotazioni, True))

print("\nEs. 4)\n")
print(terne(['1', '2', '3', '4', '5', '6']))
print(terne(['1', '2']))

print("\nEs. 5)\n")
dRilevazioni = leggiRilevazioni(fTurbine)
mostra(dRilevazioni, 1)

print("\nEs. 6)\n")
print(vibrazioneMassima(dRilevazioni, 7))
print(vibrazioneMassima(dRilevazioni, 250))
print(vibrazioneMassima(dRilevazioni, "7"))

print("\nEs. 7)\n")
print(nomiCampi(fConsumazioni))

print("\nEs. 8)\n")
lConsumazioni = leggiConsumazioni(fConsumazioni)
mostra(lConsumazioni, 1)

print("\nEs. 9)\n")
mostra(spesaMedia(lConsumazioni), 8)
mostra(spesaMedia(lConsumazioni, "Campus"))

print("\nEs. 10)\n")
dOrchidee = leggiFasta(fOrchidee)
mostra(dOrchidee, 1)

print("\nEs. 11)\n")
print(percentualeGC("GGCAT"))
print(percentualeGC("GGCATNNNNN"))
print(percentualeGC("NNN"))

print("\nEs. 12)\n")
fGC = pl.Path(__file__).parent / "gcOrchidee.csv"
print(salvaGC(dOrchidee, fGC))

print("\nEs. 13)\n")
dIscritti = caricaIscritti(fIscritti, list(dIscrittiE03))
mostra(dIscritti, 1)
print(dIscritti == dIscrittiE03)
