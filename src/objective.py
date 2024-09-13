class Objective():

    def __init__(self, text):
        self.__complete = False
        self.__text = text
    
    def get_objective(self):
        return self.__text
    
    def set_complete (self):
        self.__complete = True