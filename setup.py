from setuptools import setup, find_packages


def get_dependencies():
    deps = None
    with open("dependencies.txt", "r") as deps:
        deps = tuple(map(lambda dep: dep.strip(), deps.readlines()))

    return deps


setup(
    name="StackOverflow Simple Testing Framework",
    version="2.0.0",
    author="Pavlo Mryhlotskyi",
    author_email="kozak.holota@gmail.com",
    packages=find_packages(),
    install_requires=get_dependencies()
)
