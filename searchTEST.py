import pickle, os, sys, re
import unicodedata
from ddlite import *

authorScores = [0]

from itertools import izip_longest
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 300

with open('Try.txt') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open('small_file_{0}'.format(i * n), 'w') as fout:
            fout.writelines(g)

def parseDocIntoWords(_filename):
    filename = _filename
    text = open(filename, "r").read()
    sentence_parser = SentenceParser()
    list = sentence_parser.parse(text, 1)
    words = []
    for sentence in list:
        words.append(sentence)
    return words

def getCitations():
    complexThings = parseDocIntoWords("Try.txt")
    allWords = []
    for complexthing in complexThings:
       for word in complexthing.words:
           allWords.append(word)
    #normalized_Pos = unicodedata.normalize('NFKD', allWords[0]).encode('ascii', 'ignore')
    references = "References"
    refIndex = allWords.index(references)
    print refIndex
    return allWords[refIndex + 1:]

def getAuthors():
    #start and end with uppercase letters
    #below "references"
    #comma or period after end of name

    citations = getCitations()
    capitalIndex = 0
    authorList = []
    commasIndex = citations.index(",")
    #loops through all words, finds a capital letter and a comma, adds string between them to a list of authors
    for x in citations:
        print x
        # input = raw_input("FISH")
        true = re.search('(?<=[A-Z])//w+', x)
        if true:
            capitalIndex = citations.index(x)
        if (capitalIndex == commasIndex-1 and "," in citations[0:]):
            commasIndex = citations.index(",")
        authorList.append(citations[capitalIndex:commasIndex - 1])
        counter = 0
        new = []
        # print authorList
        #for item in authorList:
            #for i in item

    return authorList

def updateScores():
    for x in getAuthors():
        authorScores[authorScores.index(x)] += 1

updateScores()
print authorScores
