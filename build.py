import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["time"], "packages": ["pygame"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="testgame",
    version="beta0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("game.py", base=base)],
)
