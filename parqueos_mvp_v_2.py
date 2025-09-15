"""
Sistema de Parqueos

Opcional: editar PARQUEOS_CSV para cambiar el archivo de datos.
"""
from typing import List
import os

# Archivo de persistencia (CSV: nombre,capacidad,ocupados)
PARQUEOS_CSV = "parqueos.csv"

# ---------------------- LÓGICA DE DATOS ----------------------

def estado_inicial() -> List[List]:
    """Retorna estado por defecto como lista de listas: [nombre, capacidad, ocupados]."""
    return [
        ["Parqueo A", 5, 2],
        ["Parqueo B", 3, 3],
        ["El Hoyo", 4, 1],
        ["Puerta B", 6, 4],
    ]


def cargar_estado(ruta: str) -> List[List]:
    """Lee el CSV si existe; si no, retorna estado_inicial()."""
    if not os.path.exists(ruta):
        return estado_inicial()
    datos: List[List] = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                continue
            nombre = partes[0]
            try:
                capacidad = int(partes[1])
                ocupados = int(partes[2])
            except ValueError:
                continue
            datos.append([nombre, capacidad, ocupados])
    if len(datos) == 0:
        return estado_inicial()
    return datos


def guardar_estado(ruta: str, lotes: List[List]) -> None:
    """Escribe el CSV con el formato nombre,capacidad,ocupados (una línea por lote)."""
    lineas: List[str] = []
    for lote in lotes:
        nombre, capacidad, ocupados = lote[0], int(lote[1]), int(lote[2])
        lineas.append(f"{nombre},{capacidad},{ocupados}\n")  
    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(lineas)


def espacios_libres(lote: List) -> int:
    """Calcula espacios libres para un lote."""
    return max(int(lote[1]) - int(lote[2]), 0)


def puede_reservar(lote: List) -> bool:
    return espacios_libres(lote) > 0


def reservar(lotes: List[List], indice: int) -> bool:
    """Intenta reservar en el lote indicado; True si se incrementó 'ocupados'."""
    if indice < 0 or indice >= len(lotes):
        return False
    lote = lotes[indice]
    if puede_reservar(lote):
        lote[2] = int(lote[2]) + 1
        return True
    return False


def cancelar(lotes: List[List], indice: int) -> bool:
    """Intenta cancelar una reserva; True si se decrementó 'ocupados'."""
    if indice < 0 or indice >= len(lotes):
        return False
    lote = lotes[indice]
    if int(lote[2]) > 0:
        lote[2] = int(lote[2]) - 1
        return True
    return False


def resetear_estado() -> List[List]:
    """Devuelve una copia nueva del estado inicial."""
    base = estado_inicial()
    nuevo: List[List] = []
    for fila in base:
        nuevo.append([fila[0], int(fila[1]), int(fila[2])])
    return nuevo

# ---------------------- PRESENTACIÓN ----------------------

def construir_filas_tabla(lotes: List[List]) -> List[List[str]]:
    """Crea filas de texto para mostrar una tabla en consola, sin imprimirla."""
    filas: List[List[str]] = []
    for i, lote in enumerate(lotes, start=1):
        nombre = str(lote[0])
        capacidad = str(lote[1])
        ocupados = str(lote[2])
        libres = str(espacios_libres(lote))
        filas.append([str(i), nombre, capacidad, ocupados, libres])
    return filas


def formatear_tabla(filas: List[List[str]]) -> str:
    """Devuelve una cadena con la tabla monoespaciada (no imprime)."""
    encabezados = ["#", "Parqueo", "Cap", "Ocup", "Libres"]
    anchos = [len(x) for x in encabezados]
    for fila in filas:
        for c, celda in enumerate(fila):
            if len(celda) > anchos[c]:
                anchos[c] = len(celda)
    sep = " ".join(["-" * a for a in anchos])
    linea_enc = " ".join([encabezados[i].ljust(anchos[i]) for i in range(len(encabezados))])
    cuerpo = []
    for fila in filas:
        cuerpo.append(" ".join([fila[i].ljust(anchos[i]) for i in range(len(fila))]))
    return "\n" + linea_enc + "\n" + sep + "\n" + "\n".join(cuerpo) + "\n"


# ---------------------- PROGRAMA PRINCIPAL ----------------------

# Mensaje de bienvenida / introducción
print("\n⋙════ ⋆★⋆ ════ ⋘ SISTEMA DE PARQUEOS UVG ⋙ ════ ⋆★⋆ ════ ⋘")
print("Este sistema permite: ver disponibilidad, reservar y cancelar un espacio.")
print("Cómo usar:")
print("  1) Revise la tabla de disponibilidad.")
print("  2) Elija una opción del menú (1-5).")
print("  3) Siga las indicaciones en pantalla.\n")

lotes_estado = cargar_estado(PARQUEOS_CSV)
opcion_seleccionada = "0"

while opcion_seleccionada != "5":
    # Sección de disponibilidad con espaciado claro
    print("\n≻───── ⋆✩⋆ ─────≺ DISPONIBILIDAD ACTUAL ≻───── ⋆✩⋆ ─────≺\n")
    filas_tabla = construir_filas_tabla(lotes_estado)
    print(formatear_tabla(filas_tabla))

    # Menú principal con separación
    print("\n≻───── ⋆✩⋆ ─────≺ MENÚ PRINCIPAL ≻───── ⋆✩⋆ ─────≺\n")
    print("1) Ver disponibilidad")
    print("2) Reservar un espacio")
    print("3) Cancelar una reserva")
    print("4) Reiniciar sistema (estado por defecto)")
    print("5) Salir\n")
    opcion_seleccionada = input("Seleccione una opción: ").strip()

    if opcion_seleccionada == "1":
        # Solo vuelve a mostrar la tabla en la siguiente iteración
        print("\nℹ️  Información actualizada mostrada arriba.\n")
    elif opcion_seleccionada == "2":
        indice_texto = input("\nIngrese el número del parqueo para reservar: ").strip()
        if indice_texto.isdigit():
            indice_int = int(indice_texto) - 1
            if reservar(lotes_estado, indice_int):
                guardar_estado(PARQUEOS_CSV, lotes_estado)
                print("\n✅ Reserva confirmada.\n")
            else:
                print("\n❌ No se pudo reservar (sin cupo o índice inválido).\n")
        else:
            print("\n⚠️ Entrada inválida (debe ser un número de la tabla).\n")
    elif opcion_seleccionada == "3":
        indice_texto = input("\nIngrese el número del parqueo para cancelar: ").strip()
        if indice_texto.isdigit():
            indice_int = int(indice_texto) - 1
            if cancelar(lotes_estado, indice_int):
                guardar_estado(PARQUEOS_CSV, lotes_estado)
                print("\n↩️  Reserva cancelada correctamente.\n")
            else:
                print("\n⚠️ No hay reservas para cancelar o índice inválido.\n")
        else:
            print("\n⚠️ Entrada inválida (debe ser un número de la tabla).\n")
    elif opcion_seleccionada == "4":
        lotes_estado = resetear_estado()
        guardar_estado(PARQUEOS_CSV, lotes_estado)
        print("\n🔄 El sistema se ha reiniciado a su estado original.\n")
    elif opcion_seleccionada == "5":
        print("\nSaliendo... ¡Gracias por usar el sistema!\n")
    else:
        print("\n⚠️ Opción inválida. Intente nuevamente.\n")

