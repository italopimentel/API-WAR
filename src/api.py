from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from match import Match
from player import Player

partidas = []
id = 0
string_de_apresentacao = '''Sejam bem vindo ao jogo WAR!

Salas disponíveis:

'''

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def inicio():
    global partidas
    partidas_disponiveis = ''''''
    for match in partidas:
        partidas_disponiveis += "id: " + str(match.get_id()) + " - " + match.get_name() + f" players: {match.get_number_of_players()}" + "\n"
    return string_de_apresentacao + partidas_disponiveis

@app.post("/criar-partida")
async def criar_partida(numero_de_jogadores_para_iniciar : int):
    global id, string_de_apresentacao, partidas
    nova_partida = Match(match_name=f"Partida {id}", match_id=id, number_of_players_to_start=numero_de_jogadores_para_iniciar)
    partidas.append(nova_partida)
    string_de_status = f"partida criada com sucesso! id da partida: {id}"
    id += 1
    return string_de_status

@app.post("/entrar-na-partida")
async def entrar_na_partida(nome_usuario:str , id_da_partida:int):
    global partidas
    usuario = Player(nome_usuario)
    for partida in partidas:
        if partida.get_id() == id_da_partida:
            partida.join_match(usuario)
            return f"Você entrou na partida {partida.get_id()}"
    return "Não foi possível entrar na partida"

@app.get("/{id_da_partida}/{nome_do_jogador}", response_class=PlainTextResponse)
async def tela_jogo(id_da_partida:int, nome_do_jogador:str):
    global partidas
    if (partidas[id_da_partida].check_if_player_exists(nome_do_jogador)):
        jogador = partidas[id_da_partida].get_player(nome_do_jogador)
        objetivo = jogador.get_objective()
        cor_do_exercito = jogador.get_color()
        mensagem_objetivo = f"Seu objetivo: {objetivo.get_objective()}\n"
        string_de_exibicao = f"cor do exército: {cor_do_exercito}\n" + mensagem_objetivo + partidas[id_da_partida].return_game_status()
        return string_de_exibicao
    else:
        return "Você não tem acesso a essa partida"

@app.post("/{id_da_partida}/{nome_do_jogador}/set-color")
async def selecionar_cor(id_da_partida:int, nome_do_jogador: str, cor:str):
    cor_disponiveis = partidas[id_da_partida].avaliable_colors()
    if (cor in cor_disponiveis):
        jogador = partidas[id_da_partida].get_player(nome_do_jogador)
        jogador.set_color(cor)
        partidas[id_da_partida].remove_color(cor)
        return f"A cor {cor} foi aplicada ao player {jogador.get_name()}"
    else:
        return 'Cor inválida ou em uso por outro player'

