from setuptools import setup, find_packages

with open('README.md', encoding='UTF8') as f:
    readme = f.read()

setup(
    name='bra2txt',
    version='0.1.0',
    decription='Converter for print-braille text to plain txt',
    long_description=readme,
    autor='Juan D. Cabrerizo',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
