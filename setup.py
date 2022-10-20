from setuptools import find_packages, setup
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

setup(
	name="myframeworks",
	version="0.1",
	packages=find_packages()
)
