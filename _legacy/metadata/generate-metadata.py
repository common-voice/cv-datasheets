#!/usr/bin/python3

import sys, glob, re, json, math

#modality	code	native_name	english_name	speakers	hours_recorded	hours_validated

translated_native_names = {}

for fn in glob.glob('translations/*.ftl'):
	locale = fn.split('/')[1].split('.')[0]
	translated_native_names[locale] = '_'
	with open(fn) as fd:
		for line in fd:
			if re.match('^'+locale+' ', line):
				translated_native_names[locale] = line.split('=')[1].strip()

	#print(locale, native_names[locale])

translated_english_names = {}
in_block = False
with open('translations/en.ftl') as fd:
	for line in fd:
		if line.count('# [Languages]') > 0:
			in_block = True	
		if line.count('# [/]') > 0:
			in_block = False
	
		if in_block and line.strip() and line[0] != '#':
			k, v = [x.strip() for x in line.split('=')]
			translated_english_names[k] = v
	

#{"id":1,"is_contributable":1,"localizedPercentage":0,"recordedHours":3746,"validatedHours":2682,"invalidatedHours":448,"speakersCount":98579,"sentencesCount":{"targetSentenceCount":5000,"currentCount":1603937},"locale":"en","lastFetched":"2025-08-26T06:56:53.956Z"}

statistics_scs = {}
stats = json.loads(open('scs/statistics.json').read())
for stat in stats:
	#print(stat)
	#statistics_scs[locale] = [-1,-1,-1]
	locale = stat['locale']
	speakers = stat['speakersCount']
	hours_recorded = stat['recordedHours']
	hours_validated = stat['validatedHours']
	statistics_scs[locale] = [speakers, hours_recorded, hours_validated]
	
#{"statistics":[{"language":"Adyghe (West Circassian)","code":"ady","num_of_speakers":22,"hours_of_validated_recordings":"5.078580000000","num_of_validated_transcriptions":741}
#{"language":"English","code":"en","num_of_speakers":148,"total_recorded_hours":"8.313310000000","num_of_audios":1820}
statistics_sps = {}
audio_stats = json.loads(open('sps/audios.json').read())
valid_stats = json.loads(open('sps/validated-transcriptions.json').read())
for stat in audio_stats['statistics']:
	locale = stat['code']
	if locale not in statistics_sps:
		statistics_sps[locale] = [0,0,0]
	statistics_sps[locale][0] = int(stat['num_of_speakers'])
	statistics_sps[locale][1] = math.ceil(float(stat['total_recorded_hours']))
for stat in valid_stats['statistics']:
	locale = stat['code']
	if locale not in statistics_sps:
		statistics_sps[locale] = [0,0,0]
	statistics_sps[locale][2] = math.ceil(float(stat['hours_of_validated_recordings']))

enabled = {}

for fn in glob.glob('*/enabled.tsv'):
	modality = fn.split('/')[0]
	enabled[modality] = {}
	with open(fn) as fd:
		for line in fd:
			locale, native_name, english_name = line.strip().split('\t')
			if native_name == '_' and locale in translated_native_names:
				native_name = translated_native_names[locale]
			if english_name == '_' and locale in translated_english_names:
				english_name = translated_english_names[locale]
			enabled[modality][locale] = [native_name, english_name]

print('modality\tcode\tnative_name\tenglish_name\tspeakers\thours_recorded\thours_validated')
for modality in enabled:
	for locale in enabled[modality]:
		if modality == 'sps' and statistics_sps[locale][0] > 0:
			print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % tuple([modality, locale, enabled[modality][locale][0], enabled[modality][locale][1]] + statistics_sps[locale]))
		elif modality == 'scs' and statistics_scs[locale][0] > 0:
			print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % tuple([modality, locale, enabled[modality][locale][0], enabled[modality][locale][1]] + statistics_scs[locale]))
		else:
			print(locale)
			pass
