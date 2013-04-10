#for line in open("1.txt"):
import sys
#filename = sys.argv[1]
#infile=open(filename)
for line in open(sys.argv[1]):
    for word in line.split():
        if word.endswith('ing'):
            print word
            