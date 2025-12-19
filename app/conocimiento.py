# app/conocimiento.py


class BaseConocimiento:
    def __init__(self):
        self._conocimiento = [
            {
                "pregunta": "¿como cambio mi contraseña?",
                "respuesta": "Puedes cambiar tu contraseña en la seccion de configuracion de tu perfil ",
            },
            {
                "pregunta": "¿Cual es el Horario de Atencion?",
                "respuesta": "Nuestro horario es de lunes a viernes de 8 am a 5 pm. ",
            },
            {
                "pregunta": "¿Cómo contacto soporte?",
                "respuesta": "Puedes escribir a soporte@cari.com.",
            },
        ]

    def obtener_preguntas(self):
        return [item["pregunta"] for item in self._conocimiento]

    def obtener_respuestas(self, pregunta):
        for item in self._conocimiento:
            if item["pregunta"] == pregunta:
                return item["respuesta"]
        return None

    def agregar(self, pregunta, respuesta):
        self._conocimiento.append({"pregunta": pregunta, "repsuesta": respuesta})
