
import re

repile = re.compile('(?P<host_name>.*) - (?P<user_name>[\w]*|-) \[(?P<time>.*)\] "(?P<request>.*)"')


def logs():
    with open("logdata.txt", "r") as pf:
        logdata = pf.read()

    matches = repile.findall(logdata)

    results = []
    for m in matches:
        mdict = {
            'hostname': m[0],
            'user_name': m[1],
            'date': m[2],
            'request': m[3]
        }
        results.append(mdict)

    return results

for x in logs():
    print(x)
