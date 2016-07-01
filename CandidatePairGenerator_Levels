from ddlite import *
import BiomarkerCandidateGenerator, DiseaseCandidateGenerator, pickle


def doEverything():
    parser = DocParser('AGR2_blood_biomarker.txt', ftreader=TextReader())
    sentences = parser.parseDocSentences()

    BM = BiomarkerCandidateGenerator.generateBiomarkerCandidates()
    DM = DiseaseCandidateGenerator.generateDiseaseCandidates()

    possiblePairs = Relations(sentences, BM, DM)
    feats = possiblePairs.extract_features()
    otherModel = DDLiteModel(possiblePairs, feats)
    keyWords = ["associate", "express", "marker", "biomarker", "elevated", "decreased",
                "correlation", "correlates", "found", "diagnose", "variant", "appear",
                "connect", "relate", "exhibit", "indicate", "signify", "show", "demonstrate",
                "reveal", "suggest", "evidence", "elevation", "indication", "diagnosis",
                "variation", "modification", "suggestion", "link", "derivation", "denote",
                "denotation", "demonstration", "magnification", "depression", "boost", "level",
                "advance", "augmentation", "lessening", "enhancement", "expression", "buildup",
                "diminishing", "diminishment", "reduction", "drop", "dwindling", "lowering"]
    negationWords = ["not", "nor", "neither"]

    def presenceOfNot(m):
        for word in negationWords:
            if (word in m.post_window1('lemmas', 20)) and (word in m.pre_window2('lemmas', 20)):
                return True
        return False

    # 1
    def LF_distance(m):
        # print m.lemmas
        # print m.dep_labels
        distance = abs(m.e2_idxs[0] - m.e1_idxs[0])
        if distance < 8:
            # print "RETURNING ONE"
            return 0
        else:
            return -1



    def LF_mark(m):
        return -1 if ( 'vmod' in m.post_window1('dep_labels', 20) and 'mark' in m.post_window1('dep_labels', 20) or'vmod' in m.pre_window1('dep_labels', 20) and 'mark' in m.pre_window1('dep_labels', 20)) else 0
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
