# logic_grammar.py
from logic_lexer import LogicLexer
import ply.yacc as pyacc


class LogicGrammar:

    # !Error comment
    # *Info comment
    # ?Warn comment

    # tokens = LogicLexer.tokens  # calling tokens from Lexer

    # constructor
    def __init__(self):
        self.yacc = None
        self.lexer = None
        self.tokens = None

    def build(self, **kwargs):
        self.lexer = LogicLexer()
        self.lexer.build(**kwargs)
        self.tokens = self.lexer.tokens
        self.yacc = pyacc.yacc(module=self, **kwargs)

    def parse(self, string):
        self.lexer.input(string)
        return self.yacc.parse(lexer=self.lexer.lexer)

    # Axiom A
    def p_A(self, p):
        # A -> procedurecommand | multicommand
        """ A : procedurecommand
              | multicommand """
        p[0] = p[1]
        # A  : procedurecommand
        # A  : multicommand
        # print(p[0])

    # Creating procedure so it can recognize a procedure with commands inside
    def p_procedure(self, p):
        # procedurecommand -> function VAR staticnames multicommand staticnames ;
        """ procedurecommand : PROCEDURE VAR DO multicommand END ';'"""
        p[0] = {"procedure_name": p[2], "args": {"Commands": p[4], "function": p[1]}}
        # print(p[0])

    # Creating multicommand so it can recognize a single command or multiple ones
    def p_multicommand(self, p):
        # multicommand -> command | multicommand command
        """ multicommand : command
                         | multicommand command"""  # recursion
        # if there is a single command p[0] = single command
        if len(p) == 2:
            p[0] = p[1]
        # if anything else occurs p[0] = command , multicommand
        else:
            p[0] = p[1], p[2]
        # print(p[0])

    # Recognition of a single command
    def p_command(self, p):
        # command ->  commandcreate ; |  commandalter ; |....
        """ command : commandcreate ';'
                    | commandshow ';'
                    | commandalter ';'
                    | commandcomment ';'
                    | commandsave ';'
                    | commandselect ';'
                    | commanddrop ';'
                    | commandload ';'"""
        p[0] = p[1]  # command = function command...
        # print(p[0])

    def p_load(self, p):
        """ commandload : LOAD TABLE VAR FROM csvfile"""
        p[0] = {"function": p[1], "args": {"Table": p[3], "csv": p[5]}}

    # Syntax accepted after a function CREATE
    def p_commandcreate(self, p):
        # commandcreate -> staticnames VAR (argument)
        # commandcreate -> staticnames VAR staticnames (argument2)
        """ commandcreate : CREATE TABLE VAR '(' argument ')'
                          | CREATE TABLE VAR"""
        if len(p) == 4:
            p[0] = {"function": p[1], "args": {"Table": p[3], "Argument": []}}
        else:
            p[0] = {"function": p[1], "args": {"Table": p[3], "Argument": p[5]}}

    # Syntax accepted after a function DROP or SHOW
    def p_commandshow(self, p):
        """ commandshow : SHOW TABLE VAR """ # *WORKS
        p[0] = {"function": p[1], "args": {"Table": p[3]}}
        # print(p[0])

    def p_commanddrop(self, p):
        """ commanddrop : DROP TABLE VAR""" # *WORKS
        p[0] = {"function": p[1], "args": {"Table": p[3]}}

    # Syntax accepted after a function ALTER
    def p_commandalter(self, p): # *WORKS
        # commandalter -> staticnames VAR staticnames (argument)
        """ commandalter : ALTER TABLE VAR ADD COLUMN VAR
                         | ALTER TABLE VAR DROP COLUMN VAR"""
        p[0] = {"function": p[1], "args": {"Table": p[3], "WHAT": p[4], "newcolumn": p[6]}}  # commandalter = staticnames VAR staticnames argument
        # print(p[0])

    # Syntax accepted after a function COMMENT
    def p_commandcomment(self, p): # *WORKS
        # commandcomment -> staticnames staticnames VAR staticnames comment
        """ commandcomment : COMMENT ON TABLE VAR IS comment """
        p[0] = {"function": p[1], "args": {"Table": p[4], "comment": p[6]}}
        # print(p[0])

    # Syntax accepted after a function SAVE
    def p_commandsave(self, p): # *WORKS
        # commandsave -> staticnames VAR staticnames COMMASTRING
        """ commandsave : SAVE TABLE VAR AS csvfile """
        p[0] = {"function": p[1], "args": {"Table": p[3], "New_name": p[5]}}
        # print(p[0])

    # Syntax accepted after a function SELECT
    def p_commandselect(self, p):
        # commandselect -> * staticnames VAR
        """ commandselect : SELECT VAR FROM VAR
                          | SELECT VAR FROM VAR wherecomparison"""
        if len(p) == 5:
            p[0] = {"function": p[1], "args": {"Column": p[2], "Table": p[4]}}
        else:
            p[0] = {"function": p[1], "args": {"Column": p[2], "Table": p[4], "Comparison": p[5]}}  # commandselect : * staticnames VAR
        # print(p[0])

    # Syntax accepted in argument
    def p_argument(self, p):
        # argument -> eps | subargument | argument, subargument
        """ argument : subargument
                     |                          
                     | argument ',' subargument"""  # recursion
        # if argument : eps
        if len(p) == 1:
            p[0] = []
        # if argument : subargument
        if len(p) == 2:
            p[0] = p[1]  # argument : subargument
        else:
            p[0] = p[1], p[3]
            #p[0].append(p[3])
            # !unhashable type 'dict'

    # Syntax accepted in subargument
    def p_subargument(self, p):
        # subargument -> VAR VAR (NUMBER)
        """ subargument : VAR VAR '(' NUMBER ')' """
        #p[0] = {"Var": p[1], "Type": p[2], "Range": p[4]}
        p[0] = {p[1]}
        # subargument : VAR VAR NUMBER
        # print(p[0])

    # Syntax accepted in comment
    def p_comment(self, p):
        # comment -> COMMASTRING
        """ comment :  COMMASTRING """
        p[0] = p[1]
        # comment : COMMASTRING
        # print(p[0])

    def p_wherecomparison(self, p):
        """ wherecomparison : WHERE COMPARISON
                            | WHERE COMPARISON ORAND COMPARISON
                            | """
        if len(p) == 0:
            p[0] = []
        if len(p) == 3:
            p[0] = {"Comparison": p[2]}
        else:
            p[0] = {"Comparison": p[2], "Bool": p[3], "Second Comparison": p[4]}

    def p_COMPARISON(self, p):
        """ COMPARISON : VAR '>' NUMBER
                       | VAR '<' NUMBER
                       | VAR DIFFERENT NUMBER
                       | VAR GREATEREQUALTHAN NUMBER
                       | VAR LESSEQUALTHAN NUMBER"""
        p[0] ={"VAR": p[1], "Comparison": p[2], "Value": p[3]}

    def p_ORAND(self, p):
        """ ORAND : OR
                  | AND"""
        p[0] = p[1]

    # Function to pop error when there is a syntax error or unexpected end of file
    def p_error(self, p):
        if p:
            raise Exception(f"Syntax error: unexpected '{p.type}'")
        else:
            raise Exception("Syntax error: unexpected end of file")
