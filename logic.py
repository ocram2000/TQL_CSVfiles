# logic.py
from logic_lexer import LogicLexer
from pprint import PrettyPrinter
from logic_grammar import LogicGrammar
from logic_eval import Logic_eval
import sys

pp = PrettyPrinter()
lexer = LogicLexer()
lg = LogicGrammar()
lg.build()

if len(sys.argv) == 2:
    with open(sys.argv[1], "r") as file:
        contents = file.read()
        try:
            tree = lg.parse(contents)
            if tree is not None:
                print(tree)
        except Exception as exception:
            print(exception)
else:
    for expr in iter(lambda: input(">> "), ""):
        try:
            ans = lg.parse(expr)
            pp.pprint(ans)
            answer = Logic_eval.evaluate(ans)
            if answer is not None:
                print(f"<< {answer}")
        except Exception as e:
            print(e)
