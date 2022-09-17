from setuptools import find_packages, setup


setup(
    name="tsukuda_fib_py",
    version="0.0.1",
    author="tsukudamayo",
    author_email="tsukudamayo@gmail.com",
    description="Calculates a FIbonacci number",
    long_description="A basic library that calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/tsukudamayo/tsukuda-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    test_requires=["pytest"],
)

