from setuptools import find_packages, setup

NAME = "ampersand"
VERSION = "0.0.2"
URL = "https://github.com/SamimiesGames/Ampersand"

AUTHOR = "Samimies"
DESCRIPTION = "Ampersand virtual machine"


setup(
    name=NAME,
    version=VERSION,
    url=URL,
    author=AUTHOR,
    license="GPL-3.0 License",
    description=DESCRIPTION,
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"], where="src"),
    package_dir={"": "src"}
)
