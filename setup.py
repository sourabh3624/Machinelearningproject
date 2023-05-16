from setuptools import find_packages,setup
from typing import List

E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    
    '''
    this function will return the list of requirements
        '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements ]
        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements


setup(
name="machine learning project",
version="python 3.10",
author="Sourabh bainsla",
author_email="georbainsla.36georgian@gmail.com",
packages=find_packages(),
install_requirement=get_requirements("requirements.txt")


)