import sys, json

metadata = {}

stats = json.loads(open(sys.argv[1]).read())
translation_fd = open(sys.argv[2])
english_translations = {}
in_block = False
for line in translation_fd:
	if line.count('# [Languages]') > 0:
		in_block = True	
	if line.count('# [/]') > 0:
		in_block = False

	if in_block and line.strip() and line[0] != '#':
		k, v = [x.strip() for x in line.split('=')]
		english_translations[k] = v

for stat in stats:
	# {'id': 13, 'name': 'ca', 'target_sentence_count': 5000, 'native_name': 'català', 'is_contributable': 1, 'is_translated': 1, 'text_direction': 'LTR'}

	if stat['is_contributable'] != 1:
		continue

	locale = stat['name']
	native_name = stat['native_name']

	metadata[locale] = {}
	metadata[locale]['native_name'] = ''
	if native_name != locale:
		metadata[locale]['native_name'] = native_name
	metadata[locale]['english_name'] = ''
	if locale in english_translations:
		metadata[locale]['english_name'] = english_translations[locale]

print(metadata)

metadata_fd = open('metadata.json', 'w+')		
metadata_fd.write(json.dumps(metadata))
metadata_fd.close()
