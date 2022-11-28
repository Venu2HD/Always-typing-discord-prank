from pkg_resources import DistributionNotFound, VersionConflict, require

def check_requirements():
    with open("requirements.txt", "r") as requirements_file:
        requirements = requirements_file.readlines()
    needed_requirements = []
    for requirement in requirements:
        try:
            require(requirement)
        except DistributionNotFound or VersionConflict:
            needed_requirements.append(requirement)
    return needed_requirements

if __name__ == "__main__":
    check_requirements()