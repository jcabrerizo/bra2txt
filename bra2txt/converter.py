import re

class Converter:
    def __init__(self):
        pass

    def _to_upper(self, match):
        """ returns the first captured group letter in upper case"""
        return match.group(1).upper()

    def _dictionary_replacer(self, content, dictionary):
        """ replaces the entries from a dictionary to the target character """
        for ch in dictionary:
            content = content.replace(ch[0], ch[1])
        return content


    def _replace_numbers(self, match):
        """ replaces the numbers """
        number_transformation = [
            ('a','1'),
            ('b','2'),
            ('c','3'),
            ('d','4'),
            ('e','5'),
            ('f','6'),
            ('g','7'),
            ('h','8'),
            ('i','9'),
            ('j','0')  
        ]
        content = match.group(1)
        return self._dictionary_replacer(content, number_transformation)

    def _replace_one2one_characters(self, content):
        """ replaces the special characters """
        direct_transformation = [
            ('7',u'\u00f1'),    # ñ
            ('(',u'\u00e1'),    # á
            ('$',u'\u00e9'),    # é
            ('/',u'\u00ed'),    # í
            ('0',u'\u00f3'),    # ó
            (')',u'\u00fa'),    # ú
            ('<','"'),
            ('2','('),
            ('|',')')
        ]
        return self._dictionary_replacer(content, direct_transformation)

    def convert(self, content):
        # Remove maker lines
        content = re.sub(r'^ {19,}\?$','', content, flags=re.MULTILINE) # Removes print marker
        content = re.sub(r' *[:c-]{3,} *$\n?','', content, flags=re.MULTILINE) # Removes lines with sucession of ':', 'c' or '-' printed as lines 
        
        # Fix line length
        content = re.sub(r'^ {19,}#[^\n]*','', content, flags=re.MULTILINE) # Removes all lines with a number after more than 20 white spaces, for removing page numbers
        content = re.sub(r'-\n','', content) # Cut word on the end of a line
        content = re.sub(r'\n(?! {2,})',' ', content) # Removes break line character if next line doesn't start with two spaces
        content = re.sub(r' +$','', content, flags=re.MULTILINE) # Removes extra spaces at the end of lines
        content = re.sub(r'^  ','\n', content, flags=re.MULTILINE) # Replaces the two spaces at the beginning of the paragraphs for a new break line
        
        # Replace characters
        content = self._replace_one2one_characters(content)
        content = re.sub(r'{(.)', self._to_upper, content) # Upper case character after { mark
        content = re.sub(r'#(\w*)', self._replace_numbers, content) # Repace numbers after # mark
        
        return content
        