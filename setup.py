import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jadg",
    version="0.0.2",
    author="Ruben Lipperts, Georg Alberding",
    author_email="",
    description="Drinking game service focused on usability and extensibility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rlipperts/justanotherdrinkinggame",
    packages=setuptools.find_packages(include='jadg', exclude=("test*", "doc*")),
    install_requires = [
        'logging-configurator @ git+ssh://git@github.com/rlipperts/logger.git@master#egg=logging-configurator-0.0.2',
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment",
    ],
    python_requires='~=3.9',
)
