import pickle
import pandas
# load : get the data from file
inputFileName = 'input.pkl'
data = pickle.load(open('./' + inputFileName, "rb"))
# name of output file
name = 'output'
# max number of line per file
lineNum = 10000
index = 0
for x in range(0, len(data[data.keys()[0]]), lineNum):
	index+=1
    data[x:x+lineNum].to_csv(f'./' + name + '{index}.csv', encoding='utf-16')