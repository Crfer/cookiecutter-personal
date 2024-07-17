import re
import sys
import os

def validate_project_name(project_name):
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]+$', project_name):
        print(f"ERROR: El nombre del proyecto ({project_name}) es inválido. Debe comenzar con una letra y solo puede contener letras, números, guiones y guiones bajos.")
        sys.exit(1)


def main():
    project_name = '{{ cookiecutter.project_name }}'
    validate_project_name(project_name)

if __name__ == '__main__':
    main()