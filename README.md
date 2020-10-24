# bra2txt
File converter from braille codification to plain text

## Usage
By default it won't generate any output unless errors happen.

It only requires one parameter, the file to be converted, and it will generate the output in the current path with the same name and txt extension.
```bash
$ bra2txt source_file
```
Optionally you can overwrite that behavior with parameters
```bash
$ bra2txt -h
usage: bra2txt.py [-h] [-d DEST] [-s] [--dry-run] source

positional arguments:
  source                Source file

optional arguments:
  -h, --help            show this help message and exit
  -d DEST, --dest DEST  Destiny filename
  -s, --screen          Show converted text on the screen
  --dry-run             Do no save the converted text to a file
```

## Creating a exe file to use it on Windows
You can use [Pyinstaller](https://www.pyinstaller.org/) to generate a Windows executable file. By opening a `bra` file with this program you will get immediately the plain text in the same folder with `txt` extension
```
pyinstaller bra2txt.py --onefile
```