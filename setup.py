from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="plotapi",
    version="6.2.0",
    description="Engaging visualisations, made easy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://plotapi.com",
    author="Dr. Shahin Rostami",
    author_email="hello@plotapi.com",
    license="MIT",
    packages=["plotapi"],
    install_requires=["requests >=2.20.0, <3.0.0"],
    zip_safe=False,
)
