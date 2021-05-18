from setuptools import setup
from io import open
import re

def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()

with open('bitly/__init__.py', 'r', encoding='utf-8') as f:
    version = re.search(r"^__version__\s*=\s*'(.*)'.*$",
                        f.read(), flags=re.MULTILINE).group(1)

setup(name='python-bitly',
      version = version,
      description = 'Python Bitly API',
      author = 'Andrea Barbagallo',
      author_email = 'andreabarbagallo.ab7@gmail.com',
      url = 'https://github.com/barbax7/python_bitly',
      packages = ['bitly'],
      license = 'GPL2',
      install_requires = ['requests'])