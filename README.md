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
10. Entire standard library is now included

__Planned__

These features are planned (but may never be implemented):

1. Put out releases packaged with pyinstaller into a single executable
2. Include a few really useful packages like (and all of these might not be possible):
    1. paramiko
    2. pandas
    3. openpyxl
    4. IPython
    5. PyInstaller
    6. pip
    7. pexpect
    8. more to come as I think of them
3. provide a place to put executable scripts (like `bin` or `scripts`)
4. If you can think of anything else you'd like to see, please open an issue on GitHub or better yet a Pull Request

## Installing

Now that we have an official beta release, you can head over to the [downloads](https://github.com/iLoveTux/moon.py/releases/tag/0.6.0) and grab a copy.

There is no installation required. There is, however, one thing you should know about the binary releases, there are two files for each platform (except win32 because I don't actually have access to a 32 bit windows machine at the moment), a zip file and an executable file.

The executable file is ready to go, just grab it (and change the permissions if you have to) and run it. It is a full featured, single file Python distribution ready to go, but upon every execution it unzips itself into a temporary directory. This adds overhead, so if that's a problem grab the zip file.

The zip file can be extracted anywhere and it will make a directory called `./moonpy/` which contains everything you need to run. This only needs to be unzipped once and it can be executed with no additional overhead.

## Pre-Requisites

Building is quite simple, but first you have to have the pre-requisites installed:

1. [python](https://python.org)
2. [PyInstaller](http://www.pyinstaller.org/)
3. (windows only)[pyreadline](https://ipython.org/pyreadline.html)

### Additional pre-requisites for running tests

__NOTE__: The tests will only run on Linux for right now. The offending tests
are testing the ability to run scripts. They make a `NamedTemporaryFile`,
write code to them and point both moonpy and python at them. Windows does not
support having a file opened multiple times (at least I believe this is the
case I haven't actually tested this, but if things change please open an issue)

1. pexpect
2. py.test

to install these dependencies, issue the following commnd:

```
$ pip install pexpect
$ pip install py.test
```

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

Before building it would be a good idea to run the tests. If you've installed
the [Additional pre-requisites for running tests](#Additional-pre-requisites-for-running-tests)
then you simply need to navigate to the directory and issue the following
command:

```
py.test
```

Once The pre-requisites are installed, you simply need to issue the following command:

```
$ pyinstaller --onefile moonpy.py
```

This will give you a base executable, which is a fairly-fully featured Python interpreter, but it is missing most of the standard library. To get this you will need to copy the packages manually over to where the executable is located. For convenience's sake, if a directory named `site-packages` exists in the same directory as the executable, it will be added to the path (as well as the current directory).

## Usage

This file should behave exactly like python when the supported features are used. I mean to say, the features I've chosen to support should behave exactly like the official CPython executable (see [features](#features) for the list of supported features). If moonpy does not act like CPython, then it is a bug so please report it to the Github issue tracker or issue a pull request.

## Contributing

If you wish to contribute, please feel free to submit issues or issue
pull-requests. The coding-stlye here is:

> Try to be pep8 compliant, but I __REALLY__ want to keep this under 100
lines of code. Also every change should have an associated test.

Thanks for taking the time to stop by. Happy coding!
