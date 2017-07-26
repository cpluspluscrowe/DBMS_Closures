#Consider R (ABCDEF) with F = {A B, B CE, CD A}. Compute (i) A+; (ii) (CD)+.
import itertools
from copy import deepcopy

#d = {'A':['BC'],'B':['CE'],'CD':['A']}
#d = {'A':['B'],'B':['CE'],'DE':['AF']}
#R (ABCDEFG) and the
#F = {AC B, AB C, ACD  BE, C  D, EF}
d = {'AC':['B'],'AB':['C'],'ACD':['BE'],'C':['D'],'E':['F']}

def decomposition(key,tracking):
    for value in d[key]:
        if len(value) > 1:
            for letter in value:
                if not IsInDictionary(key,letter):
                    if key == tracking:
                        print("By Decompositon: " + key + " -> " + letter)
                    d[key].append(letter)

def transitivity(tracking):
    for x in d:
        for k1 in d:
            v1s = d[k1]
            for value in v1s:
                if value in d:
                    for v2 in d[value]:
                        if not IsInDictionary(k1,v2):
                            if k1 == tracking:
                                print("By Transitivity: " + k1 + " -> " + value + "; " + value + " -> " + v2 + "; implies " + k1 + " -> " + v2)
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

def reflexivity(key,tracking):
    keys = GetLetters(key)
    for letter in keys:
        if not letter in d[key]:
            if key == tracking:
                print("By Reflexivity: " + key + " -> " + letter)
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
        for cnt in range(3):
            for x in itertools.combinations(R,cnt):
                l = list(x)
                l.sort()
                string = ''.join(l)
                if Augment(key,string):
                    pass

def Closure(variable_to_track):
    d_changed = True
    while d_changed:
        d_start = deepcopy(d)
        for key in list(d):
            decomposition(key,variable_to_track)
            transitivity(variable_to_track)
            for k in list(d):
                reflexivity(k,variable_to_track)
            aggregations()
        if d_start == d:
            d_changed = False
    c = closure(variable_to_track)
    print("Closure of " + variable_to_track + ": " + c)

def RemoveComplexValues():
    for key in list(d):
        for value in list(d[key]):
            if len(value) > 1:
                d[key].remove(value)

def Canonical_Closure():
    RemoveComplexValues()
    for k1 in list(d):
        for k2 in list(d):
            if k1 != k2:
                vals1 = d[k1]
                vals2 = d[k2]
                for v1 in vals1:
                    for v2 in vals2:
                        if v1 == v2:
                            if len(k1) > len(k2):
                                d[k1].remove(v1)
                            else:
                                d[k2].remove(v2)
    for key in list(d):
        if key in d[key]:
            d[key].remove(key)
        if len(key) > 1:
            for letter in key:
                if letter in d[key]:
                    d[key].remove(letter)
    for key in list(d):
        if d[key] == []:
            del d[key]
    print("Canonical Closure:")
    for key in d:
        values = d[key]
        values.sort()
        print(key + " -> " + ''.join(values))
    print()

Canonical_Closure()

#aggregations()
#closureA = closure('A')
#print(closureA)
#print(GetRList())
#print(d)
















