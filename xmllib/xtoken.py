class Token:
    value = "NULL"
    ttype = "NULL"
    attribs = {}
    def __init__(self,value,ttype,attribs):
        self.attribs = attribs
        self.value = value
        self.ttype = ttype
    def __str__(self):
        return f"<{self.ttype},{self.value}>"


class TokenStream:
    toks = []
    def push(self,tok):
        self.toks.append(tok)
    def get_next(self):
        if len(self.toks) == 0:
            raise IndexError("Index reached 0 - Stream empty")
        tk = self.toks[0]
        del self.toks[0]
        return tk
    


