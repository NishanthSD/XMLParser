class xNode:
    value = "NULL"
    attribs = {}
    children = []
    xtype = "LEAF"
    def __init__(self,value,xtype,attrib):
        self.attribs = attrib
        self.value = value
        self.xtype = xtype
    def __str__(self):
        return f"<{self.value},{self.xtype},children : {len(self.children)}>"
