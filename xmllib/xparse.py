from tokenizer import *
from xtree import *

def parse_xml(filename):
    xts = tokenize(filename).toks
    stack = []
    stack.append(xNode(xts[0].value,"INTERNAL",xts[0].attribs))
    i = 1

    while len(stack) != 0 and i < len(xts):
        if xts[i].ttype == "OPEN":
            stack.append(xNode(xts[i].value,"INTERNAL",xts[i].attribs))
        elif xts[i].ttype == "VALUE":
            stack.append(xNode(xts[i].value,"LEAF",xts[i].attribs))
        else:
            val = xts[i].value
            child = []
            while stack[-1].value != val:
                child.append(stack[-1])
                stack.pop()
            child.reverse()
            stack[-1].children = child
        i += 1
    
    return stack[-1]


