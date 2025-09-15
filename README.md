# Proyecto Fase 2 – Prototipo de Parqueos UVG

## 📌 Descripción
Este proyecto corresponde a la **Fase 2 – Prototipado** d
El prototipo es un sistema en consola que permite a los usuarios **visualizar la disponibilidad de parqueos cercanos a la universidad y reservar un espacio**.

El código está diseñado con **estructuras básicas de Python** (listas, funciones, variables descriptivas)

## 🎯 Objetivo
Resolver el problema identificado en la **Fase 1**:  
> La falta de información clara y en tiempo real sobre la disponibilidad de parqueos cercanos al campus universitario.  

Este prototipo simula disponibilidad en distintos parqueos y permite reservar un espacio, reduciendo la incertidumbre y mejorando la experiencia de los usuarios.

## ⚙️ Funcionalidades principales
1. **Visualizar disponibilidad** de parqueos (capacidad total y espacios libres).  
2. **Reservar un espacio** en el parqueo elegido.  
3. **Cancelar una reserva** para liberar espacio.  
4. **Actualizar la información** en cada acción.  
5. **Interfaz de consola sencilla e intuitiva** con menús numerados.  

## 🛠️ Tecnologías utilizadas
- Python 3.x  
- Estructuras básicas: listas, funciones, condicionales y bucles.  

## 🚀 Instrucciones de uso
### 1. Clonar el repositorio
```bash
git clone https://github.com/usuario/prototipo-parqueos.git
cd prototipo-parqueos
python parqueos_mvp_v2.py
```
## Interacción

Seleccione la opción 1 para ver la disponibilidad de parqueos.

Seleccione la opción 2 para reservar un espacio (elija el número del parqueo).

Seleccione la opción 3 para cancelar una reserva.

Seleccione la opción 4 para resetear el estado inicial.

Seleccione la opción 5 para salir del sistema.

## Estructura del proyecto
``` bash
prototipo-parqueos/
│── parqueos_mvp_v3.py        # Código principal del prototipo
│── parqueos.csv              # Datos de parqueos (capacidad y ocupados)
│── README.md                 # Documentación del proyecto
│── CONTRIBUTING.md           # Guía de contribución y buenas prácticas
│── .gitignore                # Archivos a ignorar por Git
```
## ⚠️ Limitaciones del prototipo

Este MVP no es perfecto y presenta limitaciones conocidas:

No maneja múltiples usuarios ni horarios.

Persistencia simple en un archivo CSV (sin base de datos).

La interfaz es solo en consola (sin interfaz gráfica ni aplicación web).

No tiene autenticación ni control de concurrencia.

*Estas limitaciones se reconocen para dejar claro que el prototipo es una versión inicial, y sirven como oportunidades de mejora para fases posteriores.*

## 📈 Roadmap (mejoras futuras)

Fase 3: Manejo de horarios y tiempo límite de reserva.

Fase 4: Reportes de uso y estadísticas de ocupación.

Fase 5: Interfaz web o aplicación móvil conectada a base de datos.

Fase 6: Autenticación de usuarios y roles diferenciados.

## 👥 Creadores
Grupo 7
- Victor Flores
- Diego Melgar
- Diego Ramirez
- Daniela Roldán


