import pytest
import tempfile
import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from bra2txt.storageManager import StorageManager


def test_read_file():
    """
    Reads the content of a file
    """
    infile = tempfile.TemporaryFile('r+t')
    infile.write("bra2txt")
    infile.seek(0)
    content = StorageManager().getContent(infile.name)
    assert content == 'bra2txt'

def test_trying_to_read_non_existing_file():
    """
    Fails tryint to open a non existing file
    """
    with pytest.raises(SystemExit) as pytest_wrapped_error:
        StorageManager().getContent("non_existing")

def test_write_file():
    """
    Writes the content of a file
    """
    outfile = tempfile.NamedTemporaryFile(delete=False)
    StorageManager().saveFile("bra2txt",outfile.name)
    with open(outfile.name, 'r') as f:
        assert f.read() == "bra2txt"