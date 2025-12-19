# app/almacenamiento.py


class AlmacenamientoHistorial:
    def __init__(self):
        self._historial = []

    def guardar(self, consulta: str, sugerencias: str) -> None:
        self._historial.append({"query": consulta, "suggestion": sugerencias})

    def obtener_historial(self):
        return self._historial.copy()
