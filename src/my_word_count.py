from nltk import word_tokenize
import time
import multiprocessing as mp
import os, subprocess, sys
import string
from collections import Counter

data_files_output = subprocess.check_output(["ls",sys.argv[1]])
d = data_files_output.split()
def my_fun(i):
    input = sys.argv[1] + i
    f = open(input,'r')
    out = f.read().translate(string.maketrans("",""), string.punctuation)
    wordcount = Counter(word_tokenize(out.lower()))
    return wordcount

bert = map(my_fun,d)
ernie = reduce( (lambda x,y:x+y), bert)
arc = ernie.items()
arc.sort()

output = ''
for item in arc:
    if(len(item[0]) <= 7):
        output += item[0] + "\t\t" + str(item[1])
    else:
        output += item[0] + "\t" + str(item[1])
    output += "\n"

out = open(sys.argv[2], 'w')
out.write(output)
out.close()



