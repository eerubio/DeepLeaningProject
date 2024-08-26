from setuptools import find_packages, setup


REQUIREMENT_FILE_NAME = "requirements.txt"
HYPER_E_DOT = "-e ."

def get_requirements(file_path: str = REQUIREMENT_FILE_NAME) -> list:
    try:
        requirements = []
        with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements=[req.replace("\n", "")] for req in requirements

            if HYPER_E_DOT in requirements:
                requirements.remove(HYPER_E_DOT)
        return requirements
    except Exception as e:
        raise e


setup(
    name="XRay",
    version="0.0.1",
    author="Ernesto Enriquez",
    author_email="imt.ernestoer@gmail.com",
    install_requires=get_requirements(),
    package=find_packages()
)