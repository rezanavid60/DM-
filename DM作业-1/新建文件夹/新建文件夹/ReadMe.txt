1���ն˽���code�Լ��������ڵ��ļ����£����磺D:\sublime\����\DM��ҵ-1
2����������������stop=DM.stopwords(),����ͣ�ôʱ�����vocablist=DM.dictionary()
�õ��ֵ䡣
3�����������ĵ��ڵ��ļ��У�����allpaperinput=DM.allfile2matrix(stop)�õ������ĵ������룬����kernel�ļ�������
kernelpaperinput=DM.kernelfile2matrix(stop)�õ�kernel�ĵ������롣
4���������ļ����£�����kernelpaperlist��classcount��allpaperlist=DM.file2matrix(vocablist,kernelpaperinput,allpaperinput)
�õ�����TF-IDF�����ݡ�
5������paperfinallist=DM.calTfIdf(kernelpaperlist,classcount,vocablist)�õ�kernel�ĵ���TF-IDF��
6������DM.print2file(paperfinallist,vocablist)�õ�vocablist.txt�Լ�result of DM.txt���ļ���
