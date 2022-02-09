import json


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
        with open(path + "\\" + file_name + ".json", "a") as file:
            try:
                parsed = json.loads(data.toJSON())
                file.write(json.dumps(parsed, indent=4, sort_keys=True))
                for line in data:
                    parsed = json.loads(line.toJSON())
                    file.write(json.dumps(parsed, indent=4, sort_keys=True))
            except Exception:
                pass
        file.close()

    @staticmethod
    def get_data_from_file(path, file_name):
        return open(path + "\\" + file_name, "r")
