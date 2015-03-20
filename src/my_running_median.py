from heapq import heappush, heappop
import subprocess
import string
import sys

#Create a sorted list of file names.
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

#Execute the map function.
#Reduce it to a single list
arou = map(my_fun,word_files_list)
numbers = reduce((lambda x,y:x+y),arou)

#with open('/home/aking/p/raw_files/'+i,'r') as f:
#      output = f.read().translate(string.maketrans("",""), string.punctuation)


from heapq import heappop, heappush, heappushpop

def streaming_median(seq):
    seq = iter(seq)
    left, right  = [], [next(seq)]
    while True:
        yield right[0] if len(right) > len(left) else (right[0] - left[0])/2.0

        heappush(left, -heappushpop(right, next(seq)))
        if len(left) > len(right):
            heappush(right, -heappop(left))


a = [float(item) for item in streaming_median(numbers)]
b = map((lambda x:str(x)+"\n"),a)
b = reduce((lambda x,y: x+y),b)

out = open(sys.argv[2], 'w')
out.write(b)
out.close()
