from workspace.ETL import Extract
from workspace.ETL import Transform
from workspace.ETL import Load


class ETLManager():
    def __init__(self, path):
        self._data = list()
        self._path_file = path  # r"C:\BasicCourse\Tasks\Spotipy\songs\\"

    # Reads and extracts the JSON file.
    def extract(self):
        extractor = Extract
        self._data = extractor.Extract.extract_data(self._path_file)

    # Saves the JSON data into an object.
    def transform(self):
        tranformer = Transform
        self._data = tranformer.Transform.transform_data(self._data)

    # Saves the data into a file.
    def load(self):
        loader = Load
