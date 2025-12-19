# app/servicios.py

from difflib import get_close_matches
from app.conocimiento import BaseConocimiento


class ServicioSugerencia:
    def __init__(self, base_conocimiento: BaseConocimiento):
        self.base_conocimiento = base_conocimiento

    def generar_sugerencia(self, consulta: str) -> str:
        preguntas = self.base_conocimiento.obtener_preguntas()

        coincidencias = get_close_matches(consulta, preguntas, n=1, cutoff=0.6)
        if not coincidencias:
            return "No se encontro una repsuesta adecuada para la pregunta."

        pregunta_encontrada = coincidencias[0]
        respuesta = self.base_conocimiento.obtener_respuestas(pregunta_encontrada)

        return respuesta
