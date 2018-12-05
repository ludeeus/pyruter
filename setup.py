"""Setup configuration."""
import setuptools

with open("README.md", "r") as fh:
    LONG = fh.read()
setuptools.setup(
    name="pyruter",
    version="1.2.4",
    author="Joakim Sorensen",
    author_email="ludeeus@gmail.com",
    description="",
    long_description=LONG,
    install_requires=['aiohttp', 'async_timeout', 'click'],
    long_description_content_type="text/markdown",
    url="https://github.com/ludeeus/pyruter",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts': [
            'pyruter = pyruter.cli:CLI'
        ]
    },
)
