import pytest
import re
from bra2txt import conveter

def test_special_characters():
    """
    Replaces 1:1 caracter conversion
    """
    output = conveter.replace_one2one_characters('7($/0)2|<')
    assert output == 'ñáéíóú()"'

def test_replace_numbers():
    """
    The first 10 leter characters after a number symbol are transformed to numers
    """
    output = conveter.replace_numbers(re.match(r'#(\w*)', '#abcdefghijaaa'))
    assert output == '1234567890111'

def test_to_upper():
    """
    Letters after the caopital simbol are tranformed to upper case
    """
    output = conveter.to_upper(re.match(r'{(.)', '{ab'))
    assert output == 'A'

def test_basic_converter():
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens
    """
    output = conveter.convert('<{basic test< 2#abcdefghijaaa| break-\nline')
    assert output == '"Basic test" (1234567890111) breakline'

def test_converter():
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens. Multiline
    """
    with open('tests/test_source.bra') as f:
        source = f.read()
    with open('tests/test_dest.txt') as f:
        dest = f.read()        
    output = conveter.convert(source)
    assert output == dest