#Anastasia Douka
#260768503
import doctest

def which_delimiter(string):
    '''
    (str)-> str
    This function returns the most commonly used delimiter.
    >>> which_delimiter('0 1 2, 3')
    ' '
    '''
    delimiterDict = {} #empty dict where we will put delimiters
    for char in string:
        if char == ' ' or char == ',' or char == '\t':
            if char not in delimiterDict:
                delimiterDict[char] = 1
            else:
                delimiterDict[char] += 1
    if len(delimiterDict) == 0: 
        raise AssertionError("There exists no delimiter!")
    
    return max(delimiterDict) #take the delimeter used the most


def stage_one(input_filename, output_filename):
    '''
    (file, file) -> int
    This function takes two files as inputs and will return an integer
    of how many lines were written to the second file input.
    >>> stage_one('1111111.txt', 'stage1.tsv')
    3000
    '''
    inFile = open(input_filename, 'r') 
    outFile = open(output_filename, 'w', encoding = 'utf-8')
    records = inFile.readlines() 

    for line in records:
        delimiter = which_delimiter(line) 
        if delimiter != '\t':
            line = line.replace(delimiter, '\t')
        line = line.replace('/', '-')
        line = line.replace('.', '-')
        line = line.upper()
        outFile.write(line)
    outFile.close()
    inFile.close()
    
    return len(records)

def stage_two(input_filename, output_filename):
    '''
    (file, file) -> int
    This function takes as input two files, it makes changes in the first file
    and then returns how many lines were written to the second file (output_filename).
    >>> stage_two(’stage1.tsv’, ’stage2.tsv’)
    3000
    '''
    inFile = open(input_filename, 'r', encoding = 'utf-8') 
    outFile = open(output_filename, 'w', encoding = 'utf-8')
    records = inFile.readlines()
    
    for line in records: #each line in the records
        columns = line.split('\t') #each column in line
        if len(columns) > 9:
            if len(columns[-2])== 1:
                columns[-3] = ''.join(columns[-3:-1])
                del columns[-2]
            else:
                columns[-3]= '.'.join(columns[-3:-1])
                del columns[-2]
                
        line='\t'.join(columns)
        outFile.write(line)

    outFile.close()

    inFile.close()
    
    return len(records)
    
if __name__ == '__main__':
    doctest.testmod
    stage_one('260768503.txt', 'stage1.tsv')
    stage_two('stage1.tsv', 'stage2.tsv')
