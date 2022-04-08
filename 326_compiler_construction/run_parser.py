###########################
#	IMPORTS
###########################

import basic_parser
import basic_scanner

###########################
#	RUN_parser
###########################

def run(fn, text):
	lexer = basic_scanner.Lexer(fn, text)
	tokens, error = lexer.make_tokens()

	if error: return None, error

	# Generate AST
	parser = basic_parser.Parser(tokens)
	ast = parser.parse()

	return ast, None