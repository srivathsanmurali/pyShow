import sys
from templates import *
from utilities import *
import argparse
import pyinotify

class OnWriteHandler(pyinotify.ProcessEvent):
    def my_init(self,filename, manager):
        self.filename = filename
        self.manager = manager

    def process_IN_MODIFY(self, event):
        if not event.pathname.endswith(self.filename):
            return
        print '{} updated'.format(self.filename)
        self.manager.processJob()

class Manager:
    """
    Manages the entire process
    """
    def __init__(self, args):
        self.args = args;
        self.templateDict = {'dz1': dz1Template,
                            'revealJS': revealJSTemplate}
        self.temp = self.templateDict[self.args.template](self.args.outDir)

        self.processJob()

    def processJob(self):
        slides = readSlidesFile(self.args.input)
        out = render(self.temp, slides)
        saveHTMLToFile(self.temp.outFile, out);
        print 'Template Generated from {}. Presentation dumped to {}'.format(
                self.args.input, self.args.outDir)

    def watch(self):
        (filepath, filename) = os.path.split(self.args.input)
        wm = pyinotify.WatchManager()
        event_handler = OnWriteHandler(filename=filename, manager=self)
        notifier = pyinotify.Notifier(wm, default_proc_fun=event_handler)
        wm.add_watch(filepath, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
        print '==> Start monitoring {} (type c^c to exit)'.format(filepath)
        notifier.loop()


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

    parser.add_argument('--watch', '-w', dest='watch', action='store_true')

    args = parser.parse_args()
    args.input = os.path.abspath(args.input)
    args.outDir= os.path.abspath(args.outDir)

    manager = Manager(args)

    if args.watch:
        manager.watch()

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
