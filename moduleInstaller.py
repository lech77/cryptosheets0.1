import sys, subprocess

def install(package):
    reqs = subprocess.check_output([sys.executable, "-m", "pip", "freeze"])
    installed_packages = [r.decode().split("==")[0] for r in reqs.split()]
    if package in installed_packages:
        print(package + " has already been installed.")
    else:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(package + " was installed.")
    return