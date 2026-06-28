import pytest
from api.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# 1. Teste de retorno HTTP 200 para a rota GET /produtos
def test_get_produtos_status_200(client):
    response = client.get('/produtos')
    assert response.status_code == 200


# 2. Teste de validação da estrutura do JSON retornado
def test_produtos_json_estrutura(client):
    response = client.get('/produtos')
    dados = response.get_json()
    assert isinstance(dados, list)
    if len(dados) > 0:
        primeiro_produto = dados[0]
        assert "id" in primeiro_produto
        assert "nome" in primeiro_produto
        assert "preco" in primeiro_produto


# 3. Teste de retorno HTTP 404 para um identificador inexistente
def test_get_produto_nao_encontrado_404(client):
    response = client.get('/produtos/999')
    assert response.status_code == 404


# 4. TESTE DE AUTORIA PRÓPRIA: Validar estoque não negativo
def test_validar_estoque_positivo(client):
    response = client.get('/produtos')
    dados = response.get_json()
    for produto in dados:
        assert produto['estoque'] >= 0
