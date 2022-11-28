from os import system, name
from sys import argv

def install_requirements(needed_requirements:list):
    if name == "nt":
        for requirement in needed_requirements:
            system(f"py -m pip install {requirement}")
    else:
        for requirement in needed_requirements:
            system(f"python3 -m pip install {requirement}")

if __name__ == "__main__":
    install_requirements(argv[1])