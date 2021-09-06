from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2.10.0'
DESCRIPTION = 'Simple methods for working with coinmarketcap API'
LONG_DESCRIPTION = 'Search for actual Price of multiple coins, make conversions, get coins by price, volume and change'

# Setting up
setup(
    name="CoinCrypt",
    version=VERSION,
    author="Henrique Domiciano Osinski",
    author_email="<henriquedomiciano@yahoo.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests'],
    icense_files = ('LICENSE',),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)