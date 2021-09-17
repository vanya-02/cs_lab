import json
import re

with open('MSCT_Windows_10_20H2_v1.0.0.audit', 'r') as file:
	text = file.read()
	prog = re.compile(r'<custom_item>(.*?)</custom_item>', re.DOTALL)
	result = prog.findall(text.replace(" ", ""))


final = dict()
for i in result:
	foo = dict(re.findall(r'(?:(?<=\s)|(?<=^))(\S+?):(.*?)(?=\s[^\s:]+:|$)', i))
	final[ foo['description'] ] = dict()
	for ii in foo.keys():
		if ii != 'description':
			final[ foo['description'] ][ii] = foo[ii]



print(json.dumps(final))

print(len(final))
