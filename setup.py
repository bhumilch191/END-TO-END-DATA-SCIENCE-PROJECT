"""setup.py file used for packaging the project.
It includes metadata about the package such as name, version, author, and requirements.
It also includes a function to read the requirements from a file and return them as a list.
This file is used to create a package that can be installed using pip."""

from setuptools import setup, find_packages

def read_requirements(file_path:str)->list[str]:
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
        
        return requirements

setup(
    name="customer_churn_prediction",
    version="0.1.0",
    author="bhumil chauhan",
    author_email="bhumilchauhan1914@gmail.com",
    description="Predict customer churn or not on bank dataset.",
    packages=find_packages(),
    include_dirs=read_requirements("requirements.txt"),
)
