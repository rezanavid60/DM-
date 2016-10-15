from numpy import *
import os,shutil
import re,math,io
def txtfind():  #将ICML中所有txt文件集合中data文件夹中
    target_dir='D:\sublime\工程\DM作业-1\data'
    fileDir = 'D:\sublime\工程\DM作业-1' + os.sep + 'ICML'
    for root,dirs,files in os.walk(fileDir):
        for file in files:
            if file.endswith('.txt'):  #将以txt结尾的文件拷贝到data文件夹中
                shutil.copy(root+os.sep+file,target_dir)


def alltxttoone():  #将ICML中所有txt文件写到一个txt文件中（作业网站上要求感觉没什么用）
    target_dir='D:\sublime\工程\DM作业-1\data'
    li=os.listdir(target_dir)
    print(li)
    for i in li:
        f=open(i,'r',encoding='utf-8')
        addmore=f.read()
        fi=open('11.txt','a',encoding='utf-8')
        fi.write('/n'+addmore)
        f.close()
        fi.close()
def allfile2matrix(stopwords):#对所有文档paper数据进行处理返回所有paper的Word数组
    target_dir='D:\sublime\工程\DM作业-1\data'
    li=os.listdir(target_dir)
    number=len(li)
    stopwordsvector=stopwords
    fileVector=[]
    returnfilewords1=[]
    returnfilewords2=[]
    index=0
    for i in li:
        f=open(i,'r',encoding='utf-8')
        flines=f.readlines()
        returnfilewords1=[]
        for line in flines:
            line=line.strip()
            listfromline=re.split(r'\W',line) #以特殊符号划分词语
            for word in listfromline:
                lowword=word.lower()    #将大写字母小写化
                if len(lowword)>3 and re.search(r'\w*\d+\w*',lowword)==None and not lowword in stopwordsvector: #将包含数字特殊字符以及停用词的去掉
                    lowword1=re.findall(r'[a-zA-Z\s]+',lowword)  #只将由字母构成的单词留下
                    returnfilewords1.extend(lowword1)
                    returnfilewords1.sort()
        fileVector.append(returnfilewords1) 
        index += 1
        f.close()
    return fileVector   #返回一个fileVector的list，其中fileVector每个元素为一个list代表一篇paper,里面由处理后的单词组成

def stopwords():  #停用词加载
    stopwordsvector=[]
    fr1=open('stop.txt','r',encoding='utf-8')
    fr1lines=fr1.readlines()
    numberoffr1lines=len(fr1lines)
    for line in fr1lines:
        line = line.strip()
        listfromline = line.split()
        stopwordsvector.extend(listfromline)
    return stopwordsvector    #返回一个以停用词构成的list


def fun():
    with open('2.txt','r',encoding='utf-8')as f:
        content= f.readlines()
    with open('3.txt','w',encoding='utf-8')as f:
        for line in content:
            word=re.findall(r'[a-zA-Z\s]',line)
            str1=''
            for i in word:
                str1+=i
            str1+='\n'
            f.write(str1)

def alltxttoonestop(stopwords):#生成所有文档的字典集并将其写入2.txt文件中
    f=open('11.txt','r',encoding='utf-8')
    flines=f.readlines()
    returnfilewords1=[]
    returnfilewords2=[]
    stopwordsvector=stopwords
    for line in flines:
        line=line.strip()
        listfromline=re.split(r'\W',line)
        for word in listfromline:
            lowword=word.lower()
            if len(lowword)>3 and re.search(r'\w*\d+\w*',lowword)==None and not lowword in stopwordsvector: #和allfile2matrix函数中的一样处理单词
                returnfilewords1.append(lowword)
    returnfilewords2=list(set(returnfilewords1))
    print(len(returnfilewords2))
    returnfilewords2.sort()                
    fi=open('2.txt','a',encoding='utf-8')   #将处理完的结果写入2.txt文件中
    for l in range(len(returnfilewords2)):
        fi.write(returnfilewords2[l]+'\t')
    f.close()
    fi.close()


def dictionary():  #将字典集读出并保存到returnfilewords1这个list当中
    f=open('3.txt','r',encoding='utf-8')
    flines=f.readlines()
    returnfilewords1=[]
    for line in flines:
        line=line.strip()
        listfromline=line.split('\t')
        returnfilewords1.extend(listfromline)
    print(len(returnfilewords1))
    return returnfilewords1

def kernelfile2matrix(stopwords):#对kernel文件夹中的数据进行处理和allfile2matrix处理过程完全一样
    target_dir='D:\sublime\工程\DM作业-1\Kernel Methods'
    li=os.listdir(target_dir)
    number=len(li)
    stopwordsvector=stopwords
    fileVector=[]
    returnfilewords1=[]
    returnfilewords2=[]
    index=0
    for i in li:
        f=open(i,'r',encoding='utf-8')
        flines=f.readlines()
        returnfilewords1=[]
        for line in flines:
            line=line.strip()
            listfromline=re.split(r'\W',line)
            for word in listfromline:
                lowword=word.lower()
                if len(lowword)>3 and re.search(r'\w*\d+\w*',lowword)==None and not lowword in stopwordsvector:
                    lowword1=re.findall(r'[a-zA-Z\s]+',lowword)
                    returnfilewords1.extend(lowword1)
                    returnfilewords1.sort()
        fileVector.append(returnfilewords1)
        print(i)
        print(index)
        index += 1
        f.close()
    return fileVector
    
def file2matrix2(vocablist,input1,allfileinput):  #计算处理后的单词的词频
    numberofpaper=len(input1)
    classcount={}  #ICML当中所有txt文件中的单词出现情况以及出现次数的一个字典
    wordscount={}
    kernelpaperlist=[] #kernel文件夹中各篇paper单词出现情况以及次数
    allpaperlist=[]   #ICML当中各篇paper单词出现情况及其次数（其中元素为字典）
    for i in vocablist:
        classcount[i]=0
    for x in range(numberofpaper): #计算kernel文件夹中每篇文章的出现情况
        for word in input1[x]:
            if word in classcount.keys():
                wordscount[word] = input1[x].count(word)
        kernelpaperlist.append(wordscount)
        wordscount={}
    for x in range(len(allfileinput)):#计算所有文档中每篇文章的出现情况
        for word in allfileinput[x]:
            if word in classcount.keys():
                wordscount[word] = allfileinput[x].count(word)
        allpaperlist.append(wordscount)
        wordscount={}
        for w in classcount:  #计算总的单词出现次数
            if w in allpaperlist[x]:
                classcount[w] += 1
    return kernelpaperlist,classcount,allpaperlist

def calTfIdf(paperlistex,classcountex,vocablist):  #计算TF-IDF
    paperlist=[]
    paperlistex1=paperlistex
    paperlistfin=[]
    classcountall={}
    TFcount=[]
    classcountall=classcountex
    length=len(classcountex)
    number=len(paperlistex1)
    for x1 in classcountall.keys():  #计算IDF其中log以10为底
        if classcountall[x1] != 0:
            classcountall[x1]=log10(580.0000/classcountall[x1])
    for i in range(number):  #计算TF情况
        all1=0   #all为每篇文章处理过后的单词总数
        for x2 in classcountall.keys():
            if x2 in paperlistex1[i].keys():
                all1 =all1+paperlistex1[i][x2]
        paperlistfin.append(all1)
    for z in range(number):
        for n2 in paperlistex1[z].keys():

            paperlistex1[z][n2]=(paperlistex1[z][n2])/float(paperlistfin[z])
        TFcount.append(paperlistex1)
    paperlistfinal=paperlistex1
    for x3 in range(number):  #将TF与IDF相乘得出结果
    	for n3 in paperlistex1[x3].keys():
    		if n3 in classcountall.keys():
    			paperlistfinal[x3][n3]=classcountall[n3]*paperlistex1[x3][n3]
    return paperlistfinal  #返回一个list，其中list元素为字典（一个字典代表一篇文章），字典当中保存单词以及相应的tf-idf


def print2file(paperlistexample,vocablist):#将vocablist以及kernel当中文件的tf-idf写入相应txt文件中
	vocablistexample=sorted(vocablist)
	f=open('vocablist.txt','a',encoding='utf-8')
	for x1 in range(len(vocablist)):
		f.write(vocablistexample[x1]+'\t')
	f.close()
	fi=open('result of DM.txt','a',encoding='utf-8')
	for i in range(len(paperlistexample)):
		for x in vocablistexample:
			if x in paperlistexample[i].keys():
				fi.write(str(vocablistexample.index(x))+':'+str(paperlistexample[i][x])+'\t')
	fi.close()
   
