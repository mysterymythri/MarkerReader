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
            
def largeDocReader ()
    allWords = []
        files = []
        file_base_name = "AGR2_small_file_"
        full_text_string = open("AGR2_blood_biomarker.txt").read()
        num_new_lines = full_text_string.count("\n")
        number_small_files = int((float(num_new_lines) / 300.0) + 1)
        file_num = 300
        while file_num < (number_small_files) * 300 or file_num == (number_small_files) * 300:
            print "Here"
            files.append(file_base_name + str(file_num))
            file_num = file_num + 300
        for file in files:
            words = parseDocIntoWords(file)
            for i in words:
                allWords.append(i)