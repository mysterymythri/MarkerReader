
from ddlite import *

from itertools import izip_longest
def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

n = 300

with open('AGR2_blood_biomarker.txt') as f:
    for i, g in enumerate(grouper(n, f, fillvalue=''), 1):
        with open('small_file_{0}'.format(i * n), 'w') as fout:
            fout.writelines(g)

def parseDocIntoWords():
    filename = "AGR2_blood_biomarker.txt"
    text = open(filename, "r").read()
    sentence_parser = SentenceParser()
    list = sentence_parser.parse(text, 1)
    words = []
    for sentence in list:
        words.append(sentence)
    print words
    return words


def TestTypeGenerator(levels_entities):
    words = parseDocIntoWords()
    sentence_candidates = []
    all_levels_idxs = []
    for level in levels_entities:
        level_idxs = [level.sent_id, level.idxs[0]]
        all_levels_idxs.append(level_idxs)
        sentence_candidates.append(words[level.sent_id])

    noun_regex = RegexNgramMatch(label='Nouns', regex_pattern=r'[A-Z]?NN[A-Z]?', ignore_case=True, match_attrib='poses')

    E = Entities(sentence_candidates, noun_regex)
    return E
