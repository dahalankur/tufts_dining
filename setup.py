from setuptools import setup, find_packages

setup(
    name="tufts_dining_api",
    version="1.0",
    packages=find_packages(),
    description="A Python API for retrieving Tufts Dining menus",
    url="https://github.com/dahalankur/tufts_dining_api",
    author="Ankur Dahal",
    author_email="dahalankur123@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    keywords="tufts-dining tufts dining-api",
    install_requires=[
        "beautifulsoup4==4.9.3",
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "idna==2.10",
        "requests==2.25.1",
        "soupsieve==2.1",
        "urllib3==1.26.2"],
    python_requires=">=3.9"
)