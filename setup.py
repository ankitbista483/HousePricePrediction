from setuptools import find_packages, setup

Hype_e_dot ='-e .'
def get_requirements(file_path:str) -> list[str]:
    requirements =[]
    with open(file_path) as f:
        f.readlines()
        requirements = [req.replace('/n',' ') for req in requirements]

        if Hype_e_dot in requirements:
            requirements.remove(Hype_e_dot)
    return requirements
setup(
    name= 'HousePricePrediction',
    version= '0.0.1',
    author= 'Ankit Bista',
    author_email= 'ankitbista1406@gmail.com',
    find_packages = find_packages(),
    install_requirements = get_requirements('requirements.txt'),
)