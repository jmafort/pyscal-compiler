import os

from ast_nodes import Node
from compiler.lexical_analyzer import LexicalAnalyzer
from compiler.syntactic_analyzer import SyntacticAnalyzer


lex = LexicalAnalyzer()
lex.build()

yacc = SyntacticAnalyzer()
yacc.build()

directory = 'pyscal-programs'
cool_program_file_list = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.pys')]

for cool_program_file in cool_program_file_list:
    with open(cool_program_file, 'r') as cool_program:
        print(f"----{cool_program.name}----\n")
        root: Node = yacc.parse(cool_program.read(), tracking=True)
        root.print_tree()
