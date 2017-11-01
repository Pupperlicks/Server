import sys
filename = "app.py"
source = open(filename, 'r').read() + '\n'
compile(source, filename, 'exec')