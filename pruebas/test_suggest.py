from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sugget_respuesta_exitosa():
    respuesta = client.post("/suggest", json={"query": "¿Cómo cambio mi contraseña?"})

    assert respuesta.status_code == 200
    data = respuesta.json()

    assert "suggestion" in data
    assert isinstance(data["suggestion"], str)


def test_suggest_query_vacia():
    respuesta = client.post("/suggest", json={"query": ""})

    assert respuesta.status_code == 422
