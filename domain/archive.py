import csv


class Archive:
    def __init__(self. path_file):
        self.path_file = path_file

    def create_archive(self):
        with open(self.path_file, mode='w', encoding='utf-8') as file:
            csv_writer = csv.writer(file, delimiter=';')