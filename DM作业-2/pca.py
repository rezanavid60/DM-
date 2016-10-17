from numpy import *
def file2matrix(filename):  #读入文档并对文档进行处理
	datalist=[]
	datalabel=[]
	datalistex=[]
	f=open(filename,'r',encoding='utf-8')
	fi1=f.readlines()
	for fi in fi1:
		fi=fi.strip()
		filist=fi.split(',')
		datalistex=[]
		for x in range(len(filist)-1):
			datalistex.append(float(filist[x]))
		datalist.append(datalistex)
		datalabel.append(float(filist[-1]))
	return datalist,datalabel

def toPCA(datalist,numberofk):
	dataarray = array(datalist)
	meandataofdata = mean(dataarray,axis=0)
	dataminusmean = dataarray - meandataofdata
	stded=dataminusmean/std(dataminusmean,axis=0)
	covdata = cov(stded,rowvar=0) #对每列求协方差
	evals,evects=linalg.eig(covdata)
	evalsex=argsort(evals)   #对特征值从小到大排序
	evalsex=evalsex[-1:-(numberofk+1):-1]  #取最大的前k个特征值
	evectsex=evects[:,evalsex]   #取与特征值相应的前k个特征向量
	return evectsex       #返回训练集的投影矩阵

def judgement(datatrainlist,datatrainlabel,datatestlist): 
	testlabel=[]
	for x in range(len(datatestlist)):
		closest=[]
		distancefinal=[]
		for n in range(len(datatrainlist)):   #利用1-NN求出与待测数据最近的数据
			diffmat=datatestlist[x]-datatrainlist[n]
			sqdiffmatex=diffmat**2
			sqdiffmat=array(list(sqdiffmatex))
			sqdistance=sqdiffmat.sum()
			distance=sqdistance**0.5
			closest.append(distance)
		distancefinal=sorted(closest)
		number=closest.index(distancefinal[0]) 
		testlabel.append(datatrainlabel[closest.index(distancefinal[0])])  #取出最近的那个数据的label加入待判断集testlabel
	return testlabel

def finalpercentage(testlabel,turelabel):  #将判断集testlabel与标准测试集的label相比较得出准确率
	truenumber=0
	for x in range(len(turelabel)):
		if testlabel[x]==turelabel[x]:
			truenumber += 1
	print(truenumber)
	trueper=truenumber/len(turelabel)
	return trueper

if __name__ == '__main__':  #对相应测试集进行测试
	datatrain,labeltrain=file2matrix('datatrain1.txt')
	datatest,labeltest=file2matrix('datatest1.txt')
	returndatatrain=dot(datatrain,toPCA(datatrain,10))
	returndatatest=dot(datatest,toPCA(datatrain,10))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=10):')
	print(trueper)
	returndatatrain=dot(datatrain,toPCA(datatrain,20))
	returndatatest=dot(datatest,toPCA(datatrain,20))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=20):')
	print(trueper)
	returndatatrain=dot(datatrain,toPCA(datatrain,30))
	returndatatest=dot(datatest,toPCA(datatrain,30))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=30):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain2.txt')
	datatest,labeltest=file2matrix('datatest2.txt')
	returndatatrain=dot(datatrain,toPCA(datatrain,10))
	returndatatest=dot(datatest,toPCA(datatrain,10))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=10):')
	print(trueper)
	returndatatrain=dot(datatrain,toPCA(datatrain,20))
	returndatatest=dot(datatest,toPCA(datatrain,20))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=20):')
	print(trueper)
	returndatatrain=dot(datatrain,toPCA(datatrain,30))
	returndatatest=dot(datatest,toPCA(datatrain,30))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=30):')
	print(trueper)


