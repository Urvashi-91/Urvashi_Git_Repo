'''
Source: https://www.blopig.com/blog/2016/08/processing-large-files-using-python/
'''
'''
Below code reads all the data into RAM before attempting to process it line by line.

'''
with open("input.txt") as f:
    data = f.readlines()
    for line in data:
        process(line)

'''
Read data line by line so that single line is stored in the RAM at a time
'''
with open("input.txt") as f:
    for line in f:
        process(line)

'''
Making use of idle cores
generates a set (pool) of workers, ideally one for each core, before creating a bunch of tasks (jobs), 
one for each line, for the workers to do. I tend to use the Pool object provided by the multiprocessing 
module due to ease of use, however, you can spawn and control individual workers using mp.Process if you 
want finer control. For mere number crunching, the Pool object is very good.
'''
import multiprocessing as mp

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    for line in f:
        jobs.append( pool.apply_async(process,(line)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

'''
If the above code runs into memory issue again.
apply_async function doesnt block the pool while processing line by line
But, again all data is read into memory. So, to resolve change the function
open the file, locate specified line, read into memory and then process it.
However, there is still an overhead involved in having to locate the line.
'''
import multiprocessing as mp

def process_wrapper(lineID):
    with open("input.txt") as f:
        for i,line in enumerate(f):
            if i != lineID:
                continue
            else:
                process(line)
                break

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    for ID,line in enumerate(f):
        jobs.append( pool.apply_async(process_wrapper,(ID)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

'''
To resolve reading id and line overhead use seek function
seek function of file objects which skips you to a particular 
location within a file. Combining with the tell function, which returns the current location within a file, gives:
'''
import multiprocessing as mp

def process_wrapper(lineByte):
    with open("input.txt") as f:
        f.seek(lineByte)
        line = f.readline()
        process(line)

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
with open("input.txt") as f:
    nextLineByte = f.tell()
    for line in f:
        jobs.append( pool.apply_async(process_wrapper,(nextLineByte)) )
        nextLineByte = f.tell()

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()

'''
There is still an overhead with the opening and closing the file for each individual line.
If we process multiple lines of the file at a time as a chunk, we can reduce operations.

'''
import multiprocessing as mp,os

def process_wrapper(chunkStart, chunkSize):
    with open("input.txt") as f:
        f.seek(chunkStart)
        lines = f.read(chunkSize).splitlines()
        for line in lines:
            process(line)

def chunkify(fname,size=1024*1024):
    fileEnd = os.path.getsize(fname)
    with open(fname,'r') as f:
        chunkEnd = f.tell()
    while True:
        chunkStart = chunkEnd
        f.seek(size,1)
        f.readline()
        chunkEnd = f.tell()
        yield chunkStart, chunkEnd - chunkStart
        if chunkEnd > fileEnd:
            break

#init objects
pool = mp.Pool(cores)
jobs = []

#create jobs
for chunkStart,chunkSize in chunkify("input.txt"):
    jobs.append( pool.apply_async(process_wrapper,(chunkStart,chunkSize)) )

#wait for all jobs to finish
for job in jobs:
    job.get()

#clean up
pool.close()