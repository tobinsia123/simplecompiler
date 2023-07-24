from lex import *
from emit import *
from parse import *
import sys

def main():
    print("simple compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        source = inputFile.read()

    # Initialise
    lexer = Lexer(source)
    emitter = Emitter("out.c")
    parser = Parser(lexer, emitter)

    parser.program() # Start the parser
    emitter.writeFile() # C code file
    print("Compiling completed.")

main()
