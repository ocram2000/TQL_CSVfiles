# logic_lexer.py
import ply.lex as plex
import sys
from pprint import PrettyPrinter


class LogicLexer:

    functionsintax = ("CREATE", "DROP", "SELECT", "PROCEDURE", "ALTER", "END", "SHOW", "COMMENT", "SAVE",
                      "LOAD", "TABLE", "FROM", "WHERE", "AS", "ADD", "IS", "ON", "DO", "MODIFY", "AND", "OR", "COLUMN")

    # Creating tokens for recognition
    tokens = functionsintax + ("NUMBER", "csvfile", "VAR", "COMMASTRING", "DIFFERENT", "GREATEREQUALTHAN", "LESSEQUALTHAN",)

    # Literals to recognize single characters
    literals = ['(', ')', ';', ',', '*', '>', '<', '=']

    # ignore spaces, new line and \t
    t_ignore = " \n\t"

    # constructor
    def __init__(self):
        self.lexer = None

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    # Function to recognize token COMMASTRING
    def t_COMMASTRING(self, t):
        r"""[""](\#)?[\w ._]+[""]"""
        t.value = {t.value[1:-1]}  # Eliminate commas
        return t

    # Function to recognize token NUMBER
    def t_NUMBER(self, t):
        r"""[0-9]+"""  # recognizing digits and numbers
        return t

    def t_csvfile(self, t):  # *new token
        r"""[a-zA-Z]+\.(csv)"""
        return t

    # Function to recognize token VAR
    def t_VAR(self, t):
        r"""[a-zA-Z_]+"""  # recognizing any string
        if t.value in LogicLexer.functionsintax:
            t.type = t.value
        else:
            t.type = "VAR"
        return t

    def t_DIFFERENT(self, t):  # *new token
        r"""<>"""
        return t

    def t_GREATEREQUALTHAN(self, t):  # *new token
        r""">="""
        return t

    def t_LESSEQUALTHAN(self, t):  # *new token
        r"""<="""
        return t

    # Function to pop error when an unexpected token is detected
    def t_error(self, t):
        print(f"LEX error: Unexpected token: {t.value[0]}", file=sys.stderr)
        exit(1)


