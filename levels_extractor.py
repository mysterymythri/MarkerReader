from ddlite import *
import re

prefixes = [['Y','yotta'],['Z','zetta'],['E','exa'],['P','peta'],['T','tera'],['G','giga'],['M','mega'],['k','kilo'],['h','hecto'],
            ['da','deka'],['d','deci'],['c','centi'],['\u03bc','micro'],['n','nano'],['p','pico'],['f','femto'],['a','atto'],
            ['z','zepto'],['y','yocto']]
length_unit = ['m','meter']
area_unit = ['m2','square ','meter']
volume_unit = ['m3','cubic ','meter']
liquid_volume_unit = ['L','liter']
mass_unit = ['g','gram']

all_prefixes_units = [['Ym', 'yottameter'], ['Zm', 'zettameter'], ['Em', 'exameter'], ['Pm', 'petameter'], ['Tm', 'terameter'], ['Gm', 'gigameter'], ['Mm', 'megameter'], ['km', 'kilometer'], ['hm', 'hectometer'], ['dam', 'dekameter'], ['dm', 'decimeter'], ['cm', 'centimeter'], ['\\u03bcm', 'micrometer'], ['nm', 'nanometer'], ['pm', 'picometer'], ['fm', 'femtometer'], ['am', 'attometer'], ['zm', 'zeptometer'], ['ym', 'yoctometer'], ['Ym2', 'square yottameter'], ['Zm2', 'square zettameter'], ['Em2', 'square exameter'], ['Pm2', 'square petameter'], ['Tm2', 'square terameter'], ['Gm2', 'square gigameter'], ['Mm2', 'square megameter'], ['km2', 'square kilometer'], ['hm2', 'square hectometer'], ['dam2', 'square dekameter'], ['dm2', 'square decimeter'], ['cm2', 'square centimeter'], ['\\u03bcm2', 'square micrometer'], ['nm2', 'square nanometer'], ['pm2', 'square picometer'], ['fm2', 'square femtometer'], ['am2', 'square attometer'], ['zm2', 'square zeptometer'], ['ym2', 'square yoctometer'], ['Ym2', 'cubic yottameter'], ['Zm2', 'cubic zettameter'], ['Em2', 'cubic exameter'], ['Pm2', 'cubic petameter'], ['Tm2', 'cubic terameter'], ['Gm2', 'cubic gigameter'], ['Mm2', 'cubic megameter'], ['km2', 'cubic kilometer'], ['hm2', 'cubic hectometer'], ['dam2', 'cubic dekameter'], ['dm2', 'cubic decimeter'], ['cm2', 'cubic centimeter'], ['\\u03bcm2', 'cubic micrometer'], ['nm2', 'cubic nanometer'], ['pm2', 'cubic picometer'], ['fm2', 'cubic femtometer'], ['am2', 'cubic attometer'], ['zm2', 'cubic zeptometer'], ['ym2', 'cubic yoctometer'], ['YL', 'yottaliter'], ['ZL', 'zettaliter'], ['EL', 'exaliter'], ['PL', 'petaliter'], ['TL', 'teraliter'], ['GL', 'gigaliter'], ['ML', 'megaliter'], ['kL', 'kiloliter'], ['hL', 'hectoliter'], ['daL', 'dekaliter'], ['dL', 'deciliter'], ['cL', 'centiliter'], ['\\u03bcL', 'microliter'], ['nL', 'nanoliter'], ['pL', 'picoliter'], ['fL', 'femtoliter'], ['aL', 'attoliter'], ['zL', 'zeptoliter'], ['yL', 'yoctoliter'], ['Yg', 'yottagram'], ['Zg', 'zettagram'], ['Eg', 'exagram'], ['Pg', 'petagram'], ['Tg', 'teragram'], ['Gg', 'gigagram'], ['Mg', 'megagram'], ['kg', 'kilogram'], ['hg', 'hectogram'], ['dag', 'dekagram'], ['dg', 'decigram'], ['cg', 'centigram'], ['\\u03bcg', 'microgram'], ['ng', 'nanogram'], ['pg', 'picogram'], ['fg', 'femtogram'], ['ag', 'attogram'], ['zg', 'zeptogram'], ['yg', 'yoctogram']]



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
#(?<=[\s\W])[0-9]+[-,\.]?[0-9]+\s(?=[a-zA-Z,\.])'

def levelsGenerator():
    words = parseDocIntoWords()

    normal_syntax_regex = RegexNgramMatch(label='normal', regex_pattern=r'(?<=[^a-zA-Z:;])[0-9]+[-,\.]?[0-9]+', ignore_case=False, match_attrib='lemmas')
    range_syntax_regex = RegexNgramMatch(label='range', regex_pattern=r'[0-9]+[\W^;]?[0-9]+\s[()][^\sa-zA-Z()]+[()]', ignore_case=False, match_attrib='text')
    CE = Union(normal_syntax_regex,range_syntax_regex)
    for sentence in words:
        obj = [sentence]
        E = Entities(obj, CE)
        for e in E:
            print e.mention(attribute='words')


levelsGenerator()



