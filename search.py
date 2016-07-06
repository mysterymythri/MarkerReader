import pickle, os, sys, re
import unicodedata
from ddlite import *

authorScores = [0]

def parseDocIntoWords():
    filename = "AGR2_blood_biomarker.txt"
    text = open(filename, "r").read()
    # print "OPENING FILE"
    sentence_parser = SentenceParser()
    list = sentence_parser.parse(text, 1)
    # print "PARSED TEXT"
    words = []
    # print "GETTING ALL WORDS"
    poses = []
    for sentence in list:
        words.append(sentence)
    # print words
    return words

def getCitations():
    allWords = parseDocIntoWords()
    print allWords
    #normalized_Pos = unicodedata.normalize('NFKD', allWords[0]).encode('ascii', 'ignore')
    references = "REFERENCES"
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

    #loops through all words, finds a capital letter and a comma, adds string between them to a list of authors
    for x in citations:
        true = re.search('(?<=[A-Z])//w+', x)
        if true:
            capitalIndex = citations.index(x)
        if ("," in citations[0:]):
            commasIndex = citations.index(",")
        authorList.append(citations[capitalIndex, commasIndex])
    return authorList

def updateScores():
    for x in getAuthors():
        authorScores[authorScores.index(x)] += 1

updateScores()
print authorScores