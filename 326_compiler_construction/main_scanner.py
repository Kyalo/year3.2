#---------------------------
#	MAIN SCANNER
#---------------------------

###########################
#	IMPORTS
###########################

import basic_scanner

while True:
	text = input('basic scanner> ')
	if text.strip() == "": continue

	if 'RUN' in text:
		fn = text.strip("(\"\")RUN")
		result, error = basic_scanner.execute_run(fn)
	else:
		result, error = basic_scanner.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		print(repr(result))