if False:
    import __builtin__
    import __future__
    import __main__
    import _winreg
    import abc
    import aepack
    import aetools
    import aetypes
    import aifc
    import al
    import AL
    import anydbm
    import applesingle
    import argparse
    import array
    import ast
    import asynchat
    import asyncore
    import atexit
    import audioop
    import autoGIL
    import base64
    import BaseHTTPServer
    import Bastion
    import bdb
    import binascii
    import binhex
    import bisect
    import bsddb
    import buildtools
    import bz2
    import calendar
    import Carbon.AE
    import Carbon.AH
    import Carbon.App
    import Carbon.Appearance
    import Carbon.CarbonEvents
    import Carbon.CarbonEvt
    import Carbon.CF
    import Carbon.CG
    import Carbon.Cm
    import Carbon.Components
    import Carbon.ControlAccessor
    import Carbon.Controls
    import Carbon.CoreFounation
    import Carbon.CoreGraphics
    import Carbon.Ctl
    import Carbon.Dialogs
    import Carbon.Dlg
    import Carbon.Drag
    import Carbon.Dragconst
    import Carbon.Events
    import Carbon.Evt
    import Carbon.File
    import Carbon.Files
    import Carbon.Fm
    import Carbon.Folder
    import Carbon.Folders
    import Carbon.Fonts
    import Carbon.Help
    import Carbon.IBCarbon
    import Carbon.IBCarbonRuntime
    import Carbon.Icns
    import Carbon.Icons
    import Carbon.Launch
    import Carbon.LaunchServices
    import Carbon.List
    import Carbon.Lists
    import Carbon.MacHelp
    import Carbon.MediaDescr
    import Carbon.Menu
    import Carbon.Menus
    import Carbon.Mlte
    import Carbon.OSA
    import Carbon.OSAconst
    import Carbon.Qd
    import Carbon.Qdoffs
    import Carbon.QDOffscreen
    import Carbon.Qt
    import Carbon.QuickDraw
    import Carbon.QuickTime
    import Carbon.Res
    import Carbon.Resources
    import Carbon.Scrap
    import Carbon.Snd
    import Carbon.Sound
    import Carbon.TE
    import Carbon.TextEdit
    import Carbon.Win
    import Carbon.Windows
    import cd
    import cfmfile
    import cgi
    import CGIHTTPServer
    import cgitb
    import chunk
    import cmath
    import cmd
    import code
    import codecs
    import codeop
    import collections
    import ColorPicker
    import colorsys
    import commands
    import compileall
    import compiler
    import compiler.ast
    import compiler.visitor
    import ConfigParser
    import contextlib
    import Cookie
    import cookielib
    import copy
    import copy_reg
    import cPickle
    import cProfile
    import crypt
    import cStringIO
    import csv
    import ctypes
    import curses
    import curses.ascii
    import curses.panel
    import curses.textpad
    import datetime
    import dbhash
    import dbm
    import decimal
    import DEVICE
    import difflib
    import dircache
    import dis
    import distutils
    import distutils.archive_util
    import distutils.bcppcompiler
    import distutils.ccompiler
    import distutils.cmd
    import distutils.command
    import distutils.command.bdist
    import distutils.command.bdist_dumb
    import distutils.command.bdist_msi
    import distutils.command.bdist_packager
    import distutils.command.bdist_rpm
    import distutils.command.bdist_wininst
    import distutils.command.build
    import distutils.command.build_clib
    import distutils.command.build_ext
    import distutils.command.build_py
    import distutils.command.build_scripts
    import distutils.command.check
    import distutils.command.clean
    import distutils.command.config
    import distutils.command.install
    import distutils.command.install_data
    import distutils.command.install_headers
    import distutils.command.install_lib
    import distutils.command.install_scripts
    import distutils.command.register
    import distutils.command.sdist
    import distutils.core
    import distutils.cygwinccompiler
    import distutils.debug
    import distutils.dep_util
    import distutils.dir_util
    import distutils.dist
    import distutils.emxccompiler
    import distutils.errors
    import distutils.extension
    import distutils.fancy_getopt
    import distutils.file_util
    import distutils.filelist
    import distutils.log
    import distutils.msvccompiler
    import distutils.spawn
    import distutils.sysconfig
    import distutils.text_file
    import distutils.unixccompiler
    import distutils.util
    import distutils.version
    import dl
    import doctest
    import DocXMLRPCServer
    import dumbdbm
    import dummy_thread
    import dummy_threading
    import EasyDialogs
    import email
    import email.charset
    import email.encoders
    import email.errors
    import email.generator
    import email.header
    import email.iterators
    import email.message
    import email.mime
    import email.parser
    import email.utils
    import encodings.idna
    import encodings.utf_8_sig
    import ensurepip
    import errno
    import exceptions
    import fcntl
    import filecmp
    import fileinput
    import findertools
    import FL
    import fl
    import flp
    import fm
    import fnmatch
    import formatter
    import fpectl
    import fpformat
    import fractions
    import FrameWork
    import ftplib
    import functools
    import future_builtins
    import gc
    import gdbm
    import gensuitemodule
    import getopt
    import getpass
    import gettext
    import gl
    import GL
    import glob
    import grp
    import gzip
    import hashlib
    import heapq
    import hmac
    import hotshot
    import hotshot.stats
    import htmlentitydefs
    import htmllib
    import HTMLParser
    import httplib
    import ic
    import icopen
    import imageop
    import imaplib
    import imgfile
    import imghdr
    import imp
    import importlib
    import imputil
    import inspect
    import io
    import itertools
    import jpeg
    import json
    import keyword
    import lib2to3
    import linecache
    import locale
    import logging
    import logging.config
    import logging.handlers
    import macerrors
    import MacOS
    import macostools
    import macpath
    import macresource
    import mailbox
    import mailcap
    import marshal
    import math
    import md5
    import mhlib
    import mimetools
    import mimetypes
    import MimeWriter
    import mimify
    import MiniAEFrame
    import mmap
    import modulefinder
    import msilib
    import msvcrt
    import multifile
    import multiprocessing
    import multiprocessing.connection
    import multiprocessing.dummy
    import multiprocessing.managers
    import multiprocessing.pool
    import multiprocessing.sharedctypes
    import mutex
    import Nav
    import netrc
    import new
    import nis
    import nntplib
    import numbers
    import operator
    import optparse
    import os
    import os.path
    import ossaudiodev
    import parser
    import pdb
    import pickle
    import pickletools
    import pipes
    import PixMapWrapper
    import pkgutil
    import platform
    import plistlib
    import popen2
    import poplib
    import posix
    import posixfile
    import pprint
    import profile
    import pstats
    import pty
    import pwd
    import py_compile
    import pyclbr
    import pydoc
    import Queue
    import quopri
    import random
    import re
    import readline
    import resource
    import rexec
    import rfc822
    import rlcompleter
    import robotparser
    import runpy
    import sched
    import ScrolledText
    import select
    import sets
    import sgmllib
    import sha
    import shelve
    import shlex
    import shutil
    import signal
    import SimpleHTTPServer
    import SimpleXMLRPCServer
    import site
    import smtpd
    import smtplib
    import sndhdr
    import socket
    import SocketServer
    import spwd
    import sqlite3
    import ssl
    import stat
    import statvfs
    import string
    import StringIO
    import stringprep
    import struct
    import subprocess
    import sunau
    import sunaudiodev
    import SUNAUDIODEV
    import symbol
    import symtable
    import sys
    import sysconfig
    import syslog
    import tabnanny
    import tarfile
    import telnetlib
    import tempfile
    import termios
    import test
    import test.test_support
    import textwrap
    import thread
    import threading
    import time
    import timeit
    import Tix
    import Tkinter
    import token
    import tokenize
    import trace
    import traceback
    import ttk
    import tty
    import turtle
    import types
    import unicodedata
    import unittest
    import urllib
    import urllib2
    import urlparse
    import user
    import UserDict
    import UserList
    import UserString
    import uu
    import uuid
    import videoreader
    import warnings
    import wave
    import weakref
    import webbrowser
    import whichdb
    import winsound
    import wsgiref
    import wsgiref.handlers
    import wsgiref.headers
    import wsgiref.simple_server
    import wsgiref.util
    import wsgiref.validate
    import xdrlib
    import xml
    import xml.dom
    import xml.dom.minidom
    import xml.dom.pulldom
    import xml.etree.ElementTree
    import xml.parsers.expat
    import xml.sax
    import xml.sax.handler
    import xml.sax.saxutils
    import xml.sax.xmlreader
    import xmlrpclib
    import zipfile
    import zipimport
    import zlib
