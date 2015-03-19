#Import the necessary libraries
from nltk import word_tokenize
import time
import os, subprocess, sys
import string
from collections import Counter

#Define d, where d is a list of all filenames
data_files_output = subprocess.check_output(["ls",sys.argv[1]])
d = data_files_output.split()

#Define the map function.
#It will read in a file, remove punctuation, convert to lowercase, tokenize and count each word.
def my_fun(i):
    input = sys.argv[1] + "/" + i
    f = open(input,'r')
    out = f.read().translate(string.maketrans("",""), string.punctuation)
    wordcount = Counter(word_tokenize(out.lower()))
    return wordcount

#Execute the map function for all items in d
map_result = map(my_fun,d)

#Execute the reduce function
#It takes map_result as an argument which is a list of Counter objects.
reduce_result = reduce( (lambda x,y:x+y), map_result)

#Retrieve the items of the reduce result and sort alphabetically
final_list = reduce_result.items()
final_list.sort()

#Format the final_list
#Ensure a consistent display by adding two tabs between word and count if the length of a word is seven characters or less
output = ''
for item in final_list:
    if(len(item[0]) <= 7):
        output += item[0] + "\t\t" + str(item[1])
    else:
        output += item[0] + "\t" + str(item[1])
    output += "\n"

#Output to the specified file
out = open(sys.argv[2], 'w')
out.write(output)
out.close()



