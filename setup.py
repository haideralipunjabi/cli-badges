import setuptools
from cli_badges import __version__
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cli_badges", # Replace with your own username
    version=__version__,
    author="Haider Ali Punjabi",
    author_email="me@haideralipunjabi.com",
    keywords=["color","colour","paint","ansi","terminal","linux","python","cli","badges","cli-badges","terminal-badges","console","console-badges"],
    description="Quirky little python package for generating badges for your cli apps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haideralipunjabi/cli-badges",
    packages=["cli_badges"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Other",
        "Programming Language :: Unix Shell",
        "Topic :: Terminals"
    ],
    python_requires='>=3.6',
)