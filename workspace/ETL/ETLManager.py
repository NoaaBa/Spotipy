from workspace.ETL import Extract
from workspace.ETL import Transform
from workspace.ETL import Load


class ETLManager():
    def __init__(self, path, path_to_load, file_name):
        self._data = list()
        self._path_extract_file = path
        self._path_to_load = path_to_load
        self._file_name = file_name

    def run(self):
        self.extract()
        self.transform()
        self.load(self._data, self._path_to_load, self._file_name)

    # Reads and extracts the JSON file.
    def extract(self):
        extractor = Extract
        self._data = extractor.Extract.extract_data(self._path_extract_file)

    # Saves the JSON data into an object.
    def transform(self):
        transformer = Transform
        self._data = transformer.Transform.transform_data(self._data)

    # Saves the data into a file.
    def load(self, data, path, file_name):
        load = Load
        load.Load.create_file(path, file_name)
        load.Load.load_data_to_file(data, path, file_name)
