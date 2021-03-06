# setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my_function-lambdata-codingduckmx",
    version="0.0.0.2",
    author="Jesus Caballero",
    author_email="jcm@ciencias.unam.mx",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/CodingDuckmx/lambdata-codingduckmx",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)