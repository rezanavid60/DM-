#-*- coding:utf-8 -*-
import math
import os
import fileinput

TEXT = 0  #某类别的文档数目
SUCCEED = 0
Docs = []

Path = 'D:\sublime\工程\DM作业-1'.encoding='utf-8'
w_Path = 'D:\sublime\工程\DM作业-1'.encoding='utf-8'

##计算权重函数，tf为某词在文章中出现的次数，df为包含该词的文档数，max文章中出现次数最多的词条数
##返回值为TF-IDF权重

##把特征向量按权重进行排序
def sort(terms,TF_IDF):
    for i in range(0,len(terms)):
        m = i
        for j in range(i+1,len(terms)):
            if TF_IDF[j]>TF_IDF[m]:
                m = j
        if i!=m:
            temp = terms[i]
            terms[i] = terms[m]
            terms[m] = temp
            v = TF_IDF[i]
            TF_IDF[i] = TF_IDF[m]
            TF_IDF[m] = v

def save_words(path):
    global Docs , TEXT
    terms = []
    fp = open(path,"r")
    while True:
        line = fp.readline()
        if not line : break
        terms.append(line)
    fp.close()
    Docs.append(terms)
    TEXT += 1

def GenerateIDF(path):
    global Docs , TEXT
    terms = []
    IDF = []
    idf = 0.0
    fp = open(path,"r")
    while True:
        line = fp.readline()
        if not line : break
        flag = 0
        for i in range(0,len(terms)):
            if line == terms[i]:
                flag = 1
        if flag == 0:
            terms.append(line)
    fp.close()
    for j in range(0,len(terms)):
        df = 0
        for i in range(0,len(Docs)):
            flag = 0
            doc = Docs[i]
            for k in range(0,len(doc)):
                if terms[j] == doc[k]:
                    flag = 1
                    break
            if flag == 1:
                df += 1
        idf = math.log(float(TEXT)/float(df)+0.01)
        IDF.append(idf)
    return IDF,terms

def GenerateTF(path,terms):
    all_terms = []
    TF = []
    terms_count = len(terms)
    fp = open(path,"r")
    while True:
        line = fp.readline()
        if not line : break
        all_terms.append(line)
    for i in terms:
        tf = 0
        for j in all_terms:
            if i == j:
                tf +=1
        TF.append(float(tf)/float(terms_count))
    fp.close()
    return TF

def save_weight(TF,IDF,terms,path):
    global SUCCEED
    TF_IDF = []
    top = 200
    if len(TF)<top:
        top = len(TF)
    for i in range(0,len(TF)):
        TF_IDF.append(float(TF[i])*float(IDF[i]))
    fp = open(path,"w+")
    sort(terms,TF_IDF)
    for i in range(0,top):
        string = terms[i].strip()+" "+str(TF_IDF[i])+'\n'
        fp.write(string)
        SUCCEED += 1
    fp.close()

def read_dir(path,w_path):
    global SUCCEED
    file_list = []
    files = os.listdir(path)
    print('please wait......')
    for f in files:
        file_list.append(f)
        r_name = path + '\\' + f
        save_words(r_name)
    print('sum of docs is:%d'%TEXT)
    for i in file_list:
        print(i)
        name = path + '\\' + i
        w_name = w_path + '\\' + i
        IDF,terms = GenerateIDF(name)
        TF = GenerateTF(name,terms)
        save_weight(TF,IDF,terms,w_name)
        print ('succeed:%d'%SUCCEED)

if __name__=="__main__":
    print("main")
    read_dir(Path,w_Path)
    print('-------------------Finished-----------------------')
