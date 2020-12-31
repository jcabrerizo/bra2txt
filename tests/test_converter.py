import pytest
import re
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from bra2txt.converter import Converter

@pytest.fixture
def converter():
    return Converter()

def test_special_characters(converter):
    """
    Replaces 1:1 caracter conversion
    """
    output = converter._replace_one2one_characters('7($/0)2|<')
    assert output == 'ñáéíóú()"'

def test_replace_numbers(converter):
    """
    The first 10 leter characters after a number symbol are transformed to numers
    """
    output = converter._replace_numbers(re.match(r'#(\w*)', '#abcdefghijaaa'))
    assert output == '1234567890111'

def test_to_upper(converter):
    """
    Letters after the caopital simbol are tranformed to upper case
    """
    output = converter._to_upper(re.match(r'{(.)', '{ab'))
    assert output == 'A'

def test_basic_converter(converter):
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens
    """
    assert converter.convert('<{basic test< 2#abcdefghijaaa| break-\nline') == '"Basic test" (1234567890111) breakline'

def test_removing_printed_lines(converter):
    """
    Removal of makers for printing lines
    """
    assert converter.convert('ccccccc') == ''
    assert converter.convert(' -----') == ''
    assert converter.convert('   :::') == ''
    assert converter.convert('ccccccc\n') == ''
    assert converter.convert(' ccccccc \n') == ''
    assert converter.convert('    ----- ') == ''
    # Should not be removed
    assert converter.convert('cc') == 'cc'
    assert converter.convert(':') == ':'
    assert converter.convert(' - ') == ' -'
    assert converter.convert('c ') == 'c'

def test_converter(converter):
    """
    Converts numbers, capital letters, double quotes and parenthesis. Removes end of line hyphens. Multiline read from local file
    """
    with open('tests/test_source.bra') as f:
        source = f.read()
    with open('tests/test_dest.txt') as f:
        dest = f.read()
    output = converter.convert(source)
    assert output == dest