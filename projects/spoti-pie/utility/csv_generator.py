from dotenv import load_dotenv
import os
import csv

class CsvFileGenerator:
    def __init__(self, fileds, items):
        load_dotenv()
        self.fields = fileds
        self.items = items
        self.file_name = os.getenv("CSV_FILE_NAME")

    def csv_generator(self):
        with open(self.file_name, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = self.fields)
            writer.writeheader()
            writer.writerows(self.items)
