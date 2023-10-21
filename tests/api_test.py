from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_read_ram_stats():
    response = client.get("/ram_stats/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_read_ram_stats_with_custom_n():
    response = client.get("/ram_stats/?n=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 5


def test_read_ram_stats_invalid_n():
    response = client.get("/ram_stats/?n=0")
    assert response.status_code == 400


def test_read_ram_stats_non_integer_n():
    response = client.get("/ram_stats/?n=abc")
    assert response.status_code == 422
