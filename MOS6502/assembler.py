MODES = {
    "IMM":"#nn",
    "ABS":"$nnnn",
    "ZP":"$nn",
    "ACC":"A",
    "IMP":"",
    "INDX":"($nn,X)",
    "INDY":"($nn),Y",
    "ZPX":"$nn,X",
    "ABX":"$nnnn,X",
    "ABY":"$nnnn,Y",
    "REL":"$nn",
    "IND":"($nnnn)",
    "ZPY":"$nn,Y"
}

def cmpString(t,s,i="n"):
    if len(t)!=len(s):
        return False
    for x in range(len(s)):
        if s[x]!=t[x] and t[x]!=i:return False
    return True
def extractBytes(t,s,i="n"):
    b = ""
    for x in range(len(s)):
        if t[x]==i:b+=s[x]
    bs = []
    for i in range(0, len(s)-1, 2):
        bs.append(int(b[i:i+2],16))
    return bs

INSTRUCS = {
    "ADC":{
        "IMM":{
            "OP":0x69,
            "N":2,
            "#":2
        },
        "ABS":{
            "OP":0x6D,
            "N":4,
            "#":3
        },
        "ZP":{
            "OP":0x65,
            "N":3,
            "#":2
        },
        "INDX":{
            "OP":0x61,
            "N":6,
            "#":2,
        },
        "INDY":{
            "OP":0x71,
            "N":5,
            "#":2,
        },
        "ZPX":{
            "OP":0x75,
            "N":4,
            "#":2
        },
        "ABX":{
            "OP":0x7D,
            "N":4,
            "#":3
        },
        "ABY":{
            "OP":0x79,
            "N":4,
            "#":3
        }
    },
    "AND":{}
}

def Compiler(f, of):
    file = open(f,"r")
    tokens = []
    for l in file.readlines():
        t = l.split()
        if not t[0] in INSTRUCS:raise(Exception(f"Invalid menmonic passed({t[0]})"))
        for m in INSTRUCS[t[0]]:
            if cmpString(MODES[m],t[1]):
                tokens.append(INSTRUCS[t[0]][m]["OP"])
                for b in extractBytes(MODES[m],t[1]):tokens.append(b)
    outFile = open(of, "wb")
    for x in tokens:
        outFile.write(x.to_bytes(1))
Path = "Data\\mosasm\\assemTest.mosasm"
out = "Data\\mosasm\\assemTest.mos"
Compiler(Path,out)