from xparse import *
import json as js

def JSONBUild(Node):
    dic = {f"{Node.value}": {i:Node.attribs[i] for i in Node.attribs}}
    if len(Node.children) == 1 and Node.children[0].xtype == "LEAF":
        if len(Node.attribs) == 0:
            dic[f"{Node.value}"] = Node.children[0].value
        else:
            dic[f"{Node.value}"]["value"] = Node.children[0].value
        return dic
    for i in Node.children:
        d1 = JSONBUild(i)
        if len(d1.keys()) == 1:
            if i.value in dic[f"{Node.value}"]:
                if not isinstance(dic[f"{Node.value}"][i.value], list):
                    dic[f"{Node.value}"][i.value] = [dic[f"{Node.value}"][i.value]]
                dic[f"{Node.value}"][i.value].append(d1[i.value])
            else:
                dic[f"{Node.value}"][i.value] = d1[i.value]
        else:
            if i.value in dic[f"{Node.value}"]:
                if not isinstance(dic[f"{Node.value}"][i.value], list):
                    dic[f"{Node.value}"][i.value] = [dic[f"{Node.value}"][i.value]]
                dic[f"{Node.value}"][i.value].append(d1)
            else:
                dic[f"{Node.value}"][i.value] = d1
    return dic


def dumpJSON(inputFileName,outputFileName):
    node = parse_xml(inputFileName)
    dic = JSONBUild(node)
    fcont = js.dumps(dic,indent=1)
    file = open(outputFileName,'wt')
    file.write(fcont)
    file.close

print(dumpJSON("../t.xml","../jsons/my.json"))