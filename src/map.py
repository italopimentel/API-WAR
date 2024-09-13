class Map():

    def __init__(self):
        self.__territories = []
        self.__regions = []
    

    def replace_territories (self, territories):
        self.__territories = territories
        
    def add_territory(self, territory):
        self.__territories.append(territory)

    def get_territories(self):
        return self.__territories

    def attack_territory(self, current_player, territory_name, number_of_army):
        pass

    def defend_territory(self, current_player, territory, number_of_army):
        pass