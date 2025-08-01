'''
The setup.py file is an essential part of packaging and distributing python projects.
It is used by setuptools(or distutils in older Python versions) to define the
configuration of our project, such as its metadat, dependencied, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements() ->List[str]:
    '''
    This function will return list of requirements
    '''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirement.txt file not found")

    return requirement_list

setup(
    name="NetSecurity",
    version="0.0.1",
    author="Kundan Kumar",
    author_email="kk603850@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
