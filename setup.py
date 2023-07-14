from setuptools import setup, find_packages

setup(
    name="main_folder", 
    version ="0.0.1",
    author = "Pankaj",
    email = 'singh.pankaj0018@gmail.com',
    packages = find_packages(),
    install_requires= ["pandas", "numpy", "flask", "scikit-learn"]
)