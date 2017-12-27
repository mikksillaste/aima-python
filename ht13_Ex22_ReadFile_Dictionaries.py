# loendur dictionary
counter_dict = {}
# loe failist ridade kaupa ja loendab dictionarisse erinevad nimed
with open('/Users/mikksillaste/Downloads/aima-python/nameslist.txt') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1
        line = f.readline()

# loeb failist ridade kaupa ja loendab dictionarisse erinevad kategooriad, mille jaoks on vaja kindlat osa reast [3:-26]
counter_dict2 = {}
with open('/Users/mikksillaste/Downloads/aima-python/Training_01.txt') as f:
    line = f.readline()
    while line:
        line = line[3:-26]
        if line in counter_dict2:
            counter_dict2[line] += 1
        else:
            counter_dict2[line] = 1
        line = f.readline()

print(counter_dict)
print(counter_dict2)
