from setuptools import setup, find_packages
import pathlib


with open("README.md", "r") as fh:
    long_description = fh.read()

with open(str(pathlib.Path(__file__).parent.absolute()) + "/tsukuda_fib_py/version.py", "r") as fh:
    version = fh.read().split("=")[1].replace("'", "")

setup(
    name="tsukuda_fib_py",
    version=version,
    author="tsukudamayo",
    author_email="tsukudamayo@gmail.com",
    description="Calculates a FIbonacci number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsukudamayo/tsukuda-fib-py",
    install_requires=[
        "PyYAML>=4.1.2",
        "dill>=0.2.8",
    ],
    extras_require={
        "server": ["Flask>=1.0.0"]
    },
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fib-number = tsukuda_fib_py.cmd.fib_numb:fib_numb",
        ],
    },
    python_requires=">=3",
    test_requires=["pytest"],
)
