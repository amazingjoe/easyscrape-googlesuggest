from setuptools import setup, find_packages

VERSION = '0.0.5'
DESCRIPTION = 'Easy web scraping wrapper for Google Suggest results'
LONG_DESCRIPTION = 'This package provides a simple interface to request Google Suggest results for a given search term and returns those results as a List of strings.'

# Setting up
setup(
    name="easyscrape_googlesuggest",
    version=VERSION,
    author="Bald Man Codes (Joseph Ucuzoglu)",
    author_email="<baldmancodes@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests', 'json'],
    keywords=['web scrape', 'google suggest', 'google search', 'easyscrape'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)