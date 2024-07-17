import os
import subprocess
import sys

def initialize_git():
    print("Inicializando repositorio Git...")
    subprocess.run(['git', 'init'], check=True)
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)


def create_conda_env():
    env_file = 'environment.yml'
    if os.path.exists(env_file):
        print(f"Creando entorno conda desde {env_file}...")
        subprocess.run(['conda', 'env', 'create', '--file', env_file], check=True)
        env_name = '{{ cookiecutter.project_slug }}'
    else:
        print(f"No se encontró el archivo {env_file}")
        sys.exit(1)


def main():
    initialize_git()
    create_conda_env()



if __name__ == '__main__':
    main()