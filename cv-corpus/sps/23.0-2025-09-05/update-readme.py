import sys, glob

draft_files = glob.glob('draft/en/*.md') + glob.glob('draft/es/*.md') + glob.glob('draft/zh-TW/*.md')
final_files = glob.glob('final/en/*.md') + glob.glob('final/es/*.md') + glob.glob('final/zh-TW/*.md')
draft_codes = list(set([f.split('/')[-1].split('.')[0] for f in draft_files]))
final_codes = list(set([f.split('/')[-1].split('.')[0] for f in final_files]))

draft_codes.sort()
final_codes.sort()

print('# Datasheets')
print()
print('## Status')
print()

total_count = 0
final_count = 0
status = []

status.append('| Draft | Final |')
status.append('|-------|-------|')
for code in draft_codes:
	res = '-'
	if code in final_codes:
		res = '✔'
		final_count += 1
	status.append('| `%s` | %s |' % (code, res))
	total_count += 1

print(final_count, '/', total_count)
print()
print('\n'.join(status))
