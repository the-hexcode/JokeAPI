import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jokeapi",
    packages=["jokeapi"],
    version="0.2.5",
    license="GNU General Public License v3 (GPLv3)",
    description="An API Wrapper for Sv443's JokeAPI [Unofficial]",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="1Prototype1",
    author_email="astonlopes1999@gmail.com",
    url="""https://github.com/1Prototype1/Sv443s-JokeAPI-Python-Wrapper/""",
    keywords=["api wrapper", "wrapper", "api", "jokes", "python", "joke api"],
    install_requires=[
        "urllib3==1.25.8",
        "simplejson==3.17.0",
        "python-dotenv==0.13.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.8",
    ],
)