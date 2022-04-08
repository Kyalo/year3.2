#---------------------------
#	MAIN SCANNER
#---------------------------

###########################
#	IMPORTS
###########################

import run_scanner
import run_parser

while True:
	text = input('basic> ')
	result, error = run_parser.run('<stdin>', text)

	if error: print(error.as_string())
	else: print(result)