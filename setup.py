from setuptools import setup, find_packages
#from init import __version__

__version__ = "0.0.1"

setup(
    name = "venndiagram",
    version = __version__,
    packages = find_packages(),

    author = "Maria Thieser",

    # automatic script creation
    entry_points = {
        'console_scripts': [
            'venndiagram = venndiagram.application:main',
        ]
    }
)
