# app/modelos.py

from pydantic import BaseModel, Field


class SolicitudSugerencia(BaseModel):
    query: str = Field(
        ...,
        min_length=1,
        description="Consulta Realizada por el Usuario",
        examples=["¿Cómo cambio mi contraseña?"],
    )


class RespuestaSugerencia(BaseModel):
    suggestion: str = Field(
        ...,
        description="Sugerencia Generada a partir de la base de conocimiento",
        examples=[
            "Puedes cambiar tu contraseña en la sección de configuración de tu perfil."
        ],
    )


class EntradaConocimiento(BaseModel):
    pregunta: str = Field(
        ...,
        min_length=1,
        description="Pregunta a agregar a la base de conocimiento",
        examples=["¿Cómo contacto soporte?"],
    )
    respuesta: str = Field(
        ...,
        min_length=1,
        description="Respuesta asociada a la pregunta",
        examples=["Puedes escribir a soporte@cari.com"],
    )
