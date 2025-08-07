import sys

if len(sys.argv) < 2:
    sys.exit("too less arguments")

for arg in sys.argv[1:]:
    print("hello, my naem is", arg)