from setuptools import setup, find_packages

with open('README.md', encoding='UTF8') as f:
    readme = f.read()

setup(
    name='bra2txt',
    version='0.1.0',
    description='Converter for print-braille text to plain txt',
    long_description=readme,
    author='Juan D. Cabrerizo',
    url="https://github.com/jcabrerizo/bra2txt",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'bra2txt=bra2txt.cli:main'
        ]
    }
)