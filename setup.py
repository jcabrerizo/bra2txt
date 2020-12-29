from setuptools import setup, find_packages

with open('README.md', encoding='UTF8') as f:
    readme = f.read()

setup(
    name='bra2txt',
    version='0.1.0',
    description='Converter for print-braille text to plain txt',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Juan D. Cabrerizo',
    url="https://github.com/jcabrerizo/bra2txt",
    packages=['bra2txt'],
    entry_points={
        'console_scripts': [
            'bra2txt=bra2txt.cli:main'
        ]
    }
)