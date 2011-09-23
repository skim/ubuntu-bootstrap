import sys, shlex, subprocess, os.path, tempfile

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
    fprint()
    

def removespace(s):
    return ''.join(s.split())
    
def sub(line, echo=True, promt="$ "):
    args = shlex.split(line)
    if echo:
        fprint("%s%s", promt, " ".join(args))
    return subprocess.call(args)
    

def tofile(text, filename, sudo=False, readable=True):
    fprint(text)
    pre = ""
    if sudo:
        pre = "sudo "
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(text)
    f.close()
    sub("%scp %s %s" % (pre, f.name, filename))
    if readable:
        sub("%schmod a+r %s" % (pre, filename))


def workpath(conf, relativename):
    if relativename.startswith("/"):
        relativename = relativename[1:]
    return os.path.join(conf.workdir, relativename)
