import json
import re


def parserf(file_path):

    with open(file_path, 'r') as file:
        text = file.read()
        prog = re.compile(r'<custom_item>(.*?)</custom_item>', re.DOTALL)
        # result = prog.findall(text.replace(" ", ""))
        result = prog.findall(text)

    final = dict()
    for i in result:
        i = re.sub(r'(\s*):\s*', ':', i)
        i = re.sub(r'"', '', i)

        foo = dict(re.findall(r'(?:(?<=\s)|(?<=^))(\S+?):(.*?)(?=\s[^\s:]+:|$)', i, re.MULTILINE))
        final[foo['description']] = dict()
        for ii in foo.keys():
            if ii != 'description':
                final[foo['description']][ii] = foo[ii]

    return json.dumps(final, sort_keys=True, indent=4)


# a = parserf('C:/Users/Flipp/Desktop/MSCT_Windows_Server_2004_MS_v1.0.0.audit')
# print(a)
# print(json.dumps(final))
# print(len(final))
