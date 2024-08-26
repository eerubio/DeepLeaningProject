from setuptools import find_packages,setup

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n", "")] for req in requirements

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    
    return requirements

setup(
    name="XRay",
    version="0.0.1",
    author="Ernesto Enriquez",
    author_email="imt.ernestoer@gmail.com",
    install_requires=get_requirements("/Users/eerubio/Documents/AI/DeepLeaningProject/requirements.txt"),
    package=find_packages()
)