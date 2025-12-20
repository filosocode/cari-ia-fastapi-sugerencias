# app/modelos.py

from pydantic import BaseModel, Field


class SolicitudSugerencia(BaseModel):
    query: str = Field(
        ..., min_length=1, description="Consulta Realizada por el Usuario"
    )


class RespuestaSugerencia(BaseModel):
    suggestion: str = Field(
        ..., description="Sugerencia Generada a partir de la base de conocimiento"
    )


class EntradaConocimiento(BaseModel):
    pregunta: str = Field(
        ..., min_length=1, description="Pregunta a agregar a la base de conocimiento"
    )
    respuesta: str = Field(
        ..., min_length=1, description="Respuesta asociada a la pregunta"
    )
