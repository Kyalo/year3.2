#---------------------------
#	MAIN SCANNER
#---------------------------

###########################
#	IMPORTS
###########################

import basic_parser

while True:
	text = input('basic scanner> ')
	if text.strip() == "": continue

	if 'RUN' in text:
		fn = text.strip("(\"\")RUN")
		result, error = basic_parser.execute_run(fn)
	else:
		result, error = basic_parser.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		print(repr(result))