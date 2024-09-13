import io
from territory import Territory
from objective import Objective

class DataManager():

    @staticmethod
    def __normalized_string_data(str_line):
        return str_line.replace('\n', '')

    @staticmethod
    def __extract_data(filename):
        data = []
        with io.open(file=filename, mode='r', encoding='utf-8') as file:
            for line in file:
                normalized_data = DataManager.__normalized_string_data(line)
                data.append(normalized_data)
        return data
    
    @staticmethod
    def load_data_to(objective_list_destination, territory_map_destination):
        objectivesData = DataManager.__extract_data("data/objectives.txt")
        for objective_text in objectivesData:
            objective_list_destination.append(Objective(text=objective_text))

        territoryData = DataManager.__extract_data("data/territories.txt")
        for territory in territoryData:
            normalized_territory = territory.split(",")
            territory_map_destination.add_territory(Territory(name=normalized_territory[0], region=normalized_territory[1]))

