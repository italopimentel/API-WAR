from player import Player

class Territory ():

    def __init__(self, name, region):
        self.__name = name
        self.__dominant_player = None
        self.__region = region
        self.__army = 0
    
    def set_dominant_player(self, player):
        self.__dominant_player = player

    def add_army(self, amount):
        self.__army += amount

    def get_army(self):
        return self.__army
        
    def get_dominant_player_name(self):
        if self.__dominant_player != None:
            return self.__dominant_player.get_name()
        else:
            return "None"
        
    def get_name(self):
        return self.__name
        
    def get_region(self):
        return self.__region