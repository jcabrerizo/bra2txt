from os.path import splitext, basename
from cli_parser import CliParser
from storage_manager import StorageManager
from converter import Converter

def get_default_output_name(content):
    filename = splitext(basename(content))
    return f"{filename[0]}.txt"

def main():
    args = CliParser().create_parser().parse_args()
    storage_manager = StorageManager()
    content = storage_manager.getContent(args.source)
    content = Converter().convert(content)
    if not args.dry_run:
        dest = args.dest
        if dest == "":
            dest = get_default_output_name(args.source)
        storage_manager.saveFile(content,dest)

    if args.screen:
        print(content)

if __name__ == "__main__":
    main()