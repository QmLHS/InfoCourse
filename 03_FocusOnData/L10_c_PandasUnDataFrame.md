# L10_c — Lavorare su un DataFrame

> **Materiale pre-lezione.** Da leggere prima di venire in aula. Questa lezione non
> ha videolezione: il materiale scritto è l'unico che precede l'incontro.
>
> **File parziale.** Contiene per ora le quattro operazioni che risultavano
> mancanti dal materiale didattico pur essendo chieste all'esame — vedi
> `riepilogo_funzioni_python.md` §13. Il resto della lezione va ancora riportato
> qui dai notebook del 2023.

Tutti gli esempi girano su `data/MeteoMilano2011.csv`, il meteo giornaliero di
Milano nel 2011 — 365 righe, una per giorno.

```python
import pandas as pd

meteo = pd.read_csv("data/MeteoMilano2011.csv")
```

> Alcune colonne del file hanno uno **spazio iniziale** nel nome: si scrive
> `meteo[" Eventi"]`, non `meteo["Eventi"]`. Vedi `L10_a`.

---

## 1. Ordinare — `sort_values()`

Ordina le righe secondo i valori di una colonna. Restituisce un DataFrame nuovo:
l'originale resta com'era.

```python
caldi = meteo.sort_values("Temperatura maxC", ascending=False)
print(caldi[["CET", "Temperatura maxC"]].head(5))
```

```
           CET  Temperatura maxC
234  2011-8-23              36.0
233  2011-8-22              35.0
231  2011-8-20              35.0
232  2011-8-21              34.0
235  2011-8-24              34.0
```

| Argomento | Effetto |
|:---|:---|
| `ascending=True` | crescente — è il default |
| `ascending=False` | decrescente |

**`sort_values()` + `head()` è il modo di rispondere a "i primi N".** I cinque
giorni più caldi del 2011 stanno tutti nella stessa settimana di agosto: si vede
perché l'ordinamento li porta in cima.

Si nota anche una cosa importante: **l'indice resta attaccato alla riga.** La riga
`234` è la stessa di prima, ha solo cambiato posizione. L'indice non viene
rinumerato, e serve `reset_index()` se lo si vuole.

### Ordinare su più colonne

Si passa una lista. Il secondo criterio decide fra le righe pari sul primo:

```python
print(meteo.sort_values(["Temperatura maxC", "Precipitazionimm"],
                        ascending=[False, True])
           [["CET", "Temperatura maxC", "Precipitazionimm"]].head(3))
```

```
           CET  Temperatura maxC  Precipitazionimm
234  2011-8-23              36.0               0.0
231  2011-8-20              35.0               0.0
233  2011-8-22              35.0               0.0
```

I due giorni a 35 gradi sono ordinati fra loro per precipitazione crescente.
`ascending` prende una lista lunga quanto le colonne: qui temperatura decrescente,
pioggia crescente.

---

## 2. Selezionare per appartenenza — `isin()`

L'indicizzazione booleana con `==` confronta con **un** valore. Per confrontare con
un insieme di valori servirebbe una catena di `|`:

```python
# funziona, ma non si scala
nevosi = meteo[(meteo[" Eventi"] == "Neve") |
               (meteo[" Eventi"] == "Pioggia-Neve") |
               (meteo[" Eventi"] == "Nebbia-Pioggia-Neve")]
```

`isin()` fa la stessa cosa con una lista:

```python
nevosi = meteo[meteo[" Eventi"].isin(["Neve", "Pioggia-Neve", "Nebbia-Pioggia-Neve"])]
print(nevosi[["CET", " Eventi", "Temperatura minC"]])
```

```
          CET               Eventi  Temperatura minC
26  2011-1-27         Pioggia-Neve              -2.0
28  2011-1-29                 Neve               0.0
29  2011-1-30  Nebbia-Pioggia-Neve               0.0
61   2011-3-3         Pioggia-Neve               1.0
```

Nel 2011 a Milano ha nevicato in quattro giorni, tre a fine gennaio e uno a marzo.

`isin()` restituisce una **maschera booleana** — un `True`/`False` per riga — che si
usa dentro le quadre esattamente come una condizione qualsiasi.

### Negare con `~`

Per prendere le righe che **non** appartengono all'insieme si antepone `~`:

```python
sereni = meteo[~meteo[" Eventi"].isin(["Pioggia", "Pioggia-Temporale", "Temporale"])]
print("giorni senza pioggia né temporale:", len(sereni))
```

```
giorni senza pioggia né temporale: 287
```

> In pandas la negazione di una maschera è `~`, non `not`. Come per le condizioni
> composte si usano `&` e `|` e non `and`/`or`: gli operatori Python lavorano su un
> valore singolo, questi lavorano elemento per elemento.

---

## 3. Eliminare righe e colonne — `drop()`

`drop()` restituisce una copia senza le righe o le colonne indicate. Anche qui
l'originale non viene toccato.

### Eliminare colonne

```python
meteoPulito = meteo.drop(columns=["WindDirDegrees<br />", " Max Velocità RafficaKm/h"])
print("prima:", meteo.shape, " dopo:", meteoPulito.shape)
```

```
prima: (365, 23)  dopo: (365, 21)
```

Due colonne tolte: quella con il frammento HTML nel nome, e quella con 341 valori
mancanti su 365 vista in `L10_a`. Le righe restano 365.

### Eliminare righe

Si indicano per **etichetta dell'indice**, non per posizione:

```python
print(meteo.drop(index=[0, 1, 2]).head(2)[["CET", "Temperatura maxC"]])
```

```
        CET  Temperatura maxC
3  2011-1-4               2.0
4  2011-1-5               2.0
```

I primi tre giorni dell'anno non ci sono più, e la tabella comincia dal 4 gennaio
che conserva la sua etichetta `3`.

> **`drop(columns=...)` contro `del`.** `del meteo["colonna"]` modifica il DataFrame
> **sul posto** e non restituisce niente; `drop()` lascia stare l'originale e
> restituisce una copia. Con `drop()` bisogna ricordarsi di assegnare il risultato,
> altrimenti il lavoro si perde:
> ```python
> meteo.drop(columns=["CloudCover"])            # calcolato e buttato via
> meteo = meteo.drop(columns=[" CloudCover"])   # corretto
> ```

---

## 4. Quanto variano i dati — `std()`

La media dice dove stanno i valori, la **deviazione standard** dice quanto sono
sparsi attorno alla media. Valore piccolo: valori addensati. Valore grande: valori
molto diversi fra loro.

```python
for c in ["Temperatura maxC", "Temperatura mediaC", "Temperatura minC"]:
    print(f"{c:22s} media {meteo[c].mean():5.1f}   std {meteo[c].std():5.2f}")
```

```
Temperatura maxC       media  18.9   std  8.62
Temperatura mediaC     media  13.0   std  8.07
Temperatura minC       media   7.7   std  8.06
```

Le tre medie sono molto diverse — 18.9, 13.0, 7.7 gradi — ma le tre deviazioni
standard sono quasi uguali, attorno a 8. Ha senso: a Milano la differenza fra estate
e inverno è la stessa qualunque momento della giornata si guardi, sono le
temperature a spostarsi tutte insieme verso l'alto o il basso.

Come le altre funzioni statistiche, `std()` **ignora i valori mancanti**: le due
temperature assenti non contano e non fanno diventare `NaN` il risultato.

### `std()` compare anche in `describe()`

```python
print(meteo[["Temperatura maxC", "Temperatura minC"]].describe())
```

```
       Temperatura maxC  Temperatura minC
count        363.000000        363.000000
mean          18.876033          7.663912
std            8.623081          8.060715
min            1.000000         -8.000000
25%           11.000000          0.000000
50%           20.000000          8.000000
75%           27.000000         14.500000
max           36.000000         22.000000
```

`describe()` calcola `count`, `mean`, `std`, `min`, i tre quartili e `max` in una
volta sola. Quando serve il singolo numero — per confrontarlo, per metterlo in una
condizione — si chiama il metodo corrispondente: `.std()`, `.mean()`, `.max()`.
La riga `std` di `describe()` e il risultato di `.std()` sono lo stesso valore.

| Metodo | Cosa dà |
|:---|:---|
| `.mean()` | media |
| `.std()` | deviazione standard |
| `.var()` | varianza — il quadrato della deviazione standard |
| `.median()` | mediana, il valore centrale |

---

## Da completare

Il resto di `L10_c` — selezione con `loc`/`iloc`, creazione di colonne, gestione dei
mancanti, raggruppamenti — va riportato qui dal notebook
`Lezione11cProgPythonPandasIntroLavorareSuUnDataFrame` in `LezioniLucidi/Pandas/`.
