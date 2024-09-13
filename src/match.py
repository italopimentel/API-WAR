from map import Map
from objective import Objective
from territory import Territory
from player import Player
import io
import random

class Match():
    
    def __init__(self, match_name, match_id):
        self.__match_name = match_name
        self.__match_id = match_id
        self.__match_started = False
        self.__all_colors_checked = False
        self.__colors = ['verde', 'azul', 'amarelo', 'preto', 'branco', 'vermelho']
        self.tempo_de_espera = 0
        self.__vez_de_jogar = Player("null")
        self.__map = Map()
        self.__objectives = []
        self.__players = []
        self.__load_data()
    
    def get_id(self):
        return self.__match_id
    
    def get_name(self):
        return self.__match_name
    
    def __load_data(self):
        with io.open("data/objectives.txt", mode='r', encoding='utf-8') as objective_file:
           for objective in objective_file:
               normalized_string = objective.replace('\n', '')
               self.__objectives.append(Objective(text=normalized_string))
        
        with io.open("data/territories.txt", mode='r', encoding='utf-8') as territory_file:
           for territory in territory_file:
               normalized_territory= territory.replace('\n', '')
               payload_territories = normalized_territory.split(",")
               self.__map.add_territory(Territory(name=payload_territories[0], region=payload_territories[1]))
    
    def join_match(self, player):
        self.__players.append(player)
        random_objective_pos = random.randint(0, len(self.__objectives) - 1)
        player.set_objective(self.__objectives[random_objective_pos])

        if (self.get_number_of_players() >= 2 and self.__match_started == False):
            self.__match_started = True
            self.__vez_de_jogar = self.__players[0]

            player_id = 0
            territories = self.__map.get_territories()
            num_sorteados = []
            for iteration in range(0, len(territories)):
                random_territory_pos = random.randint(0, len(territories) - 1)
                while (random_territory_pos in num_sorteados):
                    random_territory_pos = random.randint(0, len(territories) - 1)

                num_sorteados.append(random_territory_pos)
                print(f"Numero sorteado: {random_territory_pos}")
                territories[random_territory_pos].set_dominant_player(self.__players[player_id])
                player_id += 1
                if (player_id >= len(self.__players)):
                    player_id = 0
                territories[random_territory_pos].add_army(1)
            

            self.__map.replace_territories(territories)


    def avaliable_colors(self):
        return self.__colors
    
    def remove_color (self, color):
        if color in self.__colors:
            self.__colors.remove(color)

    def __check_color_selection (self):
        self.__all_colors_checked = True
        for player in self.__players:
            if player.get_color() == None:
                self.__all_colors_checked = False
        
    def show_game_status(self):
        self.__check_color_selection()
        if (self.__match_started and self.__all_colors_checked):
            string_player_da_rodada = f'Vez de jogar: {self.__vez_de_jogar.get_name()}\n\n'
            string_territories= ''''''
            for territory in self.__map.get_territories():
                string_territories += "Região: " + territory.get_region() + '\t\t' 'Território: ' + territory.get_name() + '\t\t' + 'Tropas: ' + str(territory.get_army()) + '\t\t' + 'player_dominante: ' + territory.get_dominant_player_name() + '\n'
            return string_player_da_rodada + string_territories
        elif (self.__match_started and self.__all_colors_checked == False):
            return "Esperando os jogadores selecionarem as cores"
        else:
            return "Esperando jogadores para iniciar a partida..."

    def get_number_of_players (self):
        return len(self.__players)
    
    def check_if_player_exists(self, name):
        for player in self.__players:
            if player.get_name() == name:
                return 1
        return 0

    def get_player(self, name):
        for player in self.__players:
            if player.get_name() == name:
                return player

    






