from distutils.core import setup

setup(
    # Application name:
    name="Atom Counter",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="Taha",

    # Packages
    packages=["app"],

    # Include additional files into the package
    include_package_data=True,
    description="First project for Ad Scientam",


    # Dependent packages (distributions)
    install_requires=[
        "re"
    ],
)