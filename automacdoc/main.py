#!/usr/bin/env python
import os
import sys
from time import sleep
from subprocess import call, Popen
import webbrowser
from automacdoc import write_doc

def main(argv=None):
    argv = sys.argv if argv is None else argv
    write_doc(argv[1], argv[2])

    sleep(1)

    os.chdir(argv[2])

    call(["mkdocs", "build", "--clean"])
    Popen(["mkdocs", "serve"])

    sleep(2)

    webbrowser.open("http://127.0.0.1:8000/")

if __name__ == "__main__":
    main(sys.argv)
