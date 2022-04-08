###########################
#	IMPORTS
###########################

import basic_scanner

###########################
#	RUN
###########################

def run(fn, text):
	# Generate tokens
	lexer = basic_scanner.Lexer(fn, text)
	tokens, error = lexer.make_tokens()

	return tokens, error

