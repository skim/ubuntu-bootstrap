import sys, shlex, subprocess, os.path

class Config(object):
    pass


def config(filename="default.config"):
    config = Config()
    execfile(filename, config.__dict__)
    return config


def pubdir(o):
    return filter(lambda n: not n.startswith("__"), dir(o))


def fprint(s="", *x):
    print s % (x)
    
    
def fheadline(s, *x):
    fprint()
    fprint(s, *x)
    
def sub(line, echo=True, promt="$ "):
    args = shlex.split(line)
    if echo:
        fprint("%s%s", promt, " ".join(args))
    return subprocess.call(args)

