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
def two2onedata(datatrain,datatest):
	dataall=[]
	for x in datatrain:
		dataall.append(x)
	for n in datatest:
		dataall.append(n)
	return dataall

def toMDS(data,numberofk):
	nofdata=shape(data)[0]
	dataarray=array(data)
	sqrdata=dot(dataarray,dataarray.T)
	H=eye(nofdata)-1.0/nofdata
	T=-0.5 * dot(dot(H,sqrdata),H)
	evals,evects=linalg.eig(T)
	evalsex=argsort(evals)
	evalsex=evalsex[-1:-(numberofk+1):-1]
	evectsex=evects[:,evalsex]
	diagvec=diag(sqrt(evalsex))
	returndata=dot(evectsex,diagvec)
	return returndata

def toisomap(data):
	dictnode={}
	dictweight={}
	temdistance=[]
	distancelabel=[]
	for x in range(len(data)):
		closest=[]
		distancefinal=[]
		distancelabeltem=[]
		for n in range(len(data)):
			diffmat=array(data[x])-array(data[n])
			sqdiffmatex=diffmat**2
			sqdiffmat=array(list(sqdiffmatex))
			sqdistance=sqdiffmat.sum()
			distance=sqdistance**0.5
			closest.append(distance)
		distancefinal=sorted(closest)
		temdistance.append(distancefinal[1:5])
		for i in range(4):
			distancelabeltem.append(closest.index(distancefinal[i+1]))
		distancelabel.append(distancelabeltem)
	return temdistance,distancelabel

def datagraph(distance,label):
	graphyarray=zeros([len(distance),len(distance)])
	for x in range(len(graphyarray)):
		for n in range(4):
			graphyarray[x][label[x][n]]=distance[x][n]
	for i in range(len(graphyarray)):
		for j in range(len(graphyarray)):
			if graphyarray[i][j] == 0:
				graphyarray[i][j]=10000
			graphyarray[i][i]=0
	return graphyarray

def dijk(graphyarray):
	dij=graphyarray
	for k in range(len(graphyarray)):
		for i in range(len(graphyarray)):
			for j in range(len(graphyarray)):
				if dij[i][j]> dij[i][k]+dij[k][j]:
					dij[i][j] = dij[i][k]+dij[k][j]
	dij=dij**2
	return dij

def judgement(returndatatrain,returndatatest,labeltrain):
	testlabel=[]
	for x in range(len(returndatatest)):
		distanceex=[]
		for n in range(len(returndatatrain)):
			line=linalg.norm(returndatatest[x]-returndatatrain[n])
			distanceex.append(line)
		distancetem=sorted(distanceex)
		#number=distanceex.index(distancetem[0])
		testlabel.append(labeltrain[distanceex.index(distancetem[0])])
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
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,10)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 1 is(k=10):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain1.txt')
	datatest,labeltest=file2matrix('datatest1.txt')
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,20)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 1 is(k=20):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain1.txt')
	datatest,labeltest=file2matrix('datatest1.txt')
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,30)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 1 is(k=30):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain2.txt')
	datatest,labeltest=file2matrix('datatest2.txt')
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,10)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 2 is(k=10):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain2.txt')
	datatest,labeltest=file2matrix('datatest2.txt')
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,20)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 2 is(k=20):')
	print(trueper)
	datatrain,labeltrain=file2matrix('datatrain2.txt')
	datatest,labeltest=file2matrix('datatest2.txt')
	dataall=two2onedata(datatrain,datatest)
	temdistance,distancelabel=toisomap(dataall)
	graphyarray=datagraph(temdistance,distancelabel)
	dij=dijk(graphyarray)
	returndata=toMDS(dij,30)
	returndatatrain=returndata[0:len(datatrain)]
	returndatatest=returndata[len(datatrain):len(returndata)]
	testlabel=judgement(returndatatrain,returndatatest,labeltrain)
	trueper=finalpercentage(labeltest,testlabel)
	print('the percentage of data 2 is(k=30):')
	print(trueper)