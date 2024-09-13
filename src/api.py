from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from match import Match
from player import Player

matches = []
id = 0
presentation_string = '''Sejam bem vindo ao jogo WAR!

Salas disponíveis:

'''

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def inicio():
    global matches
    current_match = ''''''
    for match in matches:
        print(match.get_id())
        current_match += "id: " + str(match.get_id()) + " - " + match.get_name() + f" players: {match.get_number_of_players()}" + "\n"
    return presentation_string + current_match

@app.post("/criar-partida")
async def criar_partida():
    global id, presentation_string, matches
    new_match = Match(match_name=f"Pipoca do maior {id}", match_id=id)
    matches.append(new_match)
    id += 1
    return f"partida criada com sucesso! id da partida: {id}"

@app.post("/entrar-na-partida")
async def entrar_na_partida(nome_usuario:str , id_da_partida:int):
    global matches
    user = Player(nome_usuario)
    for match in matches:
        if match.get_id() == id_da_partida:
            match.join_match(user)
            return f"Você entrou na partida {match.get_id()}"
    
    return "Não foi possível entrar na partida"

@app.get("/{id}/{player_name}", response_class=PlainTextResponse)
def tela_jogo(id:int, player_name:str):
    global matches
    if (matches[id].check_if_player_exists(player_name)):
        player = matches[id].get_player(player_name)
        objetivo = player.get_objective()
        cor_do_exercito = player.get_color()
        mensagem_objetivo = f"Seu objetivo: {objetivo.get_objective()}\n"
        string_de_exibicao = f"cor do exército: {cor_do_exercito}\n" + mensagem_objetivo + matches[id].show_game_status()
        return string_de_exibicao
    else:
        return "Você não tem acesso a essa partida"

@app.post("/{id}/{player_name}/set-color")
def selecionar_cor(id:int, player_name: str, cor:str):
    cor_disponiveis = matches[id].avaliable_colors()
    if (cor in cor_disponiveis):
        player = matches[id].get_player(player_name)
        player.set_color(cor)
        matches[id].remove_color(cor)
        return f"A cor {cor} foi aplicada ao player {player.get_name()}"
    else:
        return 'Cor inválida ou em uso por outro player'

