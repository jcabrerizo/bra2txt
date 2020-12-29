import pytest
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from bra2txt.cliParser import CliParser

source = 'source.bra'

@pytest.fixture
def parser():
    return CliParser().create_parser()

def test_parser_without_source(parser):
    """
    Without source file the converter will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args()

def test_parser_with_source(parser):
    """
    With source file the converter won't exit
    """
    args = parser.parse_args([source])
    assert args.source == source

def test_parser_default_arguments(parser):
    """
    With source file and not overwriten arguments applies the defaul values
    """
    args = parser.parse_args([source])
    assert args.dest == ''
    assert args.dry_run == False
    assert args.screen == False