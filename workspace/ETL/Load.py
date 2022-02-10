import json
import logging


class Load:
    @staticmethod
    def create_file(path, file_name):
        try:
            file = open(path + "\\" + file_name, "x")
            file.close()
        except FileExistsError:
            pass

    @staticmethod
    def load_data_to_file(data, path, file_name):
        logging.basicConfig(filename="search_log_file.log", format='%(asctime)s %(message)s', filemode='w')
        logger = logging.getLogger()

        obj_list = []
        with open(path + "\\" + file_name + ".json", "a+") as file:
            if type(data) is list:
                for line in data:
                    obj_list.append(line.__dict__)
                json.dump(obj_list, file)
            else:
                try:
                    json_data = json.load(file)
                    json_data.update(data.__dict__)
                    file.seek(0)
                    json.dump(json_data, file)
                except Exception:
                    logger.debug("Trouble with dumping the data into a JSON file.")
                    json.dump(data.__dict__, file)
        file.close()

    @staticmethod
    def get_data_from_file(path, file_name):
        return open(path + "\\" + file_name, "r")
