import sys
from database import Database
from colorama import Fore 

class BotFunctions:
    def __init__(self):
        self.functions = {
            'cписок рослин' : self.see_all_plant, 
            'купити квіти': self.see_all_plant,
            'кількість усіх рослин': self.get_all_plant_quantity, 
            'опис рослини': self.see_plant_data,
            'ціна рослини': self.see_plant_data,
            'наявність рослини': self.see_plant_data,
            "у продажі": self.see_plant_data,
            'кількість рослини': self.see_plant_data,
            'додати рослину': self.add_plant,
            'видалити рослину': self.delete_plant,
            'вийти': self.stop_bot
        }
        self.database = Database()


    def add_plant(self, entities, actions):
        try:
            self.database.add_data()
            print( Fore.GREEN +"Успішно додано!" + Fore.RESET)
        except Exception as ex:
            print(Fore.RED +f"Не вдалось додати дані. {str(ex)}" + Fore.RESET)
    
    def delete_plant(self, entities, actions):
        try:
            self.database.delete_data()
            print(Fore.GREEN + "Успішно видалено!" + Fore.RESET)
        except:
            print(Fore.RED + "Не вдалось видалити дані." + Fore.RESET)

    def see_all_plant(self, entities, actions):
        data = self.database.see_all_data()
        if data is not None:
            print(Fore.GREEN + "Ось усі дані: " + Fore.BLUE)
            print(data)
            print(Fore.RESET)
        else:
            print(Fore.RED + "Схоже, даних ще немає." + Fore.RESET)

    def see_plant_data(self, entities, actions):
        data = self.database.see_plant_data(entities, actions)
        if data is not None:
            print(Fore.GREEN + "Ось що вдалось знайти: " + Fore.BLUE)
            print(data)
            print(Fore.RESET)
        else:
            print(Fore.RED + "Не вдалось знайти дані." + Fore.RESET)

    def get_all_plant_quantity(self, entities, actions):
        data = self.database.see_all_plant_quantity()
        if data is not None:
            print(Fore.GREEN + f"На даний момент у магазині {data} видів рослин." + Fore.RESET)
        else:
            print(Fore.RED + "Не вдалось підрахувати дані." + Fore.RESET)

    @staticmethod
    def stop_bot(entities, actions):
        print(Fore.GREEN + "Було приємно попрацювати :)")
        sys.exit()
