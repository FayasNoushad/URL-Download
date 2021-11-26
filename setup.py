import os
import setuptools


def requirements(file="requirements.txt"):
    if os.path.isfile(file):
        with open(file, encoding="utf-8") as r:
            return [i.strip() for i in r]
    else:
        return []


def readme(file="README.md"):
    if os.path.isfile(file):
        with open(file, encoding="utf8") as r:
            return r.read()
    else:
        return ""


setuptools.setup(
    name="urldl",
    version="1.0.9",
    description="URL content downloader",
    long_description=readme(),
    long_description_content_type="text/markdown",
    download_url="https://github.com/FayasNoushad/URL-Download/releases/latest",
    license="MIT",
    author="Fayas Noushad",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    project_urls={
        "Tracker": "https://github.com/FayasNoushad/URL-Download/issues",
        "Source": "https://github.com/FayasNoushad/URL-Download"
    },
    python_requires=">=3.6",
    py_modules=['urldl'],
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements()
)
