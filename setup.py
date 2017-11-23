from setuptools import setup

setup(
    name="pydavid",
    version=0.1,
    url="https://github.com/swarchal/pydavid",
    description="Get dataframes from DAVID queries",
    author="Scott Warchal",
    license="MIT",
    install_requires=["selenium", "bs4", "pandas"],
    tests_require=["pytest"]
    )
