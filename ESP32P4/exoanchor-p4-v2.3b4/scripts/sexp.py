import re, json, copy, pathlib, zipfile, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
def parse(path):
    tokens = iter(re.findall(r'"(?:\\.|[^"\\])*"|[()]|[^\s()]+', path.read_text()))
    def read(t):
        if t != '(': return t
        out=[]
        for t in tokens:
            if t == ')': return out
            out.append(read(t))
        raise ValueError('unclosed expression')
    return read(next(tokens))
def val(s): return json.loads(s) if s.startswith('"') else s
def q(s): return json.dumps(s,ensure_ascii=False)
def children(n,k): return [x for x in n if isinstance(x,list) and x and x[0]==k]
def child(n,k): return next(iter(children(n,k)),None)
def prop(n,k): return next((x for x in children(n,'property') if val(x[1])==k),None)
def emit(n,d=0):
    if not isinstance(n,list): return n
    if not any(isinstance(x,list) for x in n):return '('+' '.join(n)+')'
    return '('+''.join(('\n'+'  '*(d+1)+emit(x,d+1)) if isinstance(x,list) else ((' ' if i else '')+x) for i,x in enumerate(n))+'\n'+'  '*d+')'
def save(n,path):path.write_text(emit(n)+'\n')
