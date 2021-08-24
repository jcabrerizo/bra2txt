class StorageManager:
    def getContent(self, source, encoding):
        try:
            f = open (source, 'r', encoding=encoding)
        except FileNotFoundError:
            exit(f"File '{source}' not found")
        else:
            with f:
                return f.read()


    def saveFile(self, content, dest, encoding):
        with open(dest, "w", encoding = encoding) as f:
            f.write(content)