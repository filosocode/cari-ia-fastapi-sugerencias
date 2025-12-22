# app/main.py

from fastapi import FastAPI, Body
from pydantic import BaseModel

from app.modelos import SolicitudSugerencia, RespuestaSugerencia, EntradaConocimiento
from app.conocimiento import BaseConocimiento
from app.servicios import ServicioSugerencias
from app.almacenamiento import AlmacenamientoHistorial


class EstadoAPI(BaseModel):
    mensaje: str


app = FastAPI(
    title="API de sugerencias - Cari IA",
    version="1.0.0",
    description=(
        "API REST que genera sugerencias automaticas a partir de una base de "
        "preguntas frecuentes.\n\n"
        "Proyecto desarrollado como prueba tecnica, "
        "priorizando claridad, simplicidad y buenas practicas."
    ),
)

# Instancias (estado en memoria)
base_conocimiento = BaseConocimiento()
almacenamiento = AlmacenamientoHistorial()
servicio_sugerencias = ServicioSugerencias(base_conocimiento)


@app.post(
    "/suggest",
    tags=["Sugerencias"],
    response_model=RespuestaSugerencia,
    summary="Generar sugerencia automatica",
    description=(
        "Recibe una consulta del usuario y devuelve una sugerencia basada en la pregunta "
        "mas similar de la base de conocimiento.\n\n"
        "La consulta y su resultado se almacenan en el historial."
    ),
)
def sugerir_respuesta(
    solicitud: SolicitudSugerencia = Body(
        example={"query": "¿Cómo cambio mi contraseña?"}
    ),
):
    sugerencia = servicio_sugerencias.generar_sugerencia(solicitud.query)
    almacenamiento.guardar(solicitud.query, sugerencia)
    return RespuestaSugerencia(suggestion=sugerencia)


@app.get(
    "/history",
    tags=["Historial"],
    summary="Obtener historial de consultas",
    description=("Devuelve el historial completo de consultas procesadas."),
)
def obtener_historial():
    return almacenamiento.obtener_historial()


@app.post(
    "/knowledge",
    tags=["Conocimiento"],
    summary="Agregar conocimiento",
    description=(
        "Agrega una nueva pregunta y respuesta a la base de conocimiento en memoria."
    ),
)
def agregar_conocimiento(
    entrada: EntradaConocimiento = Body(
        example={
            "pregunta": "¿Como contacto soporte?",
            "respuesta": "Puedes escribir a soporte@cari.com",
        }
    )
):
    base_conocimiento.agregar(entrada.pregunta, entrada.respuesta)
    return {"mensaje": "Conocimiento agregado correctamente"}


@app.get(
    "/",
    tags=["Sistema"],
    response_model=EstadoAPI,
    summary="Estado de la API",
    description=(
        "Endpoint de verificacion para comprobar que la API esta funcionando."
    ),
)
def raiz():
    return {"mensaje": "API de Sugerencias en funcionamiento"}
