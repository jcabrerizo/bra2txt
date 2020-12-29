from argparse import ArgumentParser

class CliParser:
    def create_parser(self):
        parser = ArgumentParser()

        parser.add_argument("source",
                            help="Source file"
                            )
        parser.add_argument("-d", "--dest",
                            help="Destiny filename",
                            default=""
                            )
        parser.add_argument("-s", "--screen",
                            help="Show converted text on the screen",
                            action="store_true"
                            )
        parser.add_argument("--dry-run",
                            help="Do no save the converted text to a file",
                            action="store_true"
                            )

        return parser