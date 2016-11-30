#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader
import pypandoc as pp
from utilities import *
import os

def render(templateSource, slidesDict):
    template = templateSource.getTemplate()
    n = len(slidesDict['Slides'])
    for sId in range(n):
        if 'Contents' in slidesDict['Slides'][sId]:
            slidesDict['Slides'][sId]['Contents'] = pp.convert_text(
                    slidesDict['Slides'][sId]['Contents'],
                     to='html5', format='markdown_github')
    out = template.render(slidesDict)
    return out.encode('utf8')

class dz1Template:
    """
    wrapper for dz template
    """
    def __init__(self, outDir):
        """
        Init template setup
        Could also copy css and other files
        """
        self.outDir = outDir
        self.setupDir()
        self.outFile = os.path.join(outDir, "index.html")

    def setupDir(self):
        if not os.path.exists(self.outDir):
            os.makedirs(self.outDir)

    def getTemplate(self):
        env = Environment(loader=FileSystemLoader('./templates/dz1'))
        return env.get_template('index.html')


class revealJSTemplate:
    """
    wrapper for revealJS template
    """
    def __init__(self, outDir):
        """
        Init template setup
        Could also copy css and other files
        """
        self.outDir = outDir
        self.setupDir()
        self.outFile = os.path.join(outDir, "index.html")

    def setupDir(self):
        if not os.path.exists(self.outDir):
            copyDirectory("./templates/revealJS", self.outDir)

    def getTemplate(self):
        env = Environment(loader=FileSystemLoader('./templates/revealJS'))
        return env.get_template('index.html')
