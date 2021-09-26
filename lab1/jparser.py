import json
import re


def parserf(file_path):

    with open(file_path, 'r') as file:
        text = file.read()
        prog = re.compile(r'<custom_item>(.*?)</custom_item>', re.DOTALL)
        result = prog.findall(text.replace(" ", ""))

    final = dict()

    for i in result:
        foo = dict(re.findall(r'(?:(?<=\s)|(?<=^))(\S+?):(.*?)(?=\s[^\s:]+:|$)', i))
        final[foo['description']] = dict()
        for ii in foo.keys():
            if ii != 'description':
                final[foo['description']][ii] = foo[ii]

    return json.dumps(final)

#
# print(json.dumps(final))
# print(len(final))
