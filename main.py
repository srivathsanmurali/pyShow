import sys
from templates import *
from utilities import *
import argparse

def main():
    parser = argparse.ArgumentParser(description="Make HTML presentation from markdown styled input.")
    parser.add_argument('--template', '-t', dest='template',
                        default='dz1',
                        choices=['dz1', 'revealJS'],
                        help='template to be used (default:dz1)')
    parser.add_argument('--inFile', '-i', dest='input',
                        required=True,
                        help='Markdown styled file to be processed')
    parser.add_argument('--outDir', '-o', dest='outDir',
                        required=True,
                        help='Output dump directory')

    templateDict = {'dz1': dz1Template,
                    'revealJS': revealJSTemplate}

    args = parser.parse_args()

    slides = readSlidesFile(args.input)
    temp = templateDict[args.template](args.outDir)
    out = render(temp, slides)
    saveHTMLToFile(temp.outFile, out);

def test():
    if len(sys.argv) < 3:
        print "WRONG"
        exit()

    slides = readSlidesFile(sys.argv[1])
    temp = revealJSTemplate(sys.argv[2])
    out = render(temp, slides)
    saveHTMLToFile(temp.outFile, out)

if __name__ == "__main__":
    main()
