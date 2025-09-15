# Prototipo de Sistema de Parqueos (MVP v3)

> **Estado:** Prototipo funcional de consola que refleja los **elementos esenciales** de la solución propuesta: ver disponibilidad, reservar, cancelar y persistir el estado en archivo CSV (sin diccionarios, siguiendo las restricciones de la rúbrica).

## 1) ¿Qué resuelve? (Vínculo con Fase 1)
El problema identificado en la Fase 1 es **gestionar de forma sencilla la ocupación de parqueos** (consultar disponibilidad y evitar dobles reservas), con una solución que **no dependa de internet** y corra en equipos modestos para pruebas iniciales.
Este MVP:
- Permite **ver disponibilidad** de cada parqueo.
- **Reserva** respetando la capacidad (sin sobrevender espacios).
- **Cancela** reservas para liberar cupos.
- **Persiste** el estado en `parqueos.csv` para no perder datos entre ejecuciones.
- Mantiene **interacción simple** por consola, priorizando rapidez de prueba y cero fricción.

> En la Fase 2/3, esta base puede migrar a una interfaz web o móvil y añadir usuarios/roles, reportes y analítica.

## 2) Cómo correrlo (Instalación y uso)
Requisitos: Python 3.8+
```bash
# 1) Clonar o descargar este repo
# 2) Ubicarse en la carpeta del proyecto
# 3) Ejecutar:
python parqueos_mvp_v3.py
```
Menú principal:
```
1) Ver disponibilidad
2) Reservar un espacio
3) Cancelar una reserva
4) Resetear estado (valores por defecto)
5) Salir
```
> El archivo `parqueos.csv` **se genera/actualiza automáticamente**. Su formato es:
```
Parqueo A,5,2
Parqueo B,3,3
El Hoyo,4,1
Puerta B,6,4
```

## 3) Estructura del proyecto
```
.
├─ parqueos_mvp_v3.py        # Script principal (consola). E/S solo aquí
├─ parqueos.csv              # Persistencia (CSV sin encabezados)
├─ README.md                 # Este documento
├─ CONTRIBUTING.md           # Guía de contribución y buenas prácticas
└─ .gitignore                # Archivos/ carpetas a ignorar por Git
```

## 4) Diseño y buenas prácticas
- **Claridad del código**: nombres descriptivos, funciones pequeñas y responsabilidades únicas.
- **Sin `input/print` dentro de funciones**: la lógica es pura y testeable; la E/S está solo en el bloque principal.
- **Sin `while True`**, **sin `global`**, **sin diccionarios**: se emplean **listas** y **CSV** por la rúbrica.
- **Documentado** con docstrings concisos; comentarios mínimos y no redundantes.
- **Persistencia** con CSV para reproducibilidad y simplicidad.

### Principales funciones
- `cargar_estado(ruta)`: lee CSV o retorna estado inicial por defecto.
- `guardar_estado(ruta, lotes)`: escribe CSV.
- `espacios_libres(lote)`: capacidad – ocupados.
- `puede_reservar(lote)`: `espacios_libres > 0`.
- `reservar(lotes, indice)`: incrementa ocupados si hay cupo.
- `cancelar(lotes, indice)`: decrementa ocupados si hay reservas.
- `construir_filas_tabla(lotes)` y `formatear_tabla(filas)`: preparan salida tabular **sin imprimir**.

## 5) Demostración rápida (para README)
> Inserta aquí un GIF de ~10s mostrando: ver → reservar → ver → cancelar → ver.
Sugerencia para grabar: OBS Studio, ScreenToGif o QuickTime.

## 6) Rúbrica y cumplimiento
- **(20 pts) Prototipo funcional**: refleja los elementos esenciales (ver, reservar, cancelar, persistir). Código claro, funcional y documentado.
- **(15 pts) Resuelve el problema de Fase 1**: el MVP ataca directamente la necesidad de **conocer y gestionar cupos** sin sobre-reservas, de manera simple y offline.
- **(15 pts) Repo y buenas prácticas**: proyecto versionado, estructura mínima clara, README completo, documentación en funciones y guía de contribución.

## 7) Roadmap (siguientes pasos)
- Usuarios/roles y registro de acciones (auditoría).
- Reporte diario/semana de ocupación (CSV → gráficos).
- API/Interfaz web (Flask/Streamlit) y base de datos.
- Control de concurrencia y bloqueo temporal de plazas.
- Tests unitarios básicos (pytest) para lógica de negocio.

## 8) Licencia
MIT (o la que el curso indique).
