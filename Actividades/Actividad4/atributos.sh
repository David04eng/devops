#!/bin/bash

# Verificar si se pasó un argumento
if [ -z "$1" ]; then
    echo "Uso: $0 <directorio>"
    exit 1
fi

# Nombre del archivo de salida
salida="atributos_archivo.txt"

# Vaciar el archivo de salida antes de escribir
> "$salida"

# Recorrer todos los archivos dentro del directorio dado
for archivo in "$1"/*; do
    if [ -f "$archivo" ]; then
        permisos=$(ls -l "$archivo" | awk '{print $1}')
        usuario=$(ls -l "$archivo" | awk '{print $3}')
        grupo=$(ls -l "$archivo" | awk '{print $4}')
        tamanio=$(ls -l "$archivo" | awk '{print $5}')
        fecha_modificacion=$(ls -l "$archivo" | awk '{print $6, $7, $8}')

        # Escribir la información en el archivo de salida
        echo "Archivo: $archivo" >> "$salida"
        echo "Permisos: $permisos" >> "$salida"
        echo "Usuario: $usuario" >> "$salida"
        echo "Grupo: $grupo" >> "$salida"
        echo "Tamaño: $tamanio bytes" >> "$salida"
        echo "Última modificación: $fecha_modificacion" >> "$salida"
        echo "--------------------------------------" >> "$salida"
    fi
done

# Mensaje de éxito
echo "Información guardada en $salida"

