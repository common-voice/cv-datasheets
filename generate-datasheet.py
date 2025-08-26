import sys, re, json

metadata_file = sys.argv[1] 
languages_file = sys.argv[2]
version = sys.argv[3]
output_dir = sys.argv[4]

template_languages = {'scs':{},'sps':{}}
first = True
for line in open(languages_file):
	if first:
		first = False
		continue
	modality, locale, template_language = line.strip().split('\t')
	template_languages[modality][locale] = template_language

#metadata = json.loads(open(metadata_file).read())
#modality	code	native_name	english_name	speakers	hours_recorded	hours_validated
metadata = {'scs':{},'sps':{}}
first = True
for line in open(metadata_file):
	if first:
		first = False
		continue
	row = line.strip().split('\t')
	print(row)
	modality, locale, native_name, english_name, speakers, hours_recorded, hours_validated = row
	if locale not in metadata[modality]:
		metadata[modality][locale] = {}
	metadata[modality][locale]['english_name'] = english_name
	metadata[modality][locale]['native_name'] = native_name 
	metadata[modality][locale]['speakers'] = speakers 
	metadata[modality][locale]['hours_recorded'] = hours_recorded 
	metadata[modality][locale]['hours_validated'] = hours_validated 
	
for modality in metadata:
	for locale in metadata[modality]:
		draft_output_dir = output_dir + '/%s/%s/draft/%s' % (modality, version, template_languages[modality][locale])
		template = open('templates/%s/%s.md' % (modality, template_languages[modality][locale])).read()
		print(locale, metadata[modality][locale])
		english_name = metadata[modality][locale]['english_name']
		native_name = metadata[modality][locale]['native_name']
		version_readable = version.split('-')[0]
		if native_name == '':
			native_name = '<' + english_name + '>'
		filled_template = template.replace('{{LOCALE}}', locale)
		filled_template = filled_template.replace('{{VERSION}}', version_readable)
		filled_template = filled_template.replace('{{ENGLISH_NAME}}', english_name)
		filled_template = filled_template.replace('{{NATIVE_NAME}}', native_name)
		filled_template = filled_template.replace('{{SPEAKERS}}', metadata[modality][locale]['speakers'])
		filled_template = filled_template.replace('{{HOURS_RECORDED}}', metadata[modality][locale]['hours_recorded'])
		filled_template = filled_template.replace('{{HOURS_VALIDATED}}', metadata[modality][locale]['hours_validated'])
	
		output_fd = open(draft_output_dir + '/' + locale + '.md', 'w+')
		print(filled_template, file=output_fd)
		output_fd.close()
