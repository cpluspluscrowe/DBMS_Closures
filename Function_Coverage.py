#Consider R (ABCDEF) with F = {A B, B CE, CD A}. Compute (i) A+; (ii) (CD)+.
import itertools

d = {'A':['B'],'B':['CE'],'CD':['A']}

def decomposition(key):
    for value in d[key]:
        if len(value) > 1:
            for letter in value:
                if not IsInDictionary(key,letter):
                    d[key].append(letter)

def transitivity():
    for x in d:
        for k1 in d:
            v1s = d[k1]
            for value in v1s:
                if value in d:
                    for v2 in d[value]:
                        if not IsInDictionary(k1,v2):
                            d[k1].append(v2)

def GetLetters(List):
    l = []
    for letter in List:
        l.append(letter)
    return l

def IsInDictionary(key,check_value):
    if not key in d:
        return False
    if check_value in d[key]:
        return True
    keys = GetLetters(d[key])
    values = GetLetters(check_value)
    for val in values:
        if val in keys:
            pass
        else:
            return False
    return True

def reflexivity(key):
    keys = GetLetters(key)
    for letter in keys:
        if not letter in d[key]:
            d[key].append(letter)

def closure(letter):
    if letter in d:
        s = set()
        for List in d[letter]:
            for val in List:
                s.add(val)
    l = list(s)
    l.sort()
    string = ''.join(l)
    return string

def GetRList():
    r = GetR()
    l = []
    for letter in r:
        l.append(letter)
    return l

def GetR():
    r = set()
    for k in d:
        for kletter in k:
            r.add(kletter)
        for val in d[k]:
            for letter in val:
                r.add(letter)
    l = list(r)
    l.sort()
    string = ''.join(l)
    return string

def noRepeats(value):
    s = set()
    for letter in value:
        s.add(letter)
    l = list(s)
    l.sort()
    string = ''.join(l)
    return string

def AddAugmentValues(key_from,key_to_append_to,augmentation):
    print("Adding Augment:",key_from,key_to_append_to,augmentation)
    changed = False
    from_vals = d[key_from]
    to_vals = d[key_to_append_to]
    for already in from_vals:
        aug_already = noRepeats(already + augmentation)
        if not IsInDictionary(key_to_append_to,aug_already):
            d[key_to_append_to].append(aug_already)
            changed = True
    return changed

def Augment(key,value_to_augment):
    new_key = noRepeats(key + value_to_augment)
    if not key in d:
        print(key,"Not in d!")
        return False
    if new_key in d:
        return False
    new_values = set()
    values = d[key]
    for val in values:
        new_val = noRepeats(val + value_to_augment)
        new_values.add(new_val)
    if new_key in d:
        changed = AddAugmentValues(key,new_key,value_to_augment)
        return changed
    d[new_key] = list(new_values)
    return True

def aggregate(new_key):
    pass

def aggregations():
    for key in list(d):
        R = GetRList()
        for cnt in range(2):
            for x in itertools.combinations(R,cnt):
                l = list(x)
                l.sort()
                string = ''.join(l)
                if Augment(key,string):
                    pass
              
for key in list(d):
    decomposition(key)
    print("Dec:",d['A'])
    transitivity()
    print("Trans",d['A'])
    for k in list(d):
        reflexivity(k)
    print("Reflex",d['A'])
    aggregations()
    print("Aggr",d['A'])


#aggregations()
#closureA = closure('A')
#print(closureA)
#print(GetRList())
#print(d)
















