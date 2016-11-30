import sys
from templates.dz1Template import Template
from utilities import *

def main():
    if len(sys.argv) < 3:
        print "WRONG"
        exit()

    slides = readSlidesFile(sys.argv[1])
    temp = Template(slides, sys.argv[2])
    out = temp.render()
    saveHTMLToFile(temp.outFile, out)

if __name__ == "__main__":
    main()
