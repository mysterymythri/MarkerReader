from ddlite import *

from ddlite import *
import unicodedata

def parseDocIntoWords():
    filename = "AGR2_blood_biomarker.txt"
    text = open(filename, "r").read()
    sentence_parser = SentenceParser()
    list = sentence_parser.parse(text, 1)
    words = []
    for sentence in list:
        words.append(sentence)
    return words


def extractTitle(sentences_Article):
    numWordsToExtract = 40
    wordsExtracted = 0
    indexInSentence = 0
    currSentenceWords = ''
    sentenceNum = 0
    unicode_title = []
    for sentence in sentences_Article:
        currSentenceWords = sentence.words
        for word in currSentenceWords:
            unicode_title.append(word)
            wordsExtracted = wordsExtracted + 1
            if wordsExtracted is numWordsToExtract:
                return unicodedata.normalize('NFKD', ' '.join(unicode_title)).encode('ascii', 'ignore')
    return unicodedata.normalize('NFKD', ' '.join(unicode_title)).encode('ascii', 'ignore')


def articleScorer(biomarkerName, diseaseName, numOfRelations, articleMentionsRank):
    sentences_Article = parseDocIntoWords()
    title = extractTitle(sentences_Article)
    titleScore = 0
    relationsRatScore = 0
    mentionsScore = 0
    #Title:
    markerTitleScore = 0
    diseaseTitleScore = 0
    if biomarkerName in title:
        markerTitleScore = 1
    if diseaseName in title:
        diseaseTitleScore = 1
    titleScore = 50 * ((diseaseTitleScore + markerTitleScore) / 2)
    #mentions:
    mentionsScore = 25 * articleMentionsRank
    #relationsRat:
    relationsRatScore = 25 * numOfRelations / len(sentences_Article)

    totalScore = titleScore + mentionsScore + relationsRatScore
    return totalScore

