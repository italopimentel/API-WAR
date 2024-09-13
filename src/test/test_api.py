import requests


def test_disponibilidade_servidor():
    conexao = requests.get(f'http://127.0.0.1:8000/')
    assert conexao.status_code == 200

def test_criacao_partida():
    numero_de_jogadores = 2
    resultado = requests.post(f'http://127.0.0.1:8000/criar-partida?numero_de_jogadores_para_iniciar={numero_de_jogadores}')
    assert resultado.status_code == 200

def test_entrar_na_partida():
    jogadores = ['italo', 'paulo']
    id_partida = 0
    for jogador in jogadores:
        resultado = requests.post(f'http://127.0.0.1:8000/entrar-na-partida?nome_usuario={jogador}&id_da_partida={id_partida}')
        assert resultado.text == '"Você entrou na partida 0"'

def test_selecionar_cor():
    jogadores = ['italo', 'paulo']
    cores = {
        'italo' : 'preto',
        'paulo' : 'vermelho'
    }
    id_partida = 0
    for jogador in jogadores:
        resultado = requests.post(f'http://127.0.0.1:8000/0/{jogador}/set-color?cor={cores[jogador]}')
        assert resultado.text == f'"A cor {cores[jogador]} foi aplicada ao player {jogador}"'

def test_se_partida_foi_iniciada():
    resultado = requests.get('http://127.0.0.1:8000/0/italo')
    assert len(resultado.text) > 500
