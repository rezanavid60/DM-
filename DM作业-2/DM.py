from numpy import *
def file2matrix(filename):
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
	evalsex=argsort(evals)
	evalsex=evalsex[-1:-(numberofk+1):-1]
	evectsex=evects[:,evalsex]
	#returndatafinal=dot(stded,evectsex)
	#returndata=dot(returndatafinal,evectsex.T) + meandataofdata
	return evectsex

def judgement(datatrainlist,datatrainlabel,datatestlist):
	testlabel=[]
	for x in range(len(datatestlist)):
		closest=[]
		distancefinal=[]
		for n in range(len(datatrainlist)):
			diffmat=datatestlist[x]-datatrainlist[n]
			sqdiffmatex=diffmat**2
			sqdiffmat=array(list(sqdiffmatex))
			sqdistance=sqdiffmat.sum()
			distance=sqdistance**0.5
			closest.append(distance)
		distancefinal=sorted(closest)
		number=closest.index(distancefinal[0])
		testlabel.append(datatrainlabel[closest.index(distancefinal[0])])
	return testlabel

def finalpercentage(testlabel,turelabel):
	truenumber=0
	for x in range(len(turelabel)):
		if testlabel[x]==turelabel[x]:
			truenumber += 1
	print(truenumber)
	trueper=truenumber/len(turelabel)
	return trueper

if __name__ == '__main__':
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


