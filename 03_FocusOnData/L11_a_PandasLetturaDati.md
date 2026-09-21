# L11_a — Leggere i dati con pandas

> **Materiale pre-lezione.** Da leggere prima di venire in aula. Questa lezione non
> ha videolezione: il materiale scritto è l'unico che precede l'incontro.
>
> **File parziale.** Contiene per ora la sola sezione *Guardare cosa si è caricato*,
> scritta per colmare un buco documentato in `riepilogo_funzioni_python.md` §13:
> `.info()` compare in **15 temi d'esame** e non era insegnata da nessuna parte.
> Il resto della lezione va ancora riportato qui dai notebook del 2023.

Tutti gli esempi girano sul file `data/MeteoMilano2011.csv`: le rilevazioni
meteorologiche giornaliere di Milano per il 2011, una riga per giorno.

```python
import pandas as pd

meteo = pd.read_csv("data/MeteoMilano2011.csv")
```

---

## Guardare cosa si è caricato

Caricare un file non è capirlo. Prima di qualunque analisi servono tre domande:
**quante righe e colonne ci sono, di che tipo è ogni colonna, e dove mancano i
dati.** `info()` risponde a tutte e tre insieme.

### `info()` — la carta d'identità del DataFrame

```python
meteo.info()
```

```
<class 'pandas.DataFrame'>
RangeIndex: 365 entries, 0 to 364
Data columns (total 23 columns):
 #   Column                                 Non-Null Count  Dtype
---  ------                                 --------------  -----
 0   CET                                    365 non-null    str
 1   Temperatura maxC                       363 non-null    float64
 2   Temperatura mediaC                     363 non-null    float64
 3   Temperatura minC                       363 non-null    float64
...
 18   Max Velocità RafficaKm/h              24 non-null     float64
 19  Precipitazionimm                       365 non-null    float64
 20   CloudCover                            281 non-null    float64
 21   Eventi                                177 non-null    str
 22  WindDirDegrees<br />                   365 non-null    str
dtypes: float64(15), int64(5), str(3)
memory usage: 73.7 KB
```

Si leggono quattro cose:

| Riga dell'output | Cosa dice |
|:---|:---|
| `RangeIndex: 365 entries` | quante righe: 365, una per giorno del 2011 |
| `Data columns (total 23 columns)` | quante colonne |
| `Non-Null Count` | **quanti valori presenti** in ogni colonna |
| `Dtype` | il tipo con cui pandas ha interpretato la colonna |

**La colonna che conta è `Non-Null Count`.** Le righe sono 365: ogni colonna che
dice meno di `365 non-null` ha valori mancanti, e quanti si legge per differenza.
Qui `Max Velocità Raffica` ne ha 24 su 365 — cioè ne mancano 341, il 93%: una
colonna praticamente vuota, che è bene sapere subito e non a metà analisi.

> **`info()` contro `describe()`.** Sono due domande diverse.
> `info()` dice **com'è fatta** la tabella — tipi, presenze, memoria — e riguarda
> tutte le colonne. `describe()` dice **cosa contiene**, con media, deviazione
> standard e quartili, e riguarda solo le colonne numeriche.
> Si guarda `info()` per primo.

> **Nota sulle versioni.** Dalla versione 3 di pandas le colonne di testo appaiono
> come `str`; nelle versioni precedenti comparivano come `object`. È la stessa cosa.

### Il tipo dice se il caricamento è riuscito

`Dtype` è la verifica più rapida che il file sia stato letto come si voleva. Una
colonna di numeri che compare come `str` significa che pandas ha trovato qualcosa
che numero non è: un separatore decimale sbagliato, uno spazio, un `n.d.` in mezzo
ai valori.

Qui `float64` e `int64` sulle colonne di misura dicono che la lettura è andata
bene. `WindDirDegrees<br />` è `str` — e il nome spiega perché: il file conserva
un frammento di HTML a fine riga.

### Contare i valori mancanti

`info()` li fa vedere ma li fa contare a mente. Per il numero esatto:

```python
mancanti = meteo.isnull().sum()
print(mancanti[mancanti > 0])
```

```
Temperatura maxC               2
Temperatura mediaC             2
Temperatura minC               2
 Max VisibilitàKm             41
 Mean VisibilitàKm            41
 Min VisibilitàkM             41
 Max Velocità RafficaKm/h    341
 CloudCover                   84
 Eventi                      188
dtype: int64
```

`isnull()` costruisce una tabella di `True`/`False`, e `sum()` conta i `True`
colonna per colonna — perché in Python `True` vale 1. La selezione
`mancanti[mancanti > 0]` tiene solo le colonne che un problema ce l'hanno.

Le tre temperature ne perdono 2 su 365: due giorni senza rilevazione, trascurabile.
`Eventi` ne perde 188, ma lì il vuoto **è un dato**: significa che quel giorno non
c'è stato nessun fenomeno da segnalare.

> Un valore mancante non è sempre un errore. Prima di eliminarlo, chiedersi cosa
> significhi che manca.

### Attenzione ai nomi delle colonne

Guardando l'output di `info()` si nota che alcuni nomi cominciano con uno spazio:
`' Eventi'`, `' CloudCover'`, `' Max VisibilitàKm'`. Non è un difetto della stampa,
è com'è scritta l'intestazione del file.

Conseguenza pratica:

```python
meteo["Eventi"]      # KeyError: 'Eventi'
meteo[" Eventi"]     # funziona
```

Per vedere i nomi esatti, virgolette comprese:

```python
for c in meteo.columns:
    print(repr(c))
```

`repr()` mostra la stringa come è scritta nel codice, quindi gli spazi si vedono.
È il modo di risolvere un `KeyError` che sembra impossibile.

---

## Da completare

Il resto di `L11_a` — i parametri di `read_csv()`, i separatori, gli encoding, il
riconoscimento del formato — va riportato qui dai notebook
`Lezione11aProgPythonPandasIntroLetturaDati` in `LezioniLucidi/Pandas/`.
