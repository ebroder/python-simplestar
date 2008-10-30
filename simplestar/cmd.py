from util import AgiError, AgiResult
import sys

def send(line):
    print >>sys.stdout, line
    sys.stdout.flush()

def cmd(*args):
    def f(s):
        if ' ' in s or s == '':
            return '"%s"' % s
        else:
            return s
    
    send(' '.join(f(s) for s in args))
    
    response = sys.stdin.readline()
    if not response.startswith('200 result='):
        raise AgiError, "Unexpected result '%s'" % response
    
    result = AgiResult()
    for v in response[4:].split(' '):
        setattr(result, *v.split('=', 1))
    
    return result
