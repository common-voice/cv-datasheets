import sys, json

metadata = {}

stats = json.loads(open(sys.argv[1]).read())

for stat in stats['statistics']:
	# {'id': 13, 'name': 'ca', 'target_sentence_count': 5000, 'native_name': 'català', 'is_contributable': 1, 'is_translated': 1, 'text_direction': 'LTR'}

		locale = stat['code']
		english_name = stat['language']
		if english_name == locale:
			english_name = '_'
		print('%s\t%s\t%s' % (locale, '_', english_name))
