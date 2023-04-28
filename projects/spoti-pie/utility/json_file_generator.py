from dotenv import load_dotenv
import os
import json

class JsonFileGenerator:
    def __init__(self):
        pass

    def json_generator(self, items, file_name):
        with open(file_name, 'w') as jsonfile:
            json.dump(items, jsonfile)

    def json_reader(self, file_path):
        with open(file_path, 'r') as file:
            file_content = json.loads(file.read())
        return file_content
