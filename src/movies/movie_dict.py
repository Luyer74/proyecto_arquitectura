from abc import ABC, abstractmethod
import csv
import json

# Usando el Single Responsibility haciendo un modulo diferente


def store_movie_data(list):
    fields = ["preference_key", "movie_title", "star_cast",
              "rating", "year", "place", "vote", "link"]
    with open("movie_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for movie in list:
            writer.writerow({**movie})


class Exp(ABC):
    @abstractmethod
    def save(list):
        pass


class jsonExp(Exp):
    def save(list):
        json_object = json.dumps(list, indent=8)
        with open("movie_results.json", "w") as file:
            file.write(json_object)


class csvExp(Exp):
    def save(self, list):
        fields = ["preference_key", "movie_title", "star_cast",
                  "rating", "year", "place", "vote", "link"]
        with open("movie_results.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in list:
                writer.writerow({**movie})


class SimpleExpFac:

    def createExporter(exporterType: str) -> Exp:
        exporter: Exp = None

        if exporterType == "csv":
            exporter = csvExp()
        elif exporterType == "json":
            exporter = jsonExp()
        else:
            raise Exception("Exporter type not supported")

        return exporter
