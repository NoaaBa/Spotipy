import os, json


class Extract:
    @staticmethod
    def extract_data(path):

        path_to_json = path
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

        entities_list = list()

        for file in json_files:
            with open(path_to_json + file) as file:
                for json_obj in file:
                    json_dict = json.loads(json_obj)
                    entities_list.append(json_dict)

        return entities_list
