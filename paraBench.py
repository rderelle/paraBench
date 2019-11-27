
import sys
import csv
import itertools


print('\n        -- paraBench --\n\n')


### get the reference classification
# try to open the file
print(' read the reference classication')
try:
    file_content = csv.reader(open('reference_classification.txt'), delimiter=' ')
except:
    sys.exit(' ERROR: the file \'reference_classification.txt\' containing the reference classification is not present\n\n')

# extract proteins and pairs
all_prot    = set()
ortho_pairs = set() 
for line in file_content:
    all_prot |= set(line)
    # build orthologous pairs
    line.sort()
    for x in itertools.combinations(line, 2):
        ortho_pairs.add( x[0] + '-' + x[1] )



### initialise variables
TP = 0
FN = 0
FP = 0



### get the input file
print(' read the input classication')
# try to open the file
if len(sys.argv) == 1:
    sys.exit('\n ERROR: you should specify the file containing your classification\n\n')
else:
    try:
        file_content = open(sys.argv[1],'r')
    except:
        sys.exit('\n ERROR: the name or path of your classification is incorrect\n\n')

# check list of OGs
for line in file_content: 
    if not line.startswith('#jegfufe'):
        # clean the line
        line = line.strip('\n')
        line = line.replace('	',' ')
        line = line.replace(', ',' ')
        line = line.replace(',',' ')
        # build orthologous pairs
        insert = line.split(' ')
        insert2 = [x for x in insert if x in all_prot]
        insert2.sort()
        for x in itertools.combinations(insert2, 2):
            pair = x[0] + '-' + x[1]
            if pair in ortho_pairs:
                TP += 1
                ortho_pairs.remove(pair)
            else:
                FP += 1



### compute the metrics
print('\n\n RESULTS:\n')
# false negatives are all remaning ortho pairs
FN = len(ortho_pairs)

# calculate precision, recall and F1-score
precision = TP / (TP + FP)
recall    = TP / (TP + FN)
F1 = (precision + recall) / 2

# print results  
print(' TP = ' + str(TP))
print(' FP = ' + str(FP))
print(' FN = ' + str(FN))
print(' precision = ' + str(round(precision,5)))
print(' recall    = ' + str(round(recall,5)))
print(' F1-score  = ' + str(round(F1,5)))
print('')   


