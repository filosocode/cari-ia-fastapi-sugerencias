# app/main.py

from fastapi import FastAPI
from app.modelos import SolicitudSugerencia, RespuestaSugerencia, EntradaConocimiento

from app.conocimiento import BaseConocimiento
from app.servicios import ServicioSugerencias
from app.almacenamiento import AlmacenamientoHistorial

app = FastAPI(title="API de sugerencias - Cari IA")

# Instancias (estado en memoria)
base_conocimiento = BaseConocimiento()
almacenamiento = AlmacenamientoHistorial()
servicio_sugerencias = ServicioSugerencias(base_conocimiento)


@app.post("/suggest", response_model=RespuestaSugerencia)
def sugerir_respuesta(solicitud: SolicitudSugerencia):
    sugerencia = servicio_sugerencias.generar_sugerencia(solicitud.query)

    almacenamiento.guardar(solicitud.query, sugerencia)
    return RespuestaSugerencia(suggestion=sugerencia)


@app.get("/history")
def obtener_historial():
    return almacenamiento.obtener_historial()


@app.post("/knowledge")
def agregar_conocimiento(entrada: EntradaConocimiento):
    base_conocimiento.agregar(entrada.pregunta, entrada.respuesta)

    return {"mensaje": "Conocimiento agregado correctamente"}


@app.get("/")
def raiz():
    return {"mensaje": "API de Sugerencias en funcionamiento"}
