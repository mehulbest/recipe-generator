from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = "_e ."
def get_requirements(file_path : str)->List[str]:
    '''
    This function return list of packages that need to be installed
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
        return requirements
    



setup(
    name = 'RestaurantNameGenerator',
    version = '0.0.1',
    author = "Swarnim Dixit",
    author_email= "dixitswarnim1@gmail.com",
    packages= find_packages(),
    install_requires = get_requirements("requirements.txt")

)