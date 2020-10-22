import re
import pip
import subprocess
import sys
lst=[]
searchfile = open("auto.py", "r")
for line in searchfile:
    if ("import") in line:
        line=str(line)
        m = re.search(r"(?<=import)(.*)", line)
        a=m.group()
        lst.append(a)
searchfile.close()
print(lst)
for module in lst:
    try:
        __import__(module)
    except:
        pip.main(['install', module, '--user'])
