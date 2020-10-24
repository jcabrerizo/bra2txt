def getContent(source):
    try:
        f = open (source, 'r' )
    except FileNotFoundError:
        exit(f"File '{source}' not found")
    else:
        with f:
            return f.read()


def saveFile(content, dest):
    with open(dest, "w", encoding = 'UTF8') as f:
        f.write(content)