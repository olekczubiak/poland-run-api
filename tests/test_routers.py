import pytest

from starlette.testclient import TestClient

from app.routers import V1

client = TestClient(V1)

def test_root():
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.parametrize("dist", ['42km000m', '5km000m', '21km000m'])
def test_distance(dist):
    response = client.get(f'/distance/{dist}')
    assert response.status_code == 200


###cdn