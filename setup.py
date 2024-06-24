from setuptools import find_packages,setup 


def get_requirements(file_path:str)->list[str]:
    '''this function are the return the List of requirments'''
  
  
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        
        requirements = [req.replace('\n',"") for req in requirements]
    return requirements
setup(
    
    name = 'Job eligibilty classifier Project',
    version = '0.0.1',
    auther = 'rajkamal',
    auther_email = 'rv006090@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirement.txt')
)