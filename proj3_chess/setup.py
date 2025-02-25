from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

setup(
    name="chess",
    version="0.0.1",
    description="Maiiiiiiiii",
    long_description_content_type="text/markdown",
    long_description="A package for creating and managing chess pieces on a chessboard",
    packages=find_packages(),
)
