import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="pyruter",
    version="0.0.3",
    author="Joakim Sorensen",
    author_email="joasoe@gmail.com",
    description="A module to get information about the next departure from a stop..",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pyruter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)