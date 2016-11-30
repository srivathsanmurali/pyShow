import sys
from templates import *
from utilities import *

def main():
    if len(sys.argv) < 3:
        print "WRONG"
        exit()

    slides = readSlidesFile(sys.argv[1])
    temp = dz1Template(sys.argv[2])
    out = render(temp, slides)
    saveHTMLToFile(temp.outFile, out)

if __name__ == "__main__":
    main()
