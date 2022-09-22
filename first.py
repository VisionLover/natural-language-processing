# import nltk
# nltk.download('wordnet') // you should download this lib first 
from re import split
from itertools import groupby
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.util import Index

dct = {}
dct1 = {}
def indexing():
    f = open("train.csv",encoding="utf8")
    for i, line in enumerate(f):
        title = line.split(",")[0]
        plot = line.split(",")[1]
        for k, g in groupby(enumerate(title), lambda x: not x[1].isspace()):
            if k:
                pos, first_item = next(g)
                text = first_item + ''.join([x for _, x in g])
                ps = PorterStemmer() 
                text = text.casefold() #case folding
                tokenizer = RegexpTokenizer(r'\w+') # remove writing marks
                array = tokenizer.tokenize(text)
                lemmatizer = WordNetLemmatizer()
                text = lemmatizer.lemmatize(text) #lemma
                stem = ps.stem(text) #stemming
                if stem in dct and i in dct[stem]['docid']:
                    dct[stem]['pos'].append(pos)
                    dct_index = dct[stem]['docid'].index(i)
                    dct[stem]['tf'][dct_index] = dct[stem]['tf'][dct_index] + 1 
                elif stem in dct and i not in dct[stem]['docid']:
                    dct[stem]['docid'].append(i)
                    dct[stem]['tf'].append(1)
                    dct[stem]['pos'].append("and")
                    dct[stem]['pos'].append(pos)
                else:
                    dct[stem] = {
                        'docid' : [i],
                        'tf' : [1],
                        'pos' : [pos] }
        for k, g in groupby(enumerate(plot), lambda x: not x[1].isspace()):
            if k:
                pos, first_item = next(g)
                text = first_item + ''.join([x for _, x in g])
                ps = PorterStemmer() 
                text = text.casefold() #case folding
                tokenizer = RegexpTokenizer(r'\w+') # remove writing marks
                array = tokenizer.tokenize(text)
                lemmatizer = WordNetLemmatizer()
                text = lemmatizer.lemmatize(text) #lemma
                stem = ps.stem(text) #stemming
                if stem in dct1 and i in dct1[stem]['docid']:
                    dct1[stem]['pos'].append(pos)
                    dct1_index = dct1[stem]['docid'].index(i)
                    dct1[stem]['tf'][dct1_index] = dct1[stem]['tf'][dct1_index] + 1 
                elif stem in dct1 and i not in dct1[stem]['docid']:
                    dct1[stem]['docid'].append(i)
                    dct1[stem]['tf'].append(1)
                    dct1[stem]['pos'].append("and")
                    dct1[stem]['pos'].append(pos)
                else:
                    dct1[stem] = {
                        'docid' : [i],
                        'tf' : [1],
                        'pos' : [pos] }
        if i ==200:
            break

def add(string):
    id = string.split(",")[0]
    title = string.split(",")[1]
    plot = string.split(",")[2]
    id = int(id)
    exist = False
    for x in dct:
        if id in dct[x]['docid']:
            print("this id already exist")
            exist = True
            break
    if exist == False:
        for k, g in groupby(enumerate(title), lambda x: not x[1].isspace()):
            if k:
                pos, first_item = next(g)
                text = first_item + ''.join([x for _, x in g])
                ps = PorterStemmer() 
                text = text.casefold() #case folding
                tokenizer = RegexpTokenizer(r'\w+') # remove writing marks
                array = tokenizer.tokenize(text)
                lemmatizer = WordNetLemmatizer()
                text = lemmatizer.lemmatize(text) #lemma
                stem = ps.stem(text) #stemming
                if stem in dct and id in dct[stem]['docid']:
                    dct[stem]['pos'].append(pos)
                    dct_index = dct[stem]['docid'].index(id)
                    dct[stem]['tf'][dct_index] = dct[stem]['tf'][dct_index] + 1 
                elif stem in dct and id not in dct[stem]['docid']:
                    dct[stem]['docid'].append(id)
                    dct[stem]['tf'].append(1)
                    dct[stem]['pos'].append("and")
                    dct[stem]['pos'].append(pos)
                else:
                    dct[stem] = {
                        'docid' : [id],
                        'tf' : [1],
                        'pos' : [pos] }
        for k, g in groupby(enumerate(plot), lambda x: not x[1].isspace()):
            if k:
                pos, first_item = next(g)
                text = first_item + ''.join([x for _, x in g])
                ps = PorterStemmer() 
                text = text.casefold() #case folding
                tokenizer = RegexpTokenizer(r'\w+') # remove writing marks
                array = tokenizer.tokenize(text)
                lemmatizer = WordNetLemmatizer()
                text = lemmatizer.lemmatize(text) #lemma
                stem = ps.stem(text) #stemming
                if stem in dct1 and id in dct1[stem]['docid']:
                    dct1[stem]['pos'].append(pos)
                    dct1_index = dct1[stem]['docid'].index(id)
                    dct1[stem]['tf'][dct1_index] = dct1[stem]['tf'][dct1_index] + 1 
                    print(dct1[stem]['tf'][dct1_index])
                elif stem in dct1 and id not in dct1[stem]['docid']:
                    dct1[stem]['docid'].append(id)
                    dct1[stem]['tf'].append(1)
                    dct1[stem]['pos'].append("and")
                    dct1[stem]['pos'].append(pos)
                else:
                    dct1[stem] = {
                        'docid' : [id],
                        'tf' : [1],
                        'pos' : [pos] }


def delete(id):
    for x in dct:
        if id in dct[x]['docid']:
            length = len(dct[x]['docid'])    
            if length > 1:
                index = dct[x]['docid'].index(id)
                dct[x]['docid'].remove(id)
                deleted = dct[x]['tf'][index]
                dct[x]['tf'].remove(deleted)
                myitem = 0
                for m in dct[x]['pos'][:]:
                    if dct[x]['pos'] == "and":
                        myitem = myitem + 1
                    if myitem == index:
                        dct[x]['pos'].remove(m)
                if index == 0:
                    dct[x]['pos'].pop(0)
                break
            else:
                dct.pop(x)
                break
    for x in dct1:
        if id in dct1[x]['docid']:
            length = len(dct1[x]['docid'])    
            if length > 1:
                index = dct1[x]['docid'].index(id)
                dct1[x]['docid'].remove(id)
                deleted = dct1[x]['tf'][index]
                dct1[x]['tf'].remove(deleted)
                myitem = 0
                for m in dct1[x]['pos'][:]:
                    if m == "and":
                        myitem = myitem + 1
                    if myitem == index :
                        dct1[x]['pos'].remove(m)
                if index == 0:
                    dct1[x]['pos'].pop(0)
                break
            else:
                dct.pop(x)
                break

indexing()
menu = input("please choose\n1.indexing\n2.add\n3.delete\n")
if(menu=='1'):
    print(dct)
    print("\n\n\n")
    print(dct1)
if(menu=='2'):
    string = input("please enter your text that you wanna to add\n")
    add(string)
    print(dct)
    print("\n\n\n")
    print(dct1)
if(menu=='3'):
    id = int(input("please enter id\n"))
    delete(id)
    print(dct)
    print("\n\n\n")
    print(dct1)
