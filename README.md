# moon.py
An awesome piece of hackery, a Python interpreter in less than 100 lines of code.

## Features

This interpreter is fairly full-featured. It supports:

1. Executing Python source files
2. Executing Python module directories (following the same rules as the Python 2.7 interpreter)
3. Executing ZIPed Python modules
4. Provides an enhanced interactive interpreter (cross-session history is the only enhancement, but still...)
4. Supports `-m` to execute a module on path
5. Supports `-c` to execute a Python command
6. Supports `-i` to drop into a python interpreter after executing a script or module
7. Supports a `site-packages` directory (must be in the same directory as the script)
8. Supports relative and absolute imports
9. Supports Python source being piped in on stdin

__Planned__

These features are planned (but may never be implemented):

1. Put out releases packaged with pyinstaller into a single executable
2. Include the Python Standard Library with it in the site-packages directory (I know
this isn't where they belong, but I really want to keep it under 100 lines of source,
and this seems like an acceptable sacrifice)
3. Include a few really useful packages like (and all of these might not be possible):
    1. paramiko
    2. pandas
    3. openpyxl
    4. IPython
    5. PyInstaller
    6. pip
    7. more to come as I think of them
4. provide a place to put executable scripts (like `bin` or `scripts`)
5. If you can think of anything else you'd like to see, please open an issue on GitHub or better yet a Pull Request

## Pre-Requisites

Building is quite simple, but first you have to have the pre-requisites installed:

1. [python](https://python.org)
2. [PyInstaller](http://www.pyinstaller.org/)
3. (windows only)[pyreadline](https://ipython.org/pyreadline.html)

### Python

I built this using Python 2.7, but I'd be very interested to hear how this works on other versions

The easiest way to install Python is from [The Official Site]( https://www.python.org/downloads/)

### PyInstaller

This used to "build" (rather bundle) the single-file executable

The easiest way to install PyInstaller is with `pip`

```
$ pip install pyinstaller
```

### pyreadline (windows only)

This is used to support command history in the interactive console and to persist
that history between sessions. This package is needed for Windows because they
do not include GNU readline and so the Python readline module is not available
for users within the Standard Library.

The easiest way to install pyreadline is to use `pip`:

```
C:\> pip install pyreadline
```

## Building

Once The pre-requisites are installed, you simply need to issue the following command:

```
$ pyinstaller --onefile moonpy.py
```

This will give you a base executable, which is a fairly-fully featured Python interpreter, but it is missing most of the standard library. To get this you will need to copy the packages manually over to where the executable is located. For convenience's sake, if a directory named `site-packages` exists in the same directory as the executable, it will be added to the path (as well as the current directory).

## Usage

This file should behave exactly like python when the supported features are used. I mean to say, the features I've chosen to support should behave exactly like the official CPython executable (see [features](#features) for the list of supported features). If moonpy does not act like CPython, then it is a bug so please report it to the Github issue tracker or issue a pull request.

## Contributing

If you wish to contribute, please feel free to submit issues or issue pull-requests. The coding-stlye here is:

> Try to be pep8 compliant, but I __REALLY__ want to keep this under 100 lines of code. As soon as I implement tests (very soon) every change should have an associated test.

Thanks for taking the time to stop by. Happy coding!
