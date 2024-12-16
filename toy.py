"""
Name: Toy
Author: Mohammad Najm
Date: 12/16/2024
Description: Main driver for the toyInterprer, 
and interpreter for a toy language. Lexes, Parses, analyzes, and evalautes.
This function can accept terminal input or may use a file name as command line arguement.
"""
import sys
from lexer import tokenizer
from parser import Parser
from symbol_table import SymbolTable
from semantic_analyzer import SemanticAnalyzer
from evaluator import Evaluator

def read_input():

    # If user passes input file as command line arguement.
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            return file.read()
        
    # Read from stdin until EOF (User presses Ctrl+D on Unix/ Ctrl+Z+Enter on Windows)
    else:
        return sys.stdin.read()

def main():
    input_code = read_input()

    try:
        tokens = tokenizer(input_code)
        parser = Parser(tokens)
        parse_tree = parser.parse_program()

        symbol_table = SymbolTable()
        semantic_analyzer = SemanticAnalyzer(symbol_table)
        semantic_analyzer.analyze(parse_tree)

        evaluator = Evaluator(symbol_table)
        evaluator.evaluate(parse_tree)

    except (SyntaxError, Exception) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()