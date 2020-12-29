import pytest
import re
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from bra2txt.converter import Converter

def test_special_characters():
    """
    Replaces 1:1 caracter conversion
    """
    converter = Converter()
    output = converter._replace_one2one_characters('7($/0)2|<')
    assert output == 'ñáéíóú()"'

def test_replace_numbers():
    """
    The first 10 leter characters after a number symbol are transformed to numers
    """
    converter = Converter()
    output = converter._replace_numbers(re.match(r'#(\w*)', '#abcdefghijaaa'))
    assert output == '1234567890111'

def test_to_upper():
    """
    Letters after the caopital simbol are tranformed to upper case
    """
    converter = Converter()
    output = converter._to_upper(re.match(r'{(.)', '{ab'))
    assert output == 'A'

def test_basic_converter():
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens
    """
    converter = Converter()
    output = converter.convert('<{basic test< 2#abcdefghijaaa| break-\nline')
    assert output == '"Basic test" (1234567890111) breakline'

def test_converter():
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens. Multiline read from local file
    """
    with open('tests/test_source.bra') as f:
        source = f.read()
    with open('tests/test_dest.txt') as f:
        dest = f.read()
    converter = Converter()        
    output = converter.convert(source)
    assert output == dest