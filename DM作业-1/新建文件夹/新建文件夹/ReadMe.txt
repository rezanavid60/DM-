1、终端进入code以及数据所在的文件夹下，例如：D:\sublime\工程\DM作业-1
2、在命令行中输入stop=DM.stopwords(),读进停用词表；输入vocablist=DM.dictionary()
得到字典。
3、进入所有文档在的文件夹，输入allpaperinput=DM.allfile2matrix(stop)得到所有文档的输入，进入kernel文件夹输入
kernelpaperinput=DM.kernelfile2matrix(stop)得到kernel文档的输入。
4、进入主文件夹下，输入kernelpaperlist，classcount，allpaperlist=DM.file2matrix(vocablist,kernelpaperinput,allpaperinput)
得到计算TF-IDF的数据。
5、输入paperfinallist=DM.calTfIdf(kernelpaperlist,classcount,vocablist)得到kernel文档的TF-IDF。
6、输入DM.print2file(paperfinallist,vocablist)得到vocablist.txt以及result of DM.txt两文件。
