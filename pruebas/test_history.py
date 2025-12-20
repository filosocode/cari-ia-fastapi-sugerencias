from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_obtener_historial():
    respuesta = client.get("/history")

    assert respuesta.status_code == 200
    assert isinstance(respuesta.json(), list)
