from ddlite import *



def parseDocIntoWords():
    filename = "AGR2_blood_biomarker.txt"
    text = open(filename, "r").read()
    sentence_parser = SentenceParser()
    list = sentence_parser.parse(text, 1)
    words = []
    for sentence in list:
        words.append(sentence)
        print sentence

    return words

def measurementGenerator(levels_entities):
  
  words = parseDocIntoWords()
    all_levels_idxs = []
    for level in levels_entities:
      level_idxs = [level.sent_id, level.idxs[0]]
      all_levels_idxs.append(level_idx)
      
    
    
    normal_syntax_regex = RegexNgramMatch(label='normal', regex_pattern=r'(?<=[^a-zA-Z:;])[0-9]+[-,\.]?[0-9]+', ignore_case=False, match_attrib='lemmas')
    E = Entities(obj, CE)


levelsGenerator()

