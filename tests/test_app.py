from http import HTTPStatus

from fastapi.testclient import TestClient

from project_fastapi_python.app import app

client = TestClient(app)


def test_read_root_deve_retormar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange (organizacao)

    response = client.get('/')  # Act (acao)

    assert response.status_code == HTTPStatus.OK  # assert (garanta)
    assert response.json() == {'message': 'Olá mundo'}
