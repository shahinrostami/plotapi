from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="chord",
    version="0.0.7",
    description="Python wrapper around d3-chord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shahinrostami/chord",
    author="Dr. Shahin Rostami",
    author_email="hello@shahinrostami.com",
    license="MIT",
    packages=["chord"],
    zip_safe=False,
    install_requires=["mako", "uuid"],
)
