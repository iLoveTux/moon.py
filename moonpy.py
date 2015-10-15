import os
import sys
import code
import runpy
import atexit
import readline
import argparse

here = os.path.dirname(os.path.abspath(__file__))
if "site-packages" in os.listdir(here):
    sys.path.insert(0, os.path.abspath(os.path.join(here, "site-packages")))
sys.path.insert(0, "")


def set_up_history():
    """Taken from https://docs.python.org/2/library/readline.html#example"""
    histfile = os.path.join(os.path.expanduser("~"), ".pyhist")
    try:
        readline.read_history_file(histfile)
    except IOError:
        pass
    atexit.register(readline.write_history_file, histfile)


def run_path(args):
    """Run a path (script, zip file, or dir) just like python <script>"""
    sys.argv.pop(0)
    fname = args.file
    runpy.run_path(fname, run_name="__main__")
    if args.i:
        interact()


def run_m(args):
    """Run a module, just like python -m <module_name>"""
    sys.argv = sys.argv[sys.argv.index("-m"):]
    sys.argv.remove(args.m)
    if not len(sys.argv):
        sys.argv.append("")
    runpy.run_module(args.m, run_name="__main__", alter_sys=True)
    sys.exit(0)


def run_c(args):
    """Run a command, just like python -c <command>"""
    sys.argv = sys.argv[sys.argv.index("-c"):]
    sys.argv.remove(args.c)
    sys.path.insert(0, os.path.abspath("."))
    interpreter = code.InteractiveInterpreter()
    interpreter.runsource(args.c)
    if args.i:
        interact()
    sys.exit(0)


def interact():
    set_up_history()
    console = code.InteractiveConsole({"exit": lambda x=0: sys.exit(x)})
    console.interact("MoonPy - m-o-o-n that spells Python")


def main(argv=sys.argv):
    """Business logic. respond to argv after parsing"""
    args = parse_args(argv)

    if "-m" in sys.argv and "-c" in sys.argv:
        func = run_m if sys.argv.index("-m") < sys.argv.index("-c") else run_c
        func(args)
    elif args.c:
        run_c(args)
    elif args.m:
        run_m(args)

    args.file = sys.stdin if args.file == "-" else args.file
    if args.file is sys.stdin:
        if args.file.isatty():
            interact()
        else:
            interpreter = code.InteractiveInterpreter()
            for line in args.file:
                interpreter.runsource(line)
    else:
        run_path(args)


def parse_args(argv):
    """parse argv"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true")
    parser.add_argument("-c", type=str, nargs="?")
    parser.add_argument("-m", type=str, nargs="?")
    parser.add_argument("file", type=str, default=sys.stdin, nargs="?")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    return parser.parse_args()


if __name__ == "__main__":
    main()
