#!/usr/bin/env python
"""Gli esempi del deck d'aula di L02, eseguiti dal vivo.

Ogni blocco corrisponde a una slide di
`L02_a_InformazioneECalcolatore_aula.tex`, e i numeri che stampa sono quelli
stampati sui lucidi: se qualcosa non torna, ha ragione lo script e va corretta
la slide (la versione di pandas sulla VM non e' quella del portatile — vedi il
blocco 5, che e' l'esempio migliore della lezione proprio per questo).

    python esempi_aula.py            # tutti i blocchi
    python esempi_aula.py 2 3        # solo alcuni

I dati: `data/2009-2013_iscritti.csv` (iscritti per ateneo, MIUR) sta qui
accanto; `MeteoMilano2011.csv` vive in `03_FocusOnData/data/` perche' e' il file
della lezione su pandas, ed e' voluto che sia lo stesso.
"""
import sys
import pathlib as pl

import numpy as np
import pandas as pd

QUI = pl.Path(__file__).resolve().parent
METEO = QUI.parent / "03_FocusOnData" / "data" / "MeteoMilano2011.csv"
ISCRITTI = QUI / "data" / "2009-2013_iscritti.csv"
COL_PRESSIONE = " Mean Pressione a livello del marehPa"


def titolo(n, t):
    print(f"\n{'─' * 72}\n  {n}. {t}\n{'─' * 72}")


def blocco1_guardare_il_file():
    titolo(1, "read_csv non protesta, e una colonna diventa testo")
    df = pd.read_csv(METEO)
    print(f"righe x colonne      : {df.shape}")
    print(f"nome ultima colonna  : {df.columns[-1]!r}")
    print(f"primi valori         : {df.iloc[:3, -1].tolist()}")
    print("La direzione del vento e' testo, non gradi: nessun errore l'ha detto.")

    print()
    try:
        senza = pd.read_csv(ISCRITTI)
        print(f"iscritti.csv senza sep=';' : {senza.shape[1]} colonna")
    except pd.errors.ParserError as e:
        print("iscritti.csv senza sep=';' : ParserError —", str(e).split(". ")[-1].strip())
        print("  (una virgola dentro il nome di un ateneo, e il file si spacca a meta')")
    con = pd.read_csv(ISCRITTI, sep=";")
    print(f"iscritti.csv con  sep=';'  : {con.shape[1]} colonne, {len(con)} righe")


def blocco2_zero_davanti():
    titolo(2, "Lo zero davanti: 00101 diventa 101")
    a = pd.read_csv(ISCRITTI, sep=";", nrows=3)
    b = pd.read_csv(ISCRITTI, sep=";", nrows=3, dtype={"COD_ATENEO": str})
    print(f"default   : {a['COD_ATENEO'].tolist()}   dtype {a['COD_ATENEO'].dtype}")
    print(f"dtype=str : {b['COD_ATENEO'].tolist()}")
    print("Vale per CAP, codice fiscale, codici comune ISTAT.")


def blocco3_float():
    titolo(3, "La varianza, e perche' np.var fa due passate")
    print(f"0.1 + 0.2          = {0.1 + 0.2!r}   uguale a 0.3? {0.1 + 0.2 == 0.3}")
    print(f"somma di 0.1 x 10  = {sum([0.1] * 10)!r}   (qui gli errori si compensano)")

    p = pd.read_csv(METEO)[COL_PRESSIONE].dropna().to_numpy()
    print(f"\npressione a Milano, 2011: n = {p.size}, media = {p.mean():.4f} hPa")

    def ingenua(x):
        x = np.asarray(x)
        return (x * x).mean() - x.mean() ** 2

    def due_passate(x):
        x = np.asarray(x)
        return ((x - x.mean()) ** 2).mean()

    print(f"\n{'':16s} {'E[X^2]-E[X]^2':>18s} {'due passate':>18s}")
    for etichetta, scarto in (("", 0.0), (" + 1e8", 1e8)):
        for dt in (np.float64, np.float32):
            x = p.astype(dt) + dt(scarto)
            nome = f"{np.dtype(dt).name}{etichetta}"
            print(f"{nome:16s} {ingenua(x):18.6f} {due_passate(x):18.6f}")
    print("\nfloat32 + 1e8: la formula ingenua da' una varianza NEGATIVA.")


def blocco4_peso():
    titolo(4, "Quanto pesano i dati, e perche' si vettorizza")
    disco = METEO.stat().st_size / 1024
    df = pd.read_csv(METEO)
    print(f"meteo: {disco:.0f} KB su disco -> {df.memory_usage(deep=True).sum() / 1024:.0f} KB in memoria")

    n = 10_000_000
    print(f"\nuna colonna da {n:,} righe:")
    for dt in ("float64", "float32", "int16", "int8"):
        print(f"  {dt:8s} {np.zeros(n, dtype=dt).nbytes / 1024 ** 2:6.0f} MB")

    import time
    s = pd.Series(np.random.default_rng(0).integers(0, 100, 1_000_000))
    t0 = time.perf_counter()
    tot = 0
    for v in s:
        tot += v * 2
    t1 = time.perf_counter()
    (s * 2).sum()
    t2 = time.perf_counter()
    print(f"\nciclo Python su 1.000.000 righe : {t1 - t0:6.3f} s")
    print(f"vettorizzato (s*2).sum()        : {t2 - t1:6.3f} s  ->  {(t1 - t0) / (t2 - t1):.0f}x")


def blocco5_ambiente():
    titolo(5, "L'ambiente fa parte del risultato")
    print(f"pandas {pd.__version__} · numpy {np.__version__} · python {sys.version.split()[0]}")
    d = pd.read_csv(ISCRITTI, sep=";", nrows=3)
    print(f"COD_ATENEO qui e ora: dtype {d['COD_ATENEO'].dtype}")
    print("Lo stesso codice, su un'altra versione, puo' dare un tipo diverso:")
    print("e' il 'funziona sul mio computer' in due righe.")


def blocco6_encoding():
    titolo(6, "Da ASCII a UTF-8: a con l'accento sono due byte")
    riga = METEO.read_bytes().split(b"\n")[1]
    campo = riga.split(b",")[7]
    print(f"byte del campo        : {campo.hex(' ')}")
    print(f"letto come utf-8      : {campo.decode('utf-8')!r}")
    print(f"letto come latin-1    : {campo.decode('latin-1')!r}")

    fuori = QUI / "out"
    fuori.mkdir(exist_ok=True)
    crlf = fuori / "meteo_windows.csv"
    testo = METEO.read_text(encoding="utf-8").splitlines()[:5]
    crlf.write_bytes("\r\n".join(testo).encode("utf-8") + b"\r\n")
    print(f"\nscritto {crlf.relative_to(QUI)} con fine riga Windows: provalo con")
    print("  file out/meteo_windows.csv        # dira' 'with CRLF line terminators'")
    print("  tail -n +2 out/meteo_windows.csv | cut -d, -f23 | cat -A | head -2")
    print("Il \\r finisce DENTRO il valore: 'Nebbia' e 'Nebbia^M' diventano due categorie.")


BLOCCHI = [blocco1_guardare_il_file, blocco2_zero_davanti, blocco3_float,
           blocco4_peso, blocco5_ambiente, blocco6_encoding]


def main():
    scelti = [int(a) for a in sys.argv[1:]] or range(1, len(BLOCCHI) + 1)
    for n in scelti:
        BLOCCHI[n - 1]()
    print()


if __name__ == "__main__":
    main()
