class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.f = open(filename, mode='rt', encoding='utf-8')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()
