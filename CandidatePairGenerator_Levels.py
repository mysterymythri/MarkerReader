from ddlite import *
import BiomarkerCandidateGenerator, LevelCandidateGenerator, MeasurementCandidateGenerator, pickle

all_prefixes_units = [['Ym', 'yottameter'], ['Zm', 'zettameter'], ['Em', 'exameter'], ['Pm', 'petameter'], ['Tm', 'terameter'], ['Gm', 'gigameter'], ['Mm', 'megameter'], ['km', 'kilometer'], ['hm', 'hectometer'], ['dam', 'dekameter'], ['dm', 'decimeter'], ['cm', 'centimeter'], ['\\u03bcm', 'micrometer'], ['nm', 'nanometer'], ['pm', 'picometer'], ['fm', 'femtometer'], ['am', 'attometer'], ['zm', 'zeptometer'], ['ym', 'yoctometer'], ['Ym2', 'square yottameter'], ['Zm2', 'square zettameter'], ['Em2', 'square exameter'], ['Pm2', 'square petameter'], ['Tm2', 'square terameter'], ['Gm2', 'square gigameter'], ['Mm2', 'square megameter'], ['km2', 'square kilometer'], ['hm2', 'square hectometer'], ['dam2', 'square dekameter'], ['dm2', 'square decimeter'], ['cm2', 'square centimeter'], ['\\u03bcm2', 'square micrometer'], ['nm2', 'square nanometer'], ['pm2', 'square picometer'], ['fm2', 'square femtometer'], ['am2', 'square attometer'], ['zm2', 'square zeptometer'], ['ym2', 'square yoctometer'], ['Ym2', 'cubic yottameter'], ['Zm2', 'cubic zettameter'], ['Em2', 'cubic exameter'], ['Pm2', 'cubic petameter'], ['Tm2', 'cubic terameter'], ['Gm2', 'cubic gigameter'], ['Mm2', 'cubic megameter'], ['km2', 'cubic kilometer'], ['hm2', 'cubic hectometer'], ['dam2', 'cubic dekameter'], ['dm2', 'cubic decimeter'], ['cm2', 'cubic centimeter'], ['\\u03bcm2', 'cubic micrometer'], ['nm2', 'cubic nanometer'], ['pm2', 'cubic picometer'], ['fm2', 'cubic femtometer'], ['am2', 'cubic attometer'], ['zm2', 'cubic zeptometer'], ['ym2', 'cubic yoctometer'], ['YL', 'yottaliter'], ['ZL', 'zettaliter'], ['EL', 'exaliter'], ['PL', 'petaliter'], ['TL', 'teraliter'], ['GL', 'gigaliter'], ['ML', 'megaliter'], ['kL', 'kiloliter'], ['hL', 'hectoliter'], ['daL', 'dekaliter'], ['dL', 'deciliter'], ['cL', 'centiliter'], ['\\u03bcL', 'microliter'], ['nL', 'nanoliter'], ['pL', 'picoliter'], ['fL', 'femtoliter'], ['aL', 'attoliter'], ['zL', 'zeptoliter'], ['yL', 'yoctoliter'], ['Yg', 'yottagram'], ['Zg', 'zettagram'], ['Eg', 'exagram'], ['Pg', 'petagram'], ['Tg', 'teragram'], ['Gg', 'gigagram'], ['Mg', 'megagram'], ['kg', 'kilogram'], ['hg', 'hectogram'], ['dag', 'dekagram'], ['dg', 'decigram'], ['cg', 'centigram'], ['\\u03bcg', 'microgram'], ['ng', 'nanogram'], ['pg', 'picogram'], ['fg', 'femtogram'], ['ag', 'attogram'], ['zg', 'zeptogram'], ['yg', 'yoctogram']]

def doEverything():
    parser = DocParser('AGR2_blood_biomarker.txt', ftreader=TextReader())
    sentences = parser.parseDocSentences()

    BM = BiomarkerCandidateGenerator.generateBiomarkerCandidates()
    L = LevelsCandidateGenerator.levelsGenerator()
    M = MeasurementCandidateGenerator.measurementGenerator(L)
    

    possiblePairs = Relations(sentences, BM, L, M)
    feats = possiblePairs.extract_features()
    otherModel = DDLiteModel(possiblePairs, feats)
    negationWords = ["not", "nor", "neither"]


    # 1- distance far
    def LF_distance_far_marker_to_level(m):
        # print m.lemmas
        # print m.dep_labels
        distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
        if distance < 10:
            return 0
        else:
            return -1
        
    # 2- distance far
    def LF_distance_far_marker_to_measurement(m):
        distance = abs(m.e3_idxs[0] - m.e1_idxs[0])
        if distance < 10:
            return 0
        else:
            return -1
            
            
    # 3- distance close
    def LF_distance_close_marker_to_level(m):
        # print m.lemmas
        # print m.dep_labels
        distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
        if distance < 5:
            return 1
        else:
            return 0
        
    # 4- distance close
    def LF_distance_close_marker_to_measurement(m):
        distance = abs(m.e3_idxs[0] - m.e1_idxs[0])
        if distance < 5:
            return 1
        else:
            return 0
            
            
    
    # 5- units 
    def LF_units(m):
        found = False
        for unit in all_prefixes_units:
            if unit[0] in m.post_window2('lemmas',4) or unit[1] in m.post_window2('lemmas',4):
                found = True
        if found:
            return 1
        else:
            return 0
        
    
    LFs = [LF_investigate, LF_key,  LF_distance, LF_keyword, LF_auxpass, LF_inbetween,
           LF_possible, LF_explore, LF_key, LF_investigate, LF_yetToBeConfirmed, LF_notAssociated, LF_notRelated,
           LF_doesNotShow, LF_notLinked, LF_notCorrelated, LF_disprove, LF_doesNotSignify,
           LF_doesNotIndicate, LF_doesNotImply, LF_studies, LF_studies2, LF_studies3, LF_studies4, LF_interesting,
           LF_discussion, LF_conclusion, LF_recently, LF_induced, LF_treatment, LF_isaBiomarker, LF_marker, LF_suspect, LF_mark, LF_People]
    gts = []
    uids = []
    for tuple in mindtaggerToTruth("tags4.tsv"):
        uids.append(tuple[0])
        gts.append(tuple[1])
    otherModel.update_gt(gts, uids=uids)
    otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    otherModel.add_mindtagger_tags()

    otherModel.apply_lfs(LFs, clear=False)
    return otherModel
    # """DEBUGGING CODE"""
    # otherModel.open_mindtagger(num_sample=100, width='100%', height=1200)
    # otherModel.add_mindtagger_tags()
    # otherModel.plot_lf_stats()
    #
    # """END"""
    # # with open("thing.xml", "wb") as f:
    #


def mindtaggerToTruth(filename):
    uids = []
    list = re.split("[^\\S ]", open(filename).read())
    # print list
    count = 7
    while count < len(list):
        number = 0
        if (list[count + 6] == "true"):
            number = 1
        elif (list[count + 6] == "false"):
            number = -1
        uids.append((list[count + 5] + "::" + list[count + 3] + "::[" + list[count + 4] + ", " + list[count] + "]::['" +
                     list[count + 1] + "', '" + list[count + 2] + "']", number))
        count += 7
    return uids
# doEverything()
