from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win64":
    base = "Win64GUI"

setup(name='Blood cell',
      version='0.0.1',
      description='Biology education App!',
      executables=[Executable("main.py", base=base)])
