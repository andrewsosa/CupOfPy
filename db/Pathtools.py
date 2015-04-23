# PathTools.py by Andrew Sosa

def split_path(path):
    tokens = path.split("/")
    if len(tokens) > 1 :
        tokens.pop(0)
    return tokens

def form_path(tokens):
    return "/" + "/".join(tokens)
