# Cari IA - Sistema de Sugerencias Automaticas

##Resumen

**Cari IA** es una API REST desarrollada con **FastApi** que permite a asesores de atencion al cliente recibir **sugerencias automaticas** basadas en una base de preguntas frecuentes mientras responden consultas de usuarios.

El sistema recibe una consulta en lenguaje natural y devuelve una sugerencia relevante, utilizando una logica de similitud de texto simple.
La solucion esta diseñada como una **prueba tecnica funcional**, priorizando claridad, correcta arquitectura y cumplimiento estrcito de los requerimientos establecidos.

---

## Contexto del Problema

En los flujos de atencion al cliente, los asesores suelen responder repetidamente a un conjunto reducido de preguntas frecuentes.
Esto genera:

- Repeticion innecesaria de respuestas.
- Posibles inconsistencias en la informacion entregada.
- Aumento del tiempo de atencion por consulta

El objetivo de esta rpueba tecnica es construir un sistema ligero que asita al asesor sugiriendo respuestas relevantes en tiempo real, sin introducir complejidad innecesaria ni dependencias externas, y demostrando buenas practicas de desarrollo backend con Python.

## Alcance de la Solucion

### Funcionalidades Incluidas

- API REST desarrollada con **FastApi**
- Endpoint `POST /suggest` para generar sugerencias a partir de una consulta del usuario
- Endpoint `GET /history` para consultar el historial de preguntas y respuestas generadas
- Base de conocimiento predefinida almacenada en memoria(diccionario o archivo JSON)
- Logica basica de similitud de texto para encontrar la pregunta mas cercana
- Persistencia temporal del historial de consultas en memoria
- Validaciones simples de entrada usando **Pydantic**
- Pruebas unitarias basicas para cada endpoint

## Funcionalidades excluidas

- Persistencia en base de datos
- Autenticacion y autorizacion
- Procesamiento avanzado de lenguaje natural
- Infraestructura productiva (caching, colas, observabilidad)

Estas exclusiones son **decisiones conscientes**, alineadas con el alcance de la prueba tecnica, que busca evaluar el diseño, claridad y correcto funcionamiento de una API REST sin sobre-ingenieria.

---

##Arquietectura General

La aplicacion sigue una arquitectura modular y simple, alineada con el alcance de la prueba tecnica y orientada a facilitar la lectura, el mantenimiento y las pruebas.

La estrcutura del proyecto se organiza de la siguiente manera:

app/
├── main.py # Punto de entrada de la aplicación y definición de endpoints
├── modelos.py # Modelos de datos y validaciones (Pydantic)
├── conocimiento.py # Base de conocimiento predefinida
├── servicios.py # Lógica de negocio (sugerencias y similitud)
├── almacenamiento.py # Persistencia temporal del historial en memoria
tests/
├── test_sugerencias.py # Pruebas del endpoint /suggest
├── test_historial.py # Pruebas del endpoint /history
requirements.txt
README.md

### Principios Aplicados

- **Separaciond eresponsabilidades**: Cada modulo cumple una funcion clara y acotada.
- **Bajo Acoplamiento**: Los endpoints delegan la logica de negocio a servicios independientes.
- **Simplicidad Intencional**: Se evita complejidad innecesaria que no aporta valor al problema y alcance planteado.

Esta organizacion permite extender o modificar funcionalidades sin afectar el resto del sistema, manteniendo el codigo legible y facil de testear.

---

## Decisiones Tecnicas

## Uso de FastApi

Se utiliza **FastApi** por ser un framework ligero, moderno y ampliamente adoptado en el ecosistema Python para el desarrollo de API REST.

Permite:

- Definir endpoints de forma clara y decalrativa
- Validar datos de entrada mediante **Pydantic**
- Generar documentacion automatica(OpenAPI)
- Facilitar la escritura de pruebas.

Esta eleccion cumple directamente con los requerimientos de la prueba tecnica.

---

### Base de Conocimiento en Memoria

La base de preguntas frecuentes se mantiene en memoria, ya sea como un diccionario o estructura cargada desde un archivo JSON.

Esta decision se toma porque:

- La prueba no requiere persistencia permanente.
- Reduce dependencias externas.
- Simplifica la ejecucion y el despliegue del proyecto.

---

### Logica de Similitud de Texto

Para la generacion de sugerencias se implementa una busqueda basica de similitud utilizando tecnicas simples como `difflib.get_close_matches`.

Este enfoque:

- Cumple con el requerimiento funcional.
- Es facil de entender y mantener.
- Evita sobre-ingenieria en un contexto de prueba tecnica.

En un entorno productivo, esta logica podria reemplazarse por tecnicas mas avanzadas de procesamiento de lenguaje natural.

---

### Persistencia de Historial

El historial de consultas y sugerencias se almacena en una estrcutura en memoria(por ejemplo, una lista de diccionarios).

Esta decision:

- Cumple con el requerimiento de persistencia temporal.
- Evita el uso de bases de datos innecesarias.
- Facilita las pruebas automatizadas.

---

### Validaciones de Entrada

Se utilizan modelos de **Pydantic** para validar las solicitudes entrantes, asegurando que:

- El campo `query` este presente.
- El valor no sea vacio.

Esto permite manejar errores de forma clara y consistente.

---

### Pruebas Automatizadas

Se incluyen pruebas unitarias basicas para cada endpoint utilizando `pytest`.

Las pruebas validan:

- Codigos de estado HTTP.
- Estrcutura del JSON de respuesta.
- Casos basicos de error.

El objetivo de las pruebas es garantizar el correcto funcionamiento del sistema y demostrar buenas practicas de desarrollo backend.

---

##Tecnologias Utilizadas  
FastApi, Pydantic, difflib, pytest

##Instalacion
Pasos Claros y Reproducibles

##Ejecucion de la Aplicacion
Comando exacto para levantar la Api

##Endpoints Disponibles

- POST /suggest
- GET /history
- POST /knowledge

##Pruebas
Como ejecutarlas y que validadn

##Decisiones Tecnicas relevantes
Aqui te luces

##Limitaciones Conocidas
Demuestras Madurez

##Posibles Mejoras
Vision de futuro sin prometer Humo
