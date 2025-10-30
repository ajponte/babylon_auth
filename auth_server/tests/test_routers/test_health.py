"""Health router tests"""

HEALTH_URI = "/health/"


def test_health_ok(httpClient):
    resp = httpClient.get(HEALTH_URI)
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}
