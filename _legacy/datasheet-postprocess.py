# It would be nice to do this with a markdown parser, e.g. get an AST
# remove nodes and then render it, but I haven't found a library that
# does Markdown -> AST yet.

import sys, re
datasheet = open(sys.argv[1]).read()


# Split the Markdown into blocks by section
lines = datasheet.split('\n')
new_lines = []
for line in lines:
	line = re.sub('^(#+)', r'◊\g<1>', line)
	new_lines.append(line)
lines = '\n'.join(new_lines)
blocs = lines.split('◊')

empty_sections = [] # A list of the empty sections

# Print out non-empty sections
for bloc in blocs:
	empty = False
	if '{{' in bloc:
		empty = True
	if re.sub('^#+.*', '', bloc).strip() == '':
		empty = True
	if empty:
		empty_sections.append(bloc)
	else:
		print(bloc)

print(len(empty_sections), file=sys.stderr)
