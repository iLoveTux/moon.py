import os
import sys
import code
import runpy
import atexit
import argparse
import __builtin__

_locals = {'__builtins__': __builtin__, '__name__': '__main__', '__doc__': None, '__package__': None}

__version__ = "moonpy 0.6.0"

def set_up_history():
    """Taken from https://docs.python.org/2/library/readline.html#example"""
    try: import readline
    except ImportError: import pyreadline as readline
    histfile = os.path.join(os.path.expanduser("~"), ".pyhist")
    try: readline.read_history_file(histfile)
    except IOError: pass
    atexit.register(readline.write_history_file, histfile)

def run_path(args):
    """Run a path (script, zip file, or dir) just like python <script>"""
    sys.argv.pop(0)
    fname = args.file
    __locals = runpy.run_path(fname, run_name="__main__", init_globals=_locals)
    if args.i:
        interact(code.InteractiveConsole(locals=__locals))

def run_m(args):
    """Run a module, just like python -m <module_name>"""
    sys.argv = sys.argv[sys.argv.index("-m"):]
    sys.argv.remove(args.m)
    if not len(sys.argv): sys.argv.append("")
    runpy.run_module(args.m, run_name="__main__", alter_sys=True)
    sys.exit(0)

def run_c(args):
    """Run a command, just like python -c <command>"""
    sys.argv = ["-c"]
    sys.path.insert(0, os.path.abspath("."))
    interpreter = code.InteractiveConsole(locals=_locals)
    interpreter.runsource(args.c)
    if args.i:
        interpreter.locals["exit"] = sys.exit; interact(interpreter)
    sys.exit(0)

def run_stdin(stdin):
    sys.argv[0] = ""; sys.path.insert(0, "")
    _locals = {"exit": sys.exit, "__file__": stdin.name}
    interpreter = code.InteractiveInterpreter(locals=_locals)
    [interpreter.runsource(line) for line in stdin]
    sys.exit(0)

def interact(console=None):
    """Launch an enhanced, interactive Python interpreter"""
    set_up_history()
    sys.argv = [""]
    if not console:
        console = code.InteractiveConsole(
            locals=_locals)
    console.interact("MoonPy - m-o-o-n that spells Python")

def main(argv=None):
    """Business logic. respond to argv after parsing"""
    here = os.path.dirname(os.path.abspath(__file__))
    if "site-packages" in os.listdir(here):
        sys.path.insert(0, os.path.abspath(os.path.join(here, "site-packages")))
    args = parse_args(argv)
    if args.version: print __version__; sys.exit(0)
    if "-m" in sys.argv and "-c" in sys.argv:
        func = run_m if sys.argv.index("-m") < sys.argv.index("-c") else run_c
        func(args)
    elif args.c: run_c(args)
    elif args.m: run_m(args)
    if args.file is sys.stdin:
        if args.file.isatty():
            interact()
        else:
            run_stdin(args.file)
    else:
        run_path(args)

def parse_args(argv=None):
    """parse argv"""
    argv = sys.argv[1:] if argv is None else argv
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", action="store_true")
    parser.add_argument("-V", "--version", action="store_true")
    parser.add_argument("-c", type=str, nargs="?")
    parser.add_argument("-m", type=str, nargs="?")
    parser.add_argument("file", type=str, default="-", nargs="?")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    args = parser.parse_args(argv)
    args.file = sys.stdin if args.file == "-" else args.file
    return args

if __name__ == "__main__":
    main()
