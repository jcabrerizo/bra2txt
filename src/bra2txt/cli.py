from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser()

    parser.add_argument("source",
                        help="Source file"
                        )
    parser.add_argument("-d", "--dest",
                        help="Destiny filename",
                        default=""
                        )
    parser.add_argument("-s", "--screen",
                        help="Mostrar en pantalla el texto convertido",
                        action="store_true"
                        )
    parser.add_argument("--dry-run",
                        help="Omitir creacion de fichero de destino",
                        action="store_true"
                        )

    return parser