#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader
import pypandoc as pp
import os

class Template:
    """
    wrapper for dz template
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
            os.makedirs(self.outDir)


    def render(self):
        env = Environment(loader=FileSystemLoader('./templates/dz1'))
        template = env.get_template('template.html')
        n = len(self.slidesDict['Slides'])
        for sId in range(n):
            if 'Contents' in self.slidesDict['Slides'][sId]:
                self.slidesDict['Slides'][sId]['Contents'] = pp.convert_text(
                        self.slidesDict['Slides'][sId]['Contents'],
                         to='html5', format='markdown_github')
        out = template.render(self.slidesDict)
        return out.encode('utf8')
