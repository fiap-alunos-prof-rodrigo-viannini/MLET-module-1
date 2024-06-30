from fastapi.testclient import TestClient
from main import app

# Cria um cliente de teste para interagir com a aplicação FastAPI definida em main.app
client = TestClient(app)

# Teste para verificar se a rota "/links/" retorna status 200 e contém a chave "links" no JSON de resposta
def test_get_website_links():
    response = client.get("/links/")
    assert response.status_code == 200
    assert "links" in response.json()

# Teste para verificar se a rota "/links2/" com um link específico retorna status 200 e contém a chave "links" no JSON de resposta
def test_get_website_links2():
    link = "http://iseb3.com.br/respostas-participantes-processo-20222023"
    response = client.get(f"/links2/?link={link}")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
    assert response.status_code == 200
    assert "links" in response.json()

# Teste para verificar se a rota "/download/" com um link específico retorna status 200 e contém as chaves "message" e "file_path" no JSON de resposta
def test_download_file():
    link = "https://iseb3-site.s3.amazonaws.com/Respostas_2022_-_todas_as_participantes_-_todas_as_dimens%C3%B5es.xlsx"
    response = client.get(f"/download/?link={link}")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "file_path" in response.json()
