from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print("###############")

        asd = toml.load(r"C:\Users\toni_\Koulu\ohtuvk1\ohtuvk123\viikko2\project-reader\pyproject.toml")
        pot = asd['tool']['poetry']

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(pot['name'], pot['description'], pot['dependencies'], pot['dev-dependencies'])
