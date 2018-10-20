"""Setup."""
import setuptools
with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pyruter",
    version="0.1.1",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="""
    A module to get information about the next departure from a stop..
    """,
    long_description=LONG,
    install_requires=['requests'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pyruter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
