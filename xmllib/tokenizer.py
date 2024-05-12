import re
import xtoken as xt

opntag = r"<[a-zA-Z_][a-zA-Z0-9_]*(\s[a-zA-Z_][a-zA-Z0-9_]*=\"[a-zA-Z0-:/9_\-.\s]*\")*>"
clstag = r"</[a-zA-Z_][a-zA-Z0-9_]*>"
value = r"[a-zA-Z0-9_/\-.\s\"']+"

def split_open_tag(str1):
    name = ''
    n = len(str1)
    i = 0
    while i < n and str1[i] != " ":
        name += str1[i]
        i+=1
    attribs = []
    qoutes = 0
    kvp = ""
    while i < n:
        if str1[i] == '"':
            qoutes += 1
        if str1[i] == " " and qoutes == 0:
            i += 1
            continue
        else:
            kvp += str1[i]
            i+=1
        if qoutes == 2:
            attribs.append(kvp)
            kvp = ""
            qoutes = 0
    return [name]+attribs


def tokenize(filename):
    file = open(filename,'rt')
    str1 = ""
    ret = xt.TokenStream()
    for i in file.readlines():
        for j in i.strip():
            if j in "\t\n\r":
                continue
            else:
                if j == "<" and len(str1)>0:
                    if re.match(value,str1):
                        ret.push(xt.Token(str1,"VALUE",{}))
                        str1 = "<"
                    else:
                        raise TypeError("Invalid value : " + str1)
                elif j == ">":
                    str1 += ">"
                    if re.match(opntag,str1):
                        spl = split_open_tag(str1)
                        if len(spl) == 1:
                            ret.push(xt.Token(str1[1:-1],"OPEN",{}))
                        else:
                            tkn = xt.Token(spl[0][1:],"OPEN",{})
                            for i in range(1,len(spl)):
                                j = spl[i].split("=")
                                tkn.attribs[j[0]] = j[1].replace(">","").replace("\"","").replace("\'","")
                            ret.push(tkn)
                        str1 = ""
                    elif re.match(clstag,str1):
                        ret.push(xt.Token(str1[2:-1],"CLOSE",{}))
                        str1 = ""
                    else:
                        raise TypeError("Invalid character : "+j+" in "+str1)
                else:
                    str1 += j
    return ret



                        


