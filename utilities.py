import yaml

def saveHTMLToFile(filename, HTML):
    with open(filename, "wb") as fh:
        fh.write(HTML.encode('utf8'))
        return
    print "Error: Cant save slides to file {}".format(filename)
    exit(0)

def readSlidesFile(filename):
    with open(filename, 'r') as f:
        t = yaml.load(f)
        return t
    print "Error: Cant load slides file {}".format(filename)
    exit(0)
