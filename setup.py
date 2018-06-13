from setuptools import setup, find_packages
import os

#credits: https://pythonhosted.org/an_example_pypi_project/setuptools.html
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nolimit",
    version = "0.1",
    author = "Saverio Morelli, Simone Massaro",
    author_email = "saverio.morelli@outlook.it, mone.massaro@gmail.com",
    description = "simple desktop program to solve limits using Qt5 gui",
    license = "GPL",
    keywords = "example documentation tutorial",
    url = "https://www.saveriomorelli.com/nolimitmath/",
    packages=['nolimit', 'nolimit.sympy'],
    package_data={
        '':['*.ui', '*.png']
    },
    install_requires=['numpy', 'sympy', 'matplotlib', 'PyQt5'],
    entry_points={
        'gui_scripts': [
            'nolimit = nolimit.main:main',
            'nolimit_sympy = nolimit.sympy.nolimit_sympy:main'
        ]
    },
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)