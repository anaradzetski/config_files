import os
import shutil
import importlib
import subprocess

SRC = os.path.join(os.path.dirname(__file__), "src")


def install_requirements(module):
    subprocess.run("sudo apt-get install".split() + module.REQUIREMENTS)

    
def copy_conf_files(module):
    module_dir = os.path.dirname(module.__file__)
    for src, dst in module.CONF_FILES.items():
        shutil.copy(os.path.join(os.path.dirname(module.__file__), src), dst)


def main():
    for pkg in os.listdir(SRC):
        if pkg.startswith("__"): 
            continue
        cur_module = importlib.import_module(f"src.{pkg}.config")
        install_requirements(cur_module)
        copy_conf_files(cur_module)


if __name__ == "__main__":
    main()

