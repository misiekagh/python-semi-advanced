import json, pickle
kwiatki = {}

with open('iris.data') as plik:
    for l in plik:
        *vals,name = l.rstrip('\n').split(',')
        if name not in kwiatki.keys():
                    kwiatki[name] = []
        kwiatki[name] += [float(v) for v in vals],

    kwiatki = {k: list(map(list, zip(*v))) for k, v in kwiatki.items()}

with open('kwiatki_nf.json', 'w') as f: json.dump(kwiatki, f)

with open('kwiatki_nl.json','w') as file:
    for k,l in kwiatki.items():
        json.dump({k:{'avg':[sum(v)/len(v) for v in l],
                      'min':[min(v) for v in l],
                       'max':[max(v) for v in l]}}, file)
        file.write('\n')
