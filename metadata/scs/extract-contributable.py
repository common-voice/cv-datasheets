import sys, json

metadata = {}

stats = json.loads(open(sys.argv[1]).read())

for stat in stats:
	# {'id': 13, 'name': 'ca', 'target_sentence_count': 5000, 'native_name': 'català', 'is_contributable': 1, 'is_translated': 1, 'text_direction': 'LTR'}

	if stat['is_contributable'] == 1:
		locale = stat['name']
		native_name = stat['native_name']
		if native_name == locale:
			native_name = '_'
		print('%s\t%s\t%s' % (locale, native_name, '_'))
