import sys

def env(fd=sys.stdin):
    """
    Parse the AGI environment information and return it in a dict
    
    Read in a series of "key: value" lines, storing the key/value
    pairs into a dict. The end of the environment is marked by an
    empty line.
    """
    vars = {}
    while True:
        line = fd.readline().strip()
        if line == '':
            break
        key, data = (i.strip() for i in line.split(':'))
        if key != '':
            vars[key] = data
    
    return vars
