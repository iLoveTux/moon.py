# -*- coding: utf-8 -*-
import os
import sys
import mock
import moonpy
import pexpect
import unittest
import tempfile
import functools


class TestBasics(unittest.TestCase):
    def test_imports(self):
        from moonpy import set_up_history
        from moonpy import run_path
        from moonpy import run_m
        from moonpy import run_c
        from moonpy import interact
        from moonpy import main
        from moonpy import parse_args

class TestArgumentParser(unittest.TestCase):
    def test_dash_m(self):
        args = moonpy.parse_args(["-m", "module_1"])
        self.assertEqual(args.m, "module_1")

    def test_dash_c(self):
        args = moonpy.parse_args(["-c", "command"])
        self.assertEqual(args.c, "command")

    def test_dash_i(self):
        args = moonpy.parse_args(["-i"])
        self.assertEqual(args.i, True)

        args = moonpy.parse_args([])
        self.assertEqual(args.i, False)

    def test_file(self):
        args = moonpy.parse_args(["sample.py"])
        self.assertEqual(args.file, "sample.py")

    def test_file_defaults_stdin(self):
        args = moonpy.parse_args([])
        self.assertIs(args.file, sys.stdin)

    def test_dash_as_file(self):
        args = moonpy.parse_args(["-"])
        self.assertIs(args.file, sys.stdin)

    def test_dash_V(self):
        args = moonpy.parse_args(["-V"])
        self.assertIs(args.version, True)

        args = moonpy.parse_args(["--version"])
        self.assertIs(args.version, True)


def _mock_actions(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        with mock.patch.multiple("moonpy",
                                 set_up_history=mock.DEFAULT,
                                 run_path=mock.DEFAULT,
                                 run_m=mock.DEFAULT,
                                 run_c=mock.DEFAULT,
                                 interact=mock.DEFAULT) as patches:
            return func(*args, **kwargs)
    return _inner


# Integration Tests

def _compare_output_console(commands):
    prompt = ">>> "
    moonpy = pexpect.spawn("python moonpy.py")
    python = pexpect.spawn("python")
    interpreters = (moonpy, python)
    [interpreter.expect(prompt) for interpreter in interpreters]
    for command in commands:
        [interpreter.sendline(command) for interpreter in interpreters]
        [interpreter.expect([prompt, pexpect.EOF]) for interpreter in interpreters]
        yield python.before, moonpy.before


def _compare_output_script(content):
    t_file = tempfile.NamedTemporaryFile("r+")
    os.chmod(t_file.name, 0777)
    t_file.write(content)
    t_file.seek(0)
    fname = t_file.name
    python = pexpect.spawn("python {}".format(fname))
    moonpy = pexpect.spawn("python moonpy.py {}".format(fname))
    python.expect(pexpect.EOF)
    moonpy.expect(pexpect.EOF)
    return python.before, moonpy.before


def _compare_output_dash_c(command):
    python = pexpect.spawn("python -c '{}'".format(command))
    moonpy = pexpect.spawn("python moonpy.py -c '{}'".format(command))
    python.expect(pexpect.EOF)
    moonpy.expect(pexpect.EOF)
    return python.before, moonpy.before


class TestOutputMatchesPythonConsole(unittest.TestCase):
    def test_argv(self):
        self.assertTrue(
            _compare_output_console(["import sys", "print sys.argv", "exit()"]))

    def test_os_listdir(self):
        commands = ["import os", "print os.listdir('.')", "exit()"]
        for pyout, moonout in _compare_output_console(commands):
            self.assertEqual(pyout, moonout)


class TestOutputMatchesPythonScript(unittest.TestCase):
    def test_env(self):
        content = """
import os
print os.environ
"""
        self.assertEqual(*_compare_output_script(content))

    def test_argv(self):
        content = """
import sys
print sys.argv
"""
        self.assertEqual(*_compare_output_script(content))

    def test_file_and_name(self):
        content = """
print __file__
print __name__
"""
        self.assertEqual(*_compare_output_script(content))

class TestDashc(unittest.TestCase):
    def test_argv(self):
        command = "import sys; print sys.argv"
        self.assertEqual(*_compare_output_dash_c(command))

        command = "import sys; print sys.argv' -m markdown"
        self.assertEqual(*_compare_output_dash_c(command))

    def test_environ(self):
        command = "import os; print os.environ"
        self.assertEqual(*_compare_output_dash_c(command))
