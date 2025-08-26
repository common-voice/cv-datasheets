import sys, glob

draft_files = glob.glob('draft/en/*.md')
final_files = glob.glob('final/en/*.md')
draft_codes = [f.split('/')[-1].split('.')[0] for f in draft_files]
final_codes = [f.split('/')[-1].split('.')[0] for f in final_files]

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
