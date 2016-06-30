from ddlite import *
import re

mass_units = ['kg','g','ng']
volume_units = ['L','dL','cL','mL','nL']

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

    return words

def levelsGenerator():
    words = parseDocIntoWords()
    print words
    normal_syntax_regex = RegexNgramMatch(label='syntax', regex_pattern=r'(?<=[\s\W])[0-9]+[-,\.]?[0-9]+\s(?=[a-zA-Z,\.])', ignore_case=False, match_attrib='words')
    range_syntax_regex = RegexNgramMatch(label='syntax', regex_pattern=r'[0-9]+\s?[\W^;]?[0-9]+\s[()]{1}[\W0-9^;]+[()]{1}', ignore_case=False, match_attrib='text')
    CE = Union(normal_syntax_regex,range_syntax_regex)
    E = Entities(words, range_syntax_regex)
    for e in E:
        print e.mention(attribute='words')


levelsGenerator()

# Normal 10 mg/l: (?<=\s)[0-9]+\.?[0-9]+\s[a-zA-Z]{1,2}\/?[a-zA-Z]{0,2}


#[0-9]+ \W[LRB]{3,}\W[0-9-]+\W[RRB]{3,}\W [a-zA-Z]+\/?[a-zA-Z]+

#(?<=\s)[0-9]+[.]?[0-9]+\s[a-zA-Z]{1,2}\/?[a-zA-Z]{0,2}|(?<=\s)[0-9]+[.]?[0-9]\s(.+)\s[a-zA-Z]{1,2}\/?[a-zA-Z]{0,2}

#[0-9]+\s?[\W^;]?[0-9]+\s[()]{1}[\W0-9^;]+[()]{1}

#current
