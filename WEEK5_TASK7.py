class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def append(self, content):
        with open(self.filename, 'a') as f:
            f.write(content)
