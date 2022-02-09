class Load:
    def create_file(self, data, path, file_name):
        try:
            file = open(path + "\\" + file_name, "x")
            file.write(data)
            file.close()
        except FileExistsError:
            pass

    def load_data_to_file(self, data, path, file_name):
        file = open(path + "\\" + file_name, "a")
        file.write(str(data))
        file.close()

    def get_data_from_file(self, path, file_name):
        return open(path + "\\" + file_name, "r")
