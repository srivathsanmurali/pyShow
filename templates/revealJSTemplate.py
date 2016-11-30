#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader
import pypandoc as pp
import os
import shutil

class Template:
    """
    wrapper for revealJS template
    """
    def __init__(self, slidesDict, outDir):
        """
        Init template setup
        Could also copy css and other files
        """
        self.outDir = outDir
        self.setupDir()
        self.outFile = os.path.join(outDir, "index.html")
        self.slidesDict = slidesDict

    def setupDir(self):
        if not os.path.exists(self.outDir):
            copyDirectory("./templates/revealJS", self.outDir)

    def render(self):
        env = Environment(loader=FileSystemLoader('./templates/revealJS'))
        template = env.get_template('index.html')
        n = len(self.slidesDict['Slides'])
        for sId in range(n):
            if 'Contents' in self.slidesDict['Slides'][sId]:
                self.slidesDict['Slides'][sId]['Contents'] = pp.convert_text(
                        self.slidesDict['Slides'][sId]['Contents'],
                         to='html5', format='markdown_github')
        out = template.render(self.slidesDict)
        return out.encode('utf8')

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def test():
    test = Template(dict(), "./out")

if __name__ == "__main__":
    test()
