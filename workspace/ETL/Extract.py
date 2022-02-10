import os
import json
import logging


class Extract:
    @staticmethod
    def extract_data(path):
        logging.basicConfig(filename="search_log_file.log", format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()

        path_to_json = path
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

        entities_list = list()

        for file in json_files:
            with open(path_to_json + file) as file:
                for json_obj in file:
                    json_dict = json.loads(json_obj)
                    entities_list.append(json_dict)

        if not entities_list:
            logger.error("Error! Couldn't read the tracks from the file.")

        return entities_list
