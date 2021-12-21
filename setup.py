from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name = "InstaContent",
    version = "0.0.1",
    description = "Module to access Instagram functionalities",
    long_description = long_description,
    author_email = "20nischalkhatri@gmail.com",
    author= "neeschal00",
    packages=['InstaContent'],  #same as name
    setup_requires=['wheel'],
    install_requires=['aiohttp>=3.8.1', 'requests>=2.0.0','aiosignal>=1.2.0'], #external packages as dependencies
    python_requires=">=3.5",
    # package_dir={'':'InstaContent'},
    url = "https://github.com/neeschal00/instagram-assets",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    )


