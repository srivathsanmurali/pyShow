import yaml
import shutil

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

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

