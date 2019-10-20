from setuptools import find_packages, setup
import subprocess
subprocess.call(["pip", "install", "-r", "requirements.txt"])

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
)

