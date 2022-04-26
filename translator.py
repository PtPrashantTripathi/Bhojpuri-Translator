# Import Modules
from englisttohindi import EngtoHindi
import json

# read dictionary file
with open('dictionary/bho-hin.json', 'r') as myfile:
	data=myfile.read()

# parse bhojpuri words from file
bhojpuri = json.loads(data)

def translator(txt):
	res = EngtoHindi(txt)
	if res in bhojpuri:
		return bhojpuri[res]
	else:
		arr = res.split()
		translated = ""
		for a in arr:
			if a in bhojpuri:
				translated = ' '.join([translated, bhojpuri[a]])
			else:
				translated = ' '.join([translated, a])
		return translated.strip()

if __name__ == '__main__':
	print(translator(input()))
