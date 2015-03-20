from heapq import heappop, heappush, heappushpop
import subprocess
import string
import sys

#Create a sorted list of file names
word_files_output = subprocess.check_output(["ls",sys.argv[1]])
word_files_list = word_files_output.split()
word_files_list.sort()

#Define a function to return the number of words on each line
def my_fun(i):
    input = sys.argv[1] + i
    f = open(input,'r')
    out = f.read().translate(string.maketrans("",""), string.punctuation)
    out = out.split("\n")
    numbers = map(lambda x: len(x.split()),out)
    return numbers

#Define the running median function using a binary tree
def running_median(seq):
    seq = iter(seq)
    left, right  = [], [next(seq)]
    while True:
        yield float(right[0]) if len(right) > len(left) else (right[0] - left[0])/2.0
        heappush(left, -heappushpop(right, next(seq)))
        if len(left) > len(right):
            heappush(right, -heappop(left))

try:
    #Execute the map function and reduce the output to a single stream of numbers
    map_result = map(my_fun,word_files_list)
    numbers = reduce((lambda x,y:x+y),map_result)

    #Execute the running_median function.
    running_median_result = [item for item in running_median(numbers)]
    formatted_result = map((lambda x:str(x)+"\n"),running_median_result)
    formatted_result = reduce((lambda x,y: x+y),formatted_result)
except:
    print "Could not execute function."

#Output the running median.
out = open(sys.argv[2], 'w')
out.write(formatted_result)
out.close()
