import pickle, os, sys, re
import unicodedata
from ddlite import *

authorScores = [0]

from itertools import izip_longest

def grouper(n, iterable, _filename, fillvalue=None):

    "Collect data into fixed-length chunks or blocks"

    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx

    args = [iter(iterable)] * n

    return izip_longest(fillvalue=fillvalue, *args)



def parseDocIntoWords(_filename):
    filename = _filename
    text = open(filename, "r").read()
    text = text.replace('\n', ',')
    # print text
    #re.findare.findall(r"[\w']+", DATA)ll(r"[\w']+", DATA)
    words = text.split(',')
    return words
    #return strings

def getCitations(_filename):
    allWords = []
    files = []
    file_base_name = _filename
    full_text_string = open(_filename).read()
    num_new_lines = full_text_string.count("\n")
    number_small_files = int((float(num_new_lines) / 300.0) + 1)
    file_num = 300
    while file_num <= (number_small_files)*300:
        files.append(file_base_name + str(file_num))
        file_num = file_num + 300
    # print files
    for file in files:
        complexThings = parseDocIntoWords(file)
        for complexthing in complexThings:
            allWords.append(complexthing)
        references = "References"
        refIndex = allWords.index(references)
        print refIndex
    #print allWords
    return allWords


def getAuthors(_filename):
    citations = getCitations(_filename=_filename)
    print "no"
    print citations
    print "hi"
    capitalIndex1 = -1
    capitalIndex2 = -1
    authorList = []
    for x in citations:
        # print type(x)
        #CURRENT PROBLEM
        if (x[0] != x[0].upper()):
            #print 'hgfd'
            citations.remove(x)
        for y in x:
            if (x[len(x)-1] == x[len(x)-1].upper()):
                capitalIndex2 = len(x)-1
        authorList.append(citations[capitalIndex1:capitalIndex2])
        counter = 0
        new = []
    print authorList
    return authorList

def updateScores(_filename):
    n = 300

    with open(_filename) as f:

        for i, g in enumerate(grouper(n, f, fillvalue='',  _filename= _filename), 1):
            with open( _filename + '{0}'.format(i * n), 'w') as fout:
                fout.writelines(g)
    for x in getAuthors(_filename):
        #print x
        authorScores[authorScores.index(x)] += 1

updateScores("try.txt")
#print authorScores
