class CSVFileStorage:

    directory_name: str = "./SensorData/"
    filepath: str = ""
    hedder: str = ""

    def __init__(self, filename: str, header: str):
        self.filename = filename
        self.filepath = self.directory_name + filename
        self.header = header
        self.save(self.header)


    def save(self, data:str):
        with open(self.filepath, 'w') as f:
            f.write(data)

    def load(self):
        with open(self.filepath, 'r') as f:
            return f.read()