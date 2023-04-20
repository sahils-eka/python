from dotenv import load_dotenv
import os
import json

class JsonFileGenerator:
    def __init__(self, items):
        load_dotenv()
        self.items = items
        self.file_name = os.getenv("JSON_FILE_NAME")

    def json_generator(self):
        with open(self.file_name, 'w') as jsonfile:
            json.dump(self.items, jsonfile)
