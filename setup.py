from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="web-package-template",
    version="0.1",
    author="Azmi SAHIN",
    author_email="azmisahin@outlook.com",
    description="Project template for the development and production phases of Python packages.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/azmisahin/azmisahin-software-web-package-template-pip-python-v1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        #
    ],
)
