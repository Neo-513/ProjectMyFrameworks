import os

commands = [
	"d:",
	"cd d:/workspace_PyCharm/ProjectMyFrameworks",
	"python setup.py sdist",
	"pip install dist/myframeworks-0.1.tar.gz"
]
os.system(" & ".join(commands))
