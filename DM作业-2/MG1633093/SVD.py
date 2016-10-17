from numpy import *
def file2matrix(filename):    #读入文档并对文档进行处理
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
	return datalist,datalabel   #返回特征集和label集合

def toSVD(data,numberofk):
	dataU,datasigma,datav=linalg.svd(data)  #应用linalg包进行svd处理
	selectu=[]
	for x in dataU:#选择前k列
		temu=x[:numberofk]
		selectu.append(temu)
	selectsigma=datasigma[:numberofk]#选择前k个sigma
	selectv=datav[:numberofk]#选择前k行
	finalv=selectv.T
	return finalv  #返回训练集的投影矩阵

def judgement(datatrainlist,datatrainlabel,datatestlist):
	testlabel=[]
	for x in range(len(datatestlist)):
		closest=[]
		distancefinal=[]
		for n in range(len(datatrainlist)):       #利用1-NN求出与待测数据最近的数据
			diffmat=datatestlist[x]-datatrainlist[n]
			sqdiffmatex=diffmat**2
			sqdiffmat=array(list(sqdiffmatex))
			sqdistance=sqdiffmat.sum()
			distance=sqdistance**0.5
			closest.append(distance)
		distancefinal=sorted(closest)
		number=closest.index(distancefinal[0])
		testlabel.append(datatrainlabel[closest.index(distancefinal[0])])   #取出最近的那个数据的label加入待判断集testlabel
	return testlabel
def finalpercentage(testlabel,turelabel):   #将判断集testlabel与标准测试集的label相比较得出准确率
	truenumber=0
	for x in range(len(turelabel)):
		if testlabel[x]==turelabel[x]:
			truenumber += 1
	print(truenumber)
	trueper=truenumber/len(turelabel)
	return trueper

if __name__ == '__main__': #对相应测试集进行测试
	datatrain,labeltrain=file2matrix('datatrain1.txt')
	datatest,labeltest=file2matrix('datatest1.txt')
	returndatatrain=dot(datatrain,toSVD(datatrain,10))
	returndatatest=dot(datatest,toSVD(datatrain,10))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=10):')
	print(trueper)
	returndatatrain=dot(datatrain,toSVD(datatrain,20))
	returndatatest=dot(datatest,toSVD(datatrain,20))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=20):')
	print(trueper)
	returndatatrain=dot(datatrain,toSVD(datatrain,30))
	returndatatest=dot(datatest,toSVD(datatrain,30))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 1 is(k=30):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain2.txt')
	datatest,labeltest=file2matrix('datatest2.txt')
	returndatatrain=dot(datatrain,toSVD(datatrain,10))
	returndatatest=dot(datatest,toSVD(datatrain,10))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=10):')
	print(trueper)
	returndatatrain=dot(datatrain,toSVD(datatrain,20))
	returndatatest=dot(datatest,toSVD(datatrain,20))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=20):')
	print(trueper)
	returndatatrain=dot(datatrain,toSVD(datatrain,30))
	returndatatest=dot(datatest,toSVD(datatrain,30))
	testlabel=judgement(returndatatrain,labeltrain,returndatatest)
	trueper=finalpercentage(testlabel,labeltest)
	print('the percentage of data 2 is(k=30):')
	print(trueper)