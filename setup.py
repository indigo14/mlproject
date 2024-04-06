from setuptools import find_packages, setup
from typing import List

'''
-e or --editable is an option that installs the package in "editable" mode.
. (dot) refers to the current directory, implying that the package to be installed in editable mode is located in the current directory.
Editable mode achieves this by essentially linking the installed package in your site-packages directory back to your project directory. It means that when Python tries to import the package, it's directly accessing the project files, rather than copies of them installed somewhere in your Python environment. 
'''
HYPHEN_E_DOT = '-e .'
# function 'get_requirements' reads a file specified by file_path,  
#and returns a list of strings derived from the file's contents.
def get_requirements(file_path: str) -> List[str]:#The arrow -> in Python function definitions is used for type hinting, not enforced at runtime
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] #each list item in requirements.txt will have a \n after the item

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)# remove -e . from requirements.txt because it will automatically get connected to setup.py

    return requirements

#many parameters are available
setup(
    name='mlprojects',
    version='0.1',
    author='Michael',
    author_email='michaelyardley7@gmail.com',
    packages=find_packages(),
    # install_requires=[
    #     'numpy',
    #     'pandas',
    #     'scikit-learn',
    #     'matplotlib',
    #     'seaborn',
    #     'jupyter',
    #]Normally list packages here. But instead will create function to read
    #requirements.txt
    install_requires=get_requirements('requirements.txt')
)
