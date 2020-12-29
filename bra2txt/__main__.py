from os.path import splitext, basename
from bra2txt import cli

def get_default_output_name(content):
    filename = splitext(basename(content))
    return f"{filename[0]}.txt"

def main():
    from bra2txt import storage, converter

    args = cli.create_parser().parse_args()
    content = storage.getContent(args.source)
    content = converter.convert(content);
    if not args.dry_run:
        dest = args.dest
        if dest == "":
            dest = get_default_output_name(args.source)
        storage.saveFile(content,dest)

    if args.screen:
        print(content)

if __name__ == "__main__":
    main()