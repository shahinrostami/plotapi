from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="plotapi",
    version="6.0.1",
    description="Engaging visualisations, made easy.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://plotapi.com",
    author="Dr. Shahin Rostami",
    author_email="hello@plotapi.com",
    license="MIT",
    packages=["plotapi"],
    zip_safe=False,
)
