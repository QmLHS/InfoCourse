#!/usr/bin/env bash
# esplora.sh - il primo sguardo a un file di dati, dalla shell.
#
#   ./esplora.sh <file> [separatore]
#
# Esempi:
#   ./esplora.sh data/2009-2013_iscritti.csv ';'
#   bash ~/InfoCourse/01_AmbienteDiLavoro/esplora.sh ../dati/meteo.csv
#
# Il separatore, se non lo dici, e' la virgola.
#
# Fa tre cose, le stesse che faresti a mano: dice quanto e' grande il file,
# numera le colonne dell'intestazione, e mostra le prime righe di dati. Non
# apre il file per intero: su un file da un milione di righe ci mette lo
# stesso tempo che su uno da dieci.

file="$1"
sep="${2:-,}"

# Senza argomento non si va da nessuna parte: si dice come si usa e si esce.
if [ -z "$file" ]; then
    echo "uso: $0 <file> [separatore]" >&2
    exit 1
fi

# Il file potrebbe non esserci, o essere un percorso sbagliato: e' l'errore
# piu' comune, e conviene dirlo chiaramente invece di far fallire i comandi.
if [ ! -f "$file" ]; then
    echo "esplora.sh: non trovo '$file'" >&2
    echo "  sei in: $(pwd)" >&2
    exit 1
fi

echo "File       : $(cd "$(dirname "$file")" && pwd)/$(basename "$file")"
echo "Dimensione : $(du -h "$file" | cut -f1)"
echo "Righe      : $(wc -l < "$file")"
echo ""

echo "Colonne dell'intestazione:"
head -n 1 "$file" | tr "$sep" '\n' | cat -n
echo ""

echo "Prime 3 righe di dati:"
tail -n +2 "$file" | head -n 3
