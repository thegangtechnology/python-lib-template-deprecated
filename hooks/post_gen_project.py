from sys import platform


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def is_windows():
    return platform.startswith('win')


def is_mac():
    return platform == 'darwin'


def is_linux():
    return platform.startswith('linux')


def main():
    project_name = "{{cookiecutter.project_name}}"
    if is_windows():
        print(
            f"Project {project_name} Created\n"
            f"Recommended steps after installation\n"
            f"Create and Activate venv\n"
            f"\n"
            f"cd {project_name}\n"
            f"python -m venv venv\n"
            f".\\venv\\Scripts\\activate\n"
            f"python -m pip install -e \".[dev,test]\"\n"
            f"python -m ipykernel install --name {project_name}"
        )
    else:
        print(
            f"{BColors.BOLD}Project {project_name} Created{BColors.ENDC}\n"
            f"{BColors.HEADER}Recommended steps after installation{BColors.ENDC}\n"
            f"{BColors.HEADER}Create and Activate venv{BColors.ENDC}\n"
            f"\n"
            f"cd {project_name}\n"
            f"python3 -m venv venv\n"
            f"source venv/bin/activate\n"
            f"python -m pip install -e \".[dev,test]\"\n"
            f"python -m ipykernel install --name {project_name}"
        )

main()
