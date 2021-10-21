import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["PyPDF2", "PIL"], "includes": ["tkinter"], "include_files": ["logo.png"]}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Extrator de Textos PDF",
    version = "0.1",
    description = "Lê que é uma beleza",
    options = {"build_exe": build_exe_options},
    executables = [Executable("app.py", base=base)]

)