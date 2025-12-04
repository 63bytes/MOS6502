import csv
from math import ceil
import os
import json

FILE = os.path.dirname(__file__) + "\\mos.csv"
OUT_FILE = os.path.dirname(__file__) + "\\output.json"

MODES = [
    "IMM",
    "ABS",
    "ZP",
    "ACC",
    "IMP",
    "INDX",
    "INDY",
    "ZPX",
    "ABX",
    "ABY",
    "REL",
    "IND",
    "ZPY"
]

ATS = ["OP","N","#"]

ops = {}

def ins(l):
    o = {}
    name = l[0]
    l.remove(name)
    for i in range(len(l)):
        if l[i]=="":continue
        m = MODES[ceil((i+1)/3)-1]
        a = ATS[i%3]
        if a=="OP":
            if not o.get(m):o[m]={}
            o[m][a] = int(l[i],16)
        else:
            if not o.get(m):o[m]={}
            o[m][a] = int(l[i])
    return o,name


ops = {}
f = open(FILE,"r")
csvFile = csv.reader(f)
for lines in csvFile:
    r = ins(lines)
    ops[r[1]] = r[0]

with open(OUT_FILE,"w") as f:
    json.dump(ops,f)