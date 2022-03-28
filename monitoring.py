from abc import ABC, abstractmethod


class Monitoring(ABC):


    def __init__(self, database):
        self.database = database

    def insert_to_database(self, data):
        self.database.inset_to_database(data)



    @abstractmethod
    def get_measurements(self):
        pass
