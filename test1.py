#-*-coding:utf-8-*-
from mpi4py import MPI
from csv import DictReader, field_size_limit
from os import listdir
from sys import maxsize

maxInt = maxsize
decrement = True

arr = []
comm = MPI.COMM_WORLD
indices = 0
def test():
    with open ('/Users/juanestebanfonseca/Documents/prueba.csv') as csvf:
        readCSV = DictReader(csvf)
        #print(readCSV["content"])
        #readCSV = [1,2,3]
        for row in readCSV:
            arr.append(row)
            print(row["Edad"])
    #print("Comm.size: ",comm.size)
    csvf.close()
    print("Comm.size")
    print(comm.size)
    print("lenght arr")
    print(len(arr))
        #indices = len(arr)/comm.size
        #print(indices)
#indices = len(arr)/comm.size
#print(indices)


while decrement:

    decrement = False
    try:
        field_size_limit(maxInt)
    except OverflowError:
        maxInt = int(maxInt/10)
        decrement = True

    test()
