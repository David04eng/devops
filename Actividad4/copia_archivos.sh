#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Uso: $0 <nombre_del_archivo_destino>"
    exit 1
fi

archivo_origen="eventos.txt"
archivo_destino=$1

if [ ! -f "$archivo_origen" ]; then
    echo "Error: El archivo $archivo_origen no existe."
    exit 1
fi

cp "$archivo_origen" "$archivo_destino"

echo "Se ha copiado el contenido de $archivo_origen a $archivo_destino"
