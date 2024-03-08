from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="web_service_template",
    version="0.0.1",
    author="Azmi SAHIN",
    author_email="azmisahin@outlook.com",
    description="It is a template to be used in automation systems of web projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/azmisahin/azmisahin-software-web-service-template-flask-python-v1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11.1",
    entry_points={
        "console_scripts": [
            "tracker = package.app:main",
            "web-service-template = web.app:app.run",
        ],
    },
    install_requires=["gunicorn", "flask", "flask-restx", "gevent", "flask-socketio"],
    extras_require={
        "development": [
            "gunicorn"
            # Add development tools here
        ],
        "test": [
            "gunicorn"
            # Add test tools here
        ],
        "production": [
            # Add production tools here
        ],
    },
)
