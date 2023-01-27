#!/usr/bin/env python3

import subprocess
from os import remove
from os.path import exists, isfile
from shutil import which
from sys import stderr

from makegen.rule import Rule


def cmd_exists(file):
    return which(file) is not None


def touch(file: str) -> bool:
    if exists(file) or isfile(file):
        return False
    try:
        f = open(file, "w")
        f.write("")
        f.close()
        return True
    except OSError:
        print("OSError while creating file", file=stderr)
    return False


def run_make(file: str | None = None) -> bool:
    if not cmd_exists("make"):
        return False
    cmd = ["make"]
    if file is not None:
        if not (exists(file) or isfile(file)):
            return False
        cmd += ["-f", file]
    sub_prc = subprocess.run(cmd)
    return sub_prc.returncode == 0


def test_rule_basic() -> None:
    """
    Basic Rule Test

    This tests a basic makefile rule.
    """
    req_file_name = "world"
    touch(req_file_name)
    # Create Rule
    r = Rule("hello", "world")
    r.set_recipe([["ls", "-l", "."], ["echo", '"Hello, World!"']])
    # Read output makefile (runnable)
    cmp_file = open("./tests/rule_basic.Makefile")
    cmp_file_data = cmp_file.read()
    # Assert if both are same
    assert cmp_file_data == r.render()
    # Subproject Makefile
    run_make("./tests/rule_basic.Makefile")
    # Delete the file
    remove(req_file_name)
